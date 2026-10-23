#!/usr/bin/env python3
"""Bounded, cached source windows for local mathematics PDFs.

The helper intentionally uses the already-installed Poppler executables.  It
does not discover or load a document runtime.  Every request is page-bounded,
time-bounded, and cached against the source file's path, size, and mtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


VAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = VAULT_ROOT / "library.yml"
DEFAULT_CACHE = VAULT_ROOT / "Infrastructure/source_cache/pdf_windows"
TOOLS = ("pdfinfo", "pdftotext", "pdftoppm")
DEFAULT_TIMEOUT_SECONDS = 45
DEFAULT_MAX_PAGES = 4
DEFAULT_MAX_CACHE_MB = 512
MAX_EXCERPT_CHARS = 20_000


class SourceWindowError(RuntimeError):
    """A source request is unsafe, unavailable, or failed."""


def emit(payload: Dict[str, object]) -> int:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def library_pdf(book_id: str, library_path: Path) -> Path:
    """Read one `books.<id>.pdf` entry without importing a YAML package."""
    try:
        lines = library_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise SourceWindowError(
            f"cannot read library index {library_path}: {exc}"
        ) from exc
    in_book = False
    for line in lines:
        if re.fullmatch(rf"  {re.escape(book_id)}:", line):
            in_book = True
            continue
        if in_book and re.fullmatch(r"  [a-z0-9_]+:", line):
            break
        if in_book:
            match = re.fullmatch(r"    pdf: (.+)", line)
            if match:
                try:
                    value = json.loads(match.group(1))
                except json.JSONDecodeError as exc:
                    raise SourceWindowError(
                        f"invalid pdf entry for {book_id}"
                    ) from exc
                return Path(value).expanduser().resolve()
    raise SourceWindowError(
        f"library book has no local PDF entry: {book_id}"
    )


def resolve_source(args: argparse.Namespace) -> Tuple[Path, str]:
    if args.pdf is not None:
        source = args.pdf.expanduser().resolve()
        label = source.stem
    else:
        source = library_pdf(args.book_id, args.library)
        label = args.book_id
    if not source.is_file():
        raise SourceWindowError(f"source PDF does not exist: {source}")
    if source.suffix.lower() != ".pdf":
        raise SourceWindowError(f"source is not a PDF: {source}")
    return source, label


def tool_paths() -> Dict[str, str]:
    found: Dict[str, str] = {}
    missing: List[str] = []
    for name in TOOLS:
        path = shutil.which(name)
        if path is None:
            missing.append(name)
        else:
            found[name] = path
    if missing:
        raise SourceWindowError(
            "missing local Poppler tools: " + ", ".join(missing)
        )
    return found


def run_bounded(
    command: List[str], timeout_seconds: int
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise SourceWindowError(
            f"source tool timed out after {timeout_seconds}s: {command[0]}"
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()[-1000:]
        raise SourceWindowError(
            f"source tool failed ({command[0]}): {detail}"
        ) from exc


def page_count(
    source: Path, tools: Dict[str, str], timeout_seconds: int
) -> int:
    result = run_bounded(
        [tools["pdfinfo"], str(source)], timeout_seconds
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise SourceWindowError("pdfinfo did not report a page count")
    return int(match.group(1))


def source_fingerprint(source: Path) -> str:
    stat = source.stat()
    material = (
        f"{source}\0{stat.st_size}\0{stat.st_mtime_ns}".encode("utf-8")
    )
    return hashlib.sha256(material).hexdigest()[:20]


def safe_label(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return (cleaned or "source")[:80]


def atomic_target(path: Path) -> Path:
    return path.with_name(
        f".{path.name}.tmp-{os.getpid()}-{uuid.uuid4().hex}"
    )


def touch(path: Path) -> None:
    try:
        os.utime(path, None)
    except OSError:
        pass


def cleanup_stale_temporaries(
    cache_root: Path, minimum_age_seconds: int = 600
) -> int:
    if not cache_root.exists():
        return 0
    cutoff = time.time() - minimum_age_seconds
    removed = 0
    for path in cache_root.rglob(".*.tmp-*"):
        if path.is_file() and path.stat().st_mtime < cutoff:
            path.unlink()
            removed += 1
    return removed


def extract_text_page(
    source: Path,
    page: int,
    destination: Path,
    tools: Dict[str, str],
    timeout_seconds: int,
) -> bool:
    if destination.is_file():
        touch(destination)
        return True
    temporary = atomic_target(destination)
    try:
        run_bounded(
            [
                tools["pdftotext"],
                "-f",
                str(page),
                "-l",
                str(page),
                "-layout",
                "-enc",
                "UTF-8",
                str(source),
                str(temporary),
            ],
            timeout_seconds,
        )
        os.replace(str(temporary), str(destination))
    finally:
        if temporary.exists():
            temporary.unlink()
    return False


def render_page(
    source: Path,
    page: int,
    dpi: int,
    destination: Path,
    tools: Dict[str, str],
    timeout_seconds: int,
) -> bool:
    if destination.is_file() and destination.stat().st_size > 0:
        touch(destination)
        return True
    temporary_stem = atomic_target(destination.with_suffix(""))
    temporary_png = Path(f"{temporary_stem}.png")
    try:
        run_bounded(
            [
                tools["pdftoppm"],
                "-f",
                str(page),
                "-l",
                str(page),
                "-r",
                str(dpi),
                "-png",
                "-singlefile",
                str(source),
                str(temporary_stem),
            ],
            timeout_seconds,
        )
        if not temporary_png.is_file():
            raise SourceWindowError("pdftoppm did not create the page image")
        os.replace(str(temporary_png), str(destination))
    finally:
        if temporary_png.exists():
            temporary_png.unlink()
    return False


def iter_cache_files(cache_root: Path) -> Iterable[Path]:
    if not cache_root.exists():
        return ()
    return (
        path
        for path in cache_root.rglob("*")
        if path.is_file() and not path.name.startswith(".")
    )


def prune_cache(
    cache_root: Path, max_cache_mb: int, protected: Iterable[Path]
) -> int:
    limit = max_cache_mb * 1024 * 1024
    protected_set = {path.resolve() for path in protected}
    files = list(iter_cache_files(cache_root))
    total = sum(path.stat().st_size for path in files)
    removed = 0
    if total <= limit:
        return removed
    files.sort(key=lambda path: path.stat().st_mtime)
    for path in files:
        if total <= limit:
            break
        if path.resolve() in protected_set:
            continue
        size = path.stat().st_size
        path.unlink()
        total -= size
        removed += 1
    return removed


def validate_window(
    first: int, last: int, pages: int, max_pages: int
) -> None:
    if first < 1 or last < first:
        raise SourceWindowError("invalid page window")
    if last > pages:
        raise SourceWindowError(
            f"page window ends at {last}, but source has {pages} pages"
        )
    if last - first + 1 > max_pages:
        raise SourceWindowError(
            f"page window exceeds the {max_pages}-page safety bound"
        )


def prepare(args: argparse.Namespace) -> Dict[str, object]:
    started = time.monotonic()
    stale_temporaries_removed = cleanup_stale_temporaries(args.cache_root)
    source, label = resolve_source(args)
    tools = tool_paths()
    pages = page_count(source, tools, args.timeout_seconds)
    validate_window(args.first, args.last, pages, args.max_pages)
    fingerprint = source_fingerprint(source)
    directory = (
        args.cache_root
        / safe_label(label)
        / fingerprint
    )
    directory.mkdir(parents=True, exist_ok=True)

    want_text = args.text or not args.render
    want_render = args.render
    text_files: List[Path] = []
    image_files: List[Path] = []
    hits = 0
    misses = 0
    empty_text_pages: List[int] = []
    for page in range(args.first, args.last + 1):
        if want_text:
            text_path = directory / f"page-{page:04d}.txt"
            hit = extract_text_page(
                source,
                page,
                text_path,
                tools,
                args.timeout_seconds,
            )
            hits += int(hit)
            misses += int(not hit)
            text_files.append(text_path)
            if not text_path.read_text(
                encoding="utf-8", errors="replace"
            ).strip():
                empty_text_pages.append(page)
        if want_render:
            image_path = directory / f"page-{page:04d}-r{args.dpi}.png"
            hit = render_page(
                source,
                page,
                args.dpi,
                image_path,
                tools,
                args.timeout_seconds,
            )
            hits += int(hit)
            misses += int(not hit)
            image_files.append(image_path)

    protected = [*text_files, *image_files]
    removed = prune_cache(
        args.cache_root, args.max_cache_mb, protected
    )
    return {
        "decision": "SOURCE_WINDOW_READY",
        "source": str(source),
        "source_fingerprint": fingerprint,
        "page_count": pages,
        "first_page": args.first,
        "last_page": args.last,
        "text_files": [str(path) for path in text_files],
        "image_files": [str(path) for path in image_files],
        "empty_text_pages": empty_text_pages,
        "cache_hits": hits,
        "cache_misses": misses,
        "cache_files_pruned": removed,
        "stale_temporaries_removed": stale_temporaries_removed,
        "cache_root": str(args.cache_root),
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


def command_doctor(args: argparse.Namespace) -> int:
    tools = tool_paths()
    args.cache_root.mkdir(parents=True, exist_ok=True)
    probe = args.cache_root / f".write-probe-{os.getpid()}"
    try:
        probe.write_text("ok", encoding="utf-8")
    finally:
        if probe.exists():
            probe.unlink()
    payload: Dict[str, object] = {
        "decision": "SOURCE_WINDOW_DOCTOR_OK",
        "tools": tools,
        "cache_root": str(args.cache_root),
        "cache_writable": os.access(args.cache_root, os.W_OK),
    }
    if args.book_id is not None or args.pdf is not None:
        source, _ = resolve_source(args)
        payload["source"] = str(source)
        payload["source_exists"] = True
    return emit(payload)


def command_prepare(args: argparse.Namespace) -> int:
    return emit(prepare(args))


def command_excerpt(args: argparse.Namespace) -> int:
    args.text = True
    args.render = False
    result = prepare(args)
    remaining = min(args.max_chars, MAX_EXCERPT_CHARS)
    print(
        f"# SOURCE WINDOW pages {args.first}-{args.last} "
        f"fingerprint {result['source_fingerprint']}"
    )
    for path_text in result["text_files"]:
        path = Path(path_text)
        page_match = re.search(r"page-(\d+)", path.name)
        page = page_match.group(1) if page_match else "?"
        text = path.read_text(encoding="utf-8", errors="replace")
        excerpt = text[:remaining]
        print(f"\n## PDF page {int(page)}\n{excerpt}")
        remaining -= len(excerpt)
        if remaining <= 0:
            print("\n[excerpt truncated by source_window.py]")
            break
    return 0


def add_source_arguments(parser: argparse.ArgumentParser) -> None:
    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--book-id")
    source.add_argument("--pdf", type=Path)
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    parser.add_argument("--cache-root", type=Path, default=DEFAULT_CACHE)


def add_window_arguments(parser: argparse.ArgumentParser) -> None:
    add_source_arguments(parser)
    parser.add_argument("--first", type=int, required=True)
    parser.add_argument("--last", type=int, required=True)
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    parser.add_argument(
        "--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS
    )
    parser.add_argument(
        "--max-cache-mb", type=int, default=DEFAULT_MAX_CACHE_MB
    )
    parser.add_argument("--dpi", type=int, default=160)
    parser.add_argument("--text", action="store_true")
    parser.add_argument("--render", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor")
    add_source_arguments(doctor)
    doctor.set_defaults(handler=command_doctor)

    prepare_parser = subparsers.add_parser("prepare")
    add_window_arguments(prepare_parser)
    prepare_parser.set_defaults(handler=command_prepare)

    excerpt = subparsers.add_parser("excerpt")
    add_window_arguments(excerpt)
    excerpt.add_argument("--max-chars", type=int, default=12_000)
    excerpt.set_defaults(handler=command_excerpt)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "doctor" and args.book_id is None and args.pdf is None:
        pass
    elif args.book_id is None and args.pdf is None:
        raise SourceWindowError("--book-id or --pdf is required")
    if hasattr(args, "timeout_seconds") and args.timeout_seconds < 1:
        raise SourceWindowError("--timeout-seconds must be positive")
    if hasattr(args, "max_pages") and not 1 <= args.max_pages <= 8:
        raise SourceWindowError("--max-pages must be between 1 and 8")
    if hasattr(args, "dpi") and not 72 <= args.dpi <= 240:
        raise SourceWindowError("--dpi must be between 72 and 240")
    if hasattr(args, "max_chars") and not 1 <= args.max_chars <= MAX_EXCERPT_CHARS:
        raise SourceWindowError(
            f"--max-chars must be between 1 and {MAX_EXCERPT_CHARS}"
        )
    return args.handler(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SourceWindowError as exc:
        print(
            json.dumps(
                {"decision": "SOURCE_WINDOW_ERROR", "error": str(exc)},
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        raise SystemExit(1)
