# MathReadingVault

**Open infrastructure and evidence-linked study materials for sustained mathematics learning and research.**

MathReadingVault is a learner-directed project built with Codex assistance. It preserves mathematical reasoning across bounded sessions: the question being studied, the assumptions used, an attempted proof, a counterexample or failed route, source locations, corrections, and the exact next step. The maintainer sets the goals and standards; the agent plans the mathematical work within those boundaries.

The aim is to help students and researchers build a reusable record of understanding. A useful reading note explains why a definition appears, how a theorem uses its hypotheses, what a calculation establishes, and what remains unresolved. An interruption should leave a precise continuation that another session or learner can follow.

## Start with a real example

- [Marcus and Neukirch: 12 complete English mathematical case studies](case-studies/marcus-neukirch/INDEX.md), spanning algebraic integers, local fields, class field theory, zeta functions and prime distribution.
- [Seven other study lanes](docs/OTHER_LANES.md), with 14 mathematical excerpts and seven educational run histories: Apostol, Stein–Shakarchi, Cohen, Dieudonné, Serre, Lang and Brualdi.
- [Public English study archive](https://github.com/taonokenshin/MathReadingVault/releases/tag/study-edition-2026-10-20): 1,152 mathematical articles and 1,124 normalized session records, in textbook order, from the 20 October 2026 snapshot. File counts include drafts and historical corrections; they are not theorem or proof counts.

The repository offers English guides and English Marcus/Neukirch articles. Additional original Chinese excerpts have detailed English introductions. The recipient is free to choose their own primary book, topic, pace and rigor.

## What is reusable

| Component | Function | Evidence |
| --- | --- | --- |
| [Deterministic controller](tools/manual_batch_control.py) | Claim ownership, bound a session, retain interrupted work, count a fixed batch, request and confirm a pause | [41 existing isolated tests](tools/test_manual_batch_control.py) and a [synthetic demonstration](examples/synthetic-control/README.md) |
| [Bounded source windows](tools/source_window.py) | Work with a small, page-limited local PDF window and explicit source locators | Default four-page window; external Poppler tools; no source PDFs included |
| [Markdown transport check](tools/check_obsidian_math.py) | Find selected Obsidian delimiter hazards | Read-only heuristic; no theorem checking or GUI-render claim |
| [Mathematical handoff templates](templates/CONTINUATION.md) | Preserve exact inputs, proved/cited/attempted distinctions, a failed approach and a next step | Derived from durable study records |
| [Study archive export](tools/build_public_study_release.py) | Produce a public reading layer with source hashes and privacy-filtered references | Original private archive, runtime and account data excluded |

The toolkit is an experimental extraction of a working personal workflow. Its controller retains named historical lane mappings and needs deliberate local adaptation; it does not install a scheduler or automatically manage your account.

## Try the software locally

Python 3.9+; no API key or model call is required for the tests.

```sh
python3 -m unittest discover -s tools -p 'test_manual_batch_control.py' -v
python3 examples/synthetic-control/smoke_demo.py
python3 tools/check_obsidian_math.py case-studies
```

The first two commands use disposable fixture roots. They do not access real Codex automations. See [tool instructions](tools/README.md), [architecture](docs/ARCHITECTURE.md), and [the short reading protocol](docs/READING_PROTOCOL.md). Source-window rendering separately requires Poppler and a PDF you may lawfully access.

## Educational and research value

The case studies make hidden assumptions and normalization choices inspectable. Examples include canonical versus Lebesgue covolumes, three mechanisms behind Hilbert 90, an integral carry term missed by a dimension count, a locally valid estimate that does not justify a global conclusion, and parameter-dependent module actions that cannot be interchanged. Correction histories retain the earlier failure and the narrower usable statement.

For research preparation, exact continuations preserve a difficult local interface over multiple sessions. Source-cited inputs, reader arguments, finite computational guards and remaining gaps have separate labels. This is useful material for studying the behavior of long-running mathematical assistants: interruption recovery, scope preservation, dependency reuse and correction handling. It does not establish new mathematics or measured learning gains.

## Progress and development

The project has durable reading records across several mathematical areas. The [dated portfolio](docs/OTHER_LANES.md) distinguishes completed subranges, support books and gates. The [archive guide](docs/ARCHIVE.md) explains the Marcus/Neukirch first-reading record and later supplements. [Evidence and limitations](docs/EVIDENCE.md) separates artifact counts, software checks and mathematical qualifications.

Next development: configurable lane specifications, source-linked exercise feedback, dependency-aware correction propagation, recoverable exports, and evaluations of continuation fidelity. [Funding use and milestones](docs/FUNDING_USE.md) gives a concrete plan. This is a newly public project; no external adoption, download volume, peer-review validation or grant approval is claimed.

## Contributing and licenses

See [CONTRIBUTING.md](CONTRIBUTING.md) for reproducible bug reports, source-aware mathematical corrections and small reviewable contributions. Do not upload private PDFs, credentials, automation memory or operational state.

Original software is [MIT licensed](LICENSE). Original released prose is [CC BY 4.0](LICENSE-CONTENT.md) to the extent the maintainer holds the relevant rights. Textbooks and third-party quotations are excluded from those grants; see [third-party notices](THIRD_PARTY_NOTICES.md). Codex assisted drafting and coding; the maintainer directs the project. Historical proof-status labels retain their scope, and publication adds no mathematical certification.
