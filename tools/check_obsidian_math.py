#!/usr/bin/env python3
"""Check Markdown math delimiters for Obsidian/Codex compatibility.

This script is read-only. It reports common rendering hazards:

- display delimiters written as \[ or \]
- inline delimiters written as \( or \)
- bare bracket lines [ or ], which often come from broken display math
- unmatched $$ display delimiters

The scan ignores fenced code blocks, YAML front matter, inline code spans, the
vault backup folders, tmp folders, and .obsidian configuration.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_VAULT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".obsidian", "tmp", "backups"}
RAW_INLINE_DELIM_RE = re.compile(r"(?<!\\)\\[()]")
RAW_DISPLAY_DELIM_RE = re.compile(r"(?<!\\)\\[\[\]]")


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        rel_parts = set(path.relative_to(root).parts)
        if EXCLUDED_PARTS & rel_parts:
            continue
        yield path


def is_fence(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def strip_inline_code(line: str) -> str:
    parts = line.split("`")
    for idx in range(1, len(parts), 2):
        parts[idx] = ""
    return "`".join(parts)


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    issues: list[tuple[int, str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    in_front_matter = bool(lines and lines[0].strip() == "---")
    display_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        if idx != 1 and in_front_matter and stripped == "---":
            in_front_matter = False
            continue
        if in_front_matter:
            continue

        if is_fence(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        visible = strip_inline_code(line)
        visible_stripped = visible.strip()

        if visible_stripped == "$$":
            display_count += 1
            continue

        if visible_stripped in {r"\[", r"\]"}:
            issues.append((idx, "raw_display_delimiter", stripped))
        elif visible_stripped in {"[", "]"}:
            issues.append((idx, "bare_bracket_display_delimiter", stripped))

        if RAW_INLINE_DELIM_RE.search(visible):
            issues.append((idx, "raw_inline_delimiter", stripped))
        if RAW_DISPLAY_DELIM_RE.search(visible):
            issues.append((idx, "raw_display_delimiter_inline", stripped))

    if display_count % 2:
        issues.append((0, "unmatched_display_dollars", f"$$ count is {display_count}"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(DEFAULT_VAULT))
    parser.add_argument("--limit", type=int, default=120)
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    all_issues: list[tuple[Path, int, str, str]] = []

    for path in iter_markdown_files(root):
        for line_no, kind, snippet in scan_file(path):
            all_issues.append((path, line_no, kind, snippet))

    print(f"root: {root}")
    print(f"issues: {len(all_issues)}")

    for path, line_no, kind, snippet in all_issues[: args.limit]:
        rel = path.relative_to(root)
        loc = f"{rel}:{line_no}" if line_no else str(rel)
        print(f"{loc}: {kind}: {snippet}")

    if len(all_issues) > args.limit:
        print(f"... {len(all_issues) - args.limit} more issues")

    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
