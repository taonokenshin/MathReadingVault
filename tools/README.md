# Extracted local reading tools

These are experimental utilities extracted from a working personal mathematical reading workflow. They coordinate local work and source lookup; they do not prove theorems, certify notes or install a scheduler.

## Quick checks

Python 3.9 or later is sufficient for the controller, its tests, and the Markdown checker. From the repository root:

```sh
python3 -m unittest discover -s tools -p 'test_manual_batch_control.py' -v
python3 examples/synthetic-control/smoke_demo.py
python3 tools/manual_batch_control.py --help
python3 tools/source_window.py --help
python3 tools/check_obsidian_math.py --help
```

The existing 41 controller tests create temporary vault and automation roots. The smoke demonstration also creates only temporary configuration and runtime, simulates activation, checks competing ownership, then aborts without counting a mathematical session. Neither command reads or changes your actual Codex automations.

## `manual_batch_control.py`

Commands emit JSON decisions. The repository-relative default vault root is the parent of `tools/`; the default automation root is the isolated `.local-automations/` below that repository. It never defaults to your real Codex automation directory. Explicit `--vault-root` and `--automations-root` remain available for a deliberately configured installation.

This extraction preserves the original fixed `SPECS`: historical reading-lane names, shared locks for auxiliary tasks, twelve-session main batches, one-session auxiliary batches, timing contracts and migration compatibility. It is not yet a configurable general-purpose scheduler package. A real installation needs a deliberate mapping, a compatible automation adapter, task identity supplied by the execution environment, and private runtime initialization. Do not impersonate an existing task identity. There is no credential discovery or automatic scheduler registration.

`complete` checks ownership, order, elapsed duration and leases. It cannot know that the agent spent the time on mathematics or that a submitted proof is correct. `PAUSE_SELF` requests an external scheduler action; the Python script does not itself call the Codex application. The explicit `credit-interrupted --user-authorized` path is limited administrative recovery, not permission for an autonomous agent to count arbitrary failures.

## `source_window.py`

Requires the external Poppler commands `pdfinfo`, `pdftotext`, and `pdftoppm` on `PATH`. No textbook PDF is included. Use a PDF you are entitled to access, and a private cache:

```sh
python3 tools/source_window.py prepare --pdf /path/to/your-book.pdf --first 1 --last 2 --text --render --cache-root /path/to/private-cache
```

The default request limit is four pages and each subprocess has a 45-second timeout. The implementation permits an explicit maximum of up to eight pages; the original mathematical workflow keeps the four-page convention. Rendering images and extracted text inherit the source's distribution restrictions. Cache files must remain private when the source is private.

`--book-id` reads a narrow local `library.yml` convention, not general YAML. The optional example is:

```yaml
books:
  example_book:
    pdf: "/absolute/path/to/a-lawfully-accessed.pdf"
```

The default library is the repository's `library.yml`, and the default cache is `Infrastructure/source_cache/pdf_windows/` below the repository. Neither is bundled. Prefer explicit private paths. A cache fingerprint uses source path, size and modification time; it is not a content hash or authenticated archival record.

## `check_obsidian_math.py`

```sh
python3 tools/check_obsidian_math.py /path/to/selected-markdown-folder
```

This read-only heuristic reports common Obsidian delimiter hazards while skipping fenced code, YAML front matter and selected internal folders. It does not parse all LaTeX, verify inline math comprehensively, inspect rendered pages or audit mathematics. Pass a narrow directory containing your changed files; running without a path scans this repository.

## Extraction changes and scope

The four source files preserve their original filenames and test import. Only personal default roots were replaced: repository root for the vault/library/checker, and repository-local `.local-automations/` for automation configuration. Controller logic, timing values, named lane mappings and the existing tests were retained. The synthetic demonstration is newly added public example code.

Private state, lock ownership, automation configuration, memory, account/quota tools, source caches and commercial book files are deliberately absent. Documentation and tests describe observed behavior; no formal concurrency guarantee, mathematical proof verification, learning-outcome study or cross-platform validation is claimed.

## Recorded local verification

On 23 October 2026, using Python 3.9.6 on the maintainer's MacBook, the copied controller suite passed all 41 tests. The synthetic demo passed its activation, ownership, heartbeat and noncounted-abort checks, and all three tool `--help` commands exited successfully. `verification_results.json` records the commands and actual results. No private PDF extraction or real scheduler interaction was tested. `extraction_manifest.json` records source/public hashes and an AST comparison confirming that the reviewed code differs only in the listed default-root assignments; the existing test file is byte-identical to its source version.
