# A source-grounded portfolio of the other mathematical study lanes

Evidence review and on-disk inventory snapshot: **2026-10-23T17:29:24.153925+08:00**. This is an editorial inventory of durable local records, not a new mathematical audit or a report of externally validated research. No reading controller was claimed and no live reading state, automation, lock, or source PDF was changed. The public [case index](../case-studies/other-lanes/INDEX.md) and [provenance manifest](../case-studies/other-lanes/PROVENANCE.json) supply selected source basenames, hashes, and excerpt ranges.

## What the project contributes

MathReadingVault studies how a learner-directed, AI-assisted mathematical reading project can accumulate useful reasoning over many bounded sessions. Its educational output is more than summaries: definitions are connected to their purpose, proofs to their hypotheses, calculations to their error bounds, and failed approaches to counterexamples. Persistent continuation markers let a later session resume one precise mathematical question. Separate first-pass, reviewed, cited, conditional, attempted, and source-caveat labels prevent an attractive explanation from silently becoming a stronger claim.

These are reusable learning and research-support practices. A researcher or graduate student can look up an earlier dependency, inspect why an attempted inference failed, and find the next local question without rereading an entire conversation. The records also provide realistic material for evaluating long-running mathematical assistants: recovery after interruption, preservation of scope, correction of earlier errors, and honest handling of work that remains open. This inventory establishes that artifacts exist; it does not establish mathematical novelty, peer-review acceptance, teaching effectiveness, or formal proof verification.

## Inventory conventions

Counts below are top-level Markdown files in each book's `deep_reading/` and `runs/`, excluding `README.md`. They count files on disk, including drafts, superseded records, historical maintenance logs, and paired-book pointer logs. They are **not** counts of theorems, solved exercises, unique sessions, accepted occurrences, or independently checked results. The exact snapshot time is given above. The public case manifest preserves the totals and convention. New 23 October work was in progress while this editorial inventory was prepared; a newly appearing note or log is not treated as an accepted result.

| Study lane | Books represented | Mathematical-note files | Run-record files | Evidence boundary |
|---|---|---:|---:|---|
| Apostol foundations and analytic number theory | *Introduction to Analytic Number Theory*; *Mathematical Analysis* | 160 | 402 | Mature, selective pass-2 support; ordinary work maintenance-gated |
| Stein–Shakarchi analysis | *Fourier Analysis*; *Complex Analysis* | 643 | 336 | Complex Analysis is the current mathematical continuation; Fourier remains a separate prior record |
| Cohen arithmetic | *Number Theory, Volume I* | 348 | 62 | First pass in Chapter 8; Volume II remains gated |
| Dieudonné analysis | *Infinitesimal Calculus* | 725 | 392 | Current Chapter XV reader extension; exact data and domain licenses matter |
| Serre finite groups | *Finite Groups: An Introduction* | 403 | 60 | Scoped first-pass coverage with explicit gaps; Chapter 8 reader extension remains active |
| Lang algebra | *Algebra* | 33 | 129 | Local Chapter XVII §7 reader problems; no whole-book completion claim |
| Brualdi combinatorics | *Introductory Combinatorics* | 87 | 95 | Foundation stage in §2.5; later books remain gated |

## Apostol: connecting analysis hypotheses to number-theoretic tools

Public cases: [APOSTOL-N1](../case-studies/other-lanes/apostol-01-partition-mechanisms.md) | [APOSTOL-N2](../case-studies/other-lanes/apostol-02-perron-interchange-boundary.md) | [APOSTOL-R1](../case-studies/other-lanes/apostol-run-history.md).

The state and July termination audit describe a selective pass-2 archive, rather than a full solution manual for both books. Twenty-six named historical hard-review packets are recorded as resolved and no live hard packet remains in that queue; this is the project's own historical assessment. The current gate permits reopening only for a concrete dependency, counterexample risk, or source/formula problem. *Mathematical Analysis* supplies named support instead of launching a second uncontrolled reading line.

The public examples should show the distinction between three mechanisms behind partition identities—finite roots-of-unity filtering, infinite-product identities, and Poisson/theta transformation—and the reason a Perron integral must first be truncated before sum–integral interchange. The latter makes the failure of full-line absolute integrability explicit, then explains the separate tail estimate. These examples teach transfer of hypotheses across books and avoidance of invalid formal manipulations.

Boundary: the historical queue's closure does not prove that every exercise in either book was independently reconstructed. The durable termination record retains a Franklin-reconstruction qualification and scope-external provenance. Later Apostol-folder run files often contain the shared Stein lane's canonical record and must not be advertised as new Apostol mathematics.

## Stein–Shakarchi: local evidence, global conclusions, and normalization

Public cases: [STEIN-N1](../case-studies/other-lanes/stein-01-energy-and-global-coordinate-error.md) | [STEIN-N2](../case-studies/other-lanes/stein-02-affine-monodromy-order.md) | [STEIN-R1](../case-studies/other-lanes/stein-run-history.md).

The last sealed state inspected is the 15 October Complex Analysis review of specified Jensen, growth, product, Weierstrass, Gamma, Beta, and hypergeometric subranges. Its next saved objective is the Chapter 6 theta–Mellin/zeta continuation interface. The same archive explicitly keeps Stein's meromorphic completed-zeta convention separate from the common entire xi convention. Fourier's mathematical `last_run` remains 4 October, despite later paired pointer files. Current in-progress 23 October drafts are not counted as completed work here.

Two project-authored reader notes make strong case studies. One separates energy rigidity and sharp inner-disk covering from global coordinate closeness, using a counterexample family. The other shows why the order of affine monodromy operations cannot be recovered from the individual root winding counts alone, and why an analytic inverse's cover need not be universal. Both teach the precise transition from a local calculation to a global assertion.

Boundary: the state reports 23 primary review packets, with 21 reviewed and 2 still pass-1, but qualifications are attached to actual subranges. General continuous Jordan theory, unrestricted Dirichlet existence, arbitrary cubic-period existence, specified Fourier support gates, and later source pages remain held. These numbers are recorded project labels, not an independent audit performed for this publication.

## Cohen: turning arithmetic structure into a certified computation

Public cases: [COHEN-N1](../case-studies/other-lanes/cohen-01-heegner-certification.md) | [COHEN-N2](../case-studies/other-lanes/cohen-02-fixed-divisor-caveat.md) | [COHEN-R1](../case-studies/other-lanes/cohen-run-history.md).

The 15 October state stops at actual Chapter 8 Exercise 19, printed page 611 / source PDF page 636. The saved next question is Exercise 20(a), with the elementary congruence restrictions, explicit witness search, analytic nonvanishing, descent, and Heegner discovery deliberately separated. Volume I's first-pass gate is still false, so Volume II is not an active reading achievement. An in-progress 23 October Exercise 21 note is not used to advance this sealed frontier.

The selected cases concern the difference between an approximate Heegner computation and an exact rational-point certificate, and between a square class and a fixed integer divisor representative in a quartic covering. Their value is methodological: denominator bounds, parameterization normalization, local hypotheses, and the direction of a variable substitution can determine whether a numerical result supports an exact conclusion. The Heegner note also withdraws an earlier reader misreading rather than converting it into a spurious textbook erratum.

Boundary: deep inputs such as modularity, Gross–Zagier, Mazur, standard Tate classifications, and relevant height theorems are cited rather than claimed as newly proved. BSD/Sha-dependent estimates, the fixed negative-32 Heegner interface, the large-minimum enumeration problem, and other recorded computational gaps remain explicit. Local source caveats are not presented as official publisher errata.

## Dieudonné: correlation-aware error bounds and genuine admissible data

Public cases: [DIEUDONNE-N1](../case-studies/other-lanes/dieudonne-01-correlated-rounding-penalty.md) | [DIEUDONNE-N2](../case-studies/other-lanes/dieudonne-02-boundary-input-interior-output.md) | [DIEUDONNE-R1](../case-studies/other-lanes/dieudonne-run-history.md).

The 23 October 15:07 run is explicitly completed and records an accepted 11/12 continuation receipt. It studies the current Chapter XV Euler–Maclaurin/oscillatory remainder extension: joint four-real-dimensional Gram bounds, a complete two-root L1 calculation, signed boundary terms, and a second periodic discrepancy. The saved next question is a common normalized support-gap calculation; its analytic template is recorded, while numerical center/gradient/remainder payment and a new uniform gain remain unapplied.

The selected older reader notes explain two portable lessons: separate rounding of correlated quantities can introduce a first-order amplitude penalty, and an input on a product of boundary circles can map to an interior output point when the actual real derivative has full rank. This is useful training in rigorous numerical reasoning because a narrow numerical box, an admissible parameter set, and a correct common-data comparison are distinct objects.

Boundary: all improvements are conditional on named prior anchors, domains, root licenses, and complete transport fees. They are reader-level pass-1 extensions, not global textbook results. The numerical magnitude of an interval improvement is not advertised as general-purpose accuracy or scientific novelty. The original imaginary enclosure, old problem gaps, and book/source gates remain in force.

## Serre: integral structure cannot be recovered from dimensions alone

Public cases: [SERRE-N1](../case-studies/other-lanes/serre-01-equal-index-different-quotients.md) | [SERRE-N2](../case-studies/other-lanes/serre-02-raw-joint-bounded-scope.md) | [SERRE-R1](../case-studies/other-lanes/serre-run-history.md).

The book state records a scoped first pass with explicit open gaps. Its latest sealed 15 October continuation concerns a fixed Chapter 8 integral/tensor problem: recorded nonlinear Tor generator formulas and two cyclic bar packets are reused, while residual Bockstein ranks, elementary divisors, and actual exponents remain open. The archive's project-level first-pass coverage through Chapter 10 does not mean every printed assertion or exercise was proved literally as printed.

The compact equal-index counterexample is especially suitable for public teaching: two quotients have the same order and the same index but different mod-three dimensions because a carry term was lost. A second note explains a raw joint-input argument, preserving the actual marked ambient group and a bounded h=1,2 scope instead of replacing an embedding by an abstract Smith type. These cases illustrate how a plausible rank/order check can miss the information the proof actually needs.

Boundary: rationalized structure, mod-three splittings, and integral complexes are kept separate. A quotient of the correct dimension is not automatically a genuine syzygy or Bockstein subcomplex. Historical source caveats, corrected exercise formulations, and cited background remain visible. No public-open-problem or novel-research claim is inferred from an internal `open` or `gap` label.

## Lang: explicit modules, two actions, and noncommuting specialization

Public cases: [LANG-N1](../case-studies/other-lanes/lang-01-colon-specialization.md) | [LANG-N2](../case-studies/other-lanes/lang-02-action-dependent-tensor-sections.md) | [LANG-R1](../case-studies/other-lanes/lang-run-history.md).

The 5 October saved state concerns local reader-generated problems beside Chapter XVII §7. The next unattempted unit is a three-generator fractional ideal over k[t^5,t^9]; it is not permission to jump to a new chapter or to restart a completed two-generator example. The two selected notes derive actual relation modules, tensor kernels, colon ideals, and the two endomorphism-ring actions for explicit nonmonomial fractional ideals.

Their pedagogical theme is a sequence of distinctions: equal length versus isomorphism; a perfect pairing versus freeness; abstract specialization versus recomputing a colon ideal in the special fiber; and a section for one module action versus a section for the other. Parameter and characteristic branches make the limits of a tempting generalization inspectable.

Boundary: these are recorded first-pass reader arguments with bounded computational guards and source support at one already-read page. They do not establish a general classification, whole-chapter closure, or completion of Lang's book. Original source theorem and hard-packet grades are not automatically upgraded by the reader examples. The selected log seals mathematics and validation but defers official counting to the controller; this portfolio does not infer a missing receipt.

## Brualdi: elementary counting as a laboratory for assumptions

Public cases: [BRUALDI-N1](../case-studies/other-lanes/brualdi-01-negative-association-boundaries.md) | [BRUALDI-N2](../case-studies/other-lanes/brualdi-02-counting-fibers-and-boxes.md) | [BRUALDI-R1](../case-studies/other-lanes/brualdi-run-history.md).

The 5 October completed run records a selective review in §2.5 and a confirmed terminal 12/12 self-pause. The saved new-source frontier is strictly below the earlier source page's y=810 boundary, not a guessed next exercise number. Stage 1 is unfinished. Beck–Robins and Stanley therefore remain preparation/gated books, not completed or currently advanced study lanes.

The selected notes connect fixed-size weighted subsets to inclusion couplings and negative association, and connect quantity vectors to fibers, finite boxes, reciprocity, and actual facet conditions. The examples repeatedly test whether forgetting labels changes the probability law, whether pairwise correlation suffices for a block statement, and whether a plausible unique-interior-point criterion is strong enough. Short reader-authored excerpts should begin after the textbook's elementary source example, retaining the provenance and status preface.

Boundary: only named subranges receive the recorded reviewed label. General weighted/capped spectra, old word-spectrum questions, some real-rootedness/unimodality questions, an earlier source-pending item, and a geometry literature-only hard item remain open or deferred. Bounded enumerations check examples and do not replace the general written arguments.

## How to publish these examples responsibly

The [public case index](../case-studies/other-lanes/INDEX.md) contains two short project-authored mathematical excerpts and one English educational run history per lane. The historical excerpts retain their original Chinese/English language and have detailed English prefaces. Do not publish scanned textbook pages, long copied textbook statements, or a systematic complete solution manual. Keep original mathematical attribution and the recorded qualification next to the excerpt. The selected file is a candidate, not a blanket rights clearance for all linked dependencies.

This curated release excludes private machine paths, unrelated personal information, live state and ownership data, private automation memory, and source PDFs. References to omitted dependent notes or certificates are rendered as provenance descriptions rather than working links. The release is a collection of educational case studies, not a standalone complete proof package. A documented example can be valuable even when its current endpoint is an honest unresolved local gap.
