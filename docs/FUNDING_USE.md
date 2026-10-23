# Development plan and use of support

MathReadingVault develops open tools and evidence-linked materials for sustained mathematical learning and research preparation. The public project brings a working personal workflow into a reusable, documented form. Its first release has substantial existing material and a small tested control plane; external adoption and educational effectiveness still need evaluation.

## Concrete work already represented

The 20 October English Marcus/Neukirch snapshot contains 1,152 mathematical articles and 1,124 normalized study records. The 23 October inventory of nine other book folders contains 2,399 mathematical-note files and 1,476 run-record files. These dated inventories include drafts, superseded records and paired-book pointers and must not be added up as distinct mathematical results. The repository publishes representative cases from those other lanes and the complete privacy-filtered English reading layer separately.

The original main-session design uses a fixed batch of twelve qualified occurrences, normally one start slot per hour, followed by pause and explicit manual reactivation. About 50 minutes of direct mathematics per occurrence gives a planned ten hours of mathematical work per full batch, within roughly eleven to twelve elapsed session-hours. This is a planning target, not proof that every recorded minute was active thought. Recovery and quota constraints can spread a batch over a longer calendar period.

Capacity planning is based on observed allowance consumption, then adjusted locally. A separate read-only monitor historically used a low-watermark/high-watermark rule to identify refreshes; it never launched reading work or redeemed reset credits. Subscription percentages are not API token counts or a per-task cost measurement. The public release contains no account-reading or quota-control integration.

## Development milestones

| Stage | Deliverable | Evidence of completion |
| --- | --- | --- |
| Portable core | Replace fixed lane mappings with validated user configuration and a scheduler-adapter boundary | Isolated fixtures, schema checks, backward-compatibility tests, documented manual rearm/pause flow |
| Source-linked learning | Generate small diagnostic exercise sets with progressive hints and explicit answer/source keys | Original numbering preserved; cited inputs and corrections surfaced; learner feedback changes the route |
| Correction propagation | Record which later arguments rely on a corrected assumption or normalization | Small reproducible dependency examples; stale qualifications flagged without silently rewriting history |
| Recovery and handoff evaluation | Test exact continuation after simulated timeout, context loss and replacement ownership | Fixed disclosed cases and failure criteria; no hidden benchmark contamination or invented success rate |
| Public study exports | Maintain readable chapter-order releases with provenance and privacy checks | Reproducible manifests, zero unresolved local file targets, documented omissions and reviewer feedback |

## How model/API support would be used

Support would fund development and maintenance of the open system: reproducing reported continuation failures, reviewing controller/configuration changes, improving source-linked feedback, validating public exports, and building openly inspectable evaluation cases. A bounded pilot can also test the mathematical-assistant pipeline itself on rights-cleared or reader-authored tasks, retaining failures and qualifications.

A proposed pilot allocation is 40% reproducible evaluation and failure analysis, 30% software tests/refactoring and pull-request review, 20% source-linked educational interfaces, and 10% documentation/translation/release work. These are future budget fractions, not historical measured spending. No API amount, dollar cost per proof or token count is claimed without usage exports and an explicit model/pricing basis.

The next evaluation should record software version, task type, model settings where observable, wall time, API token usage if actually metered, successful continuation, correction preservation and unresolved gaps. Publish aggregate results and failure cases; keep credentials, account IDs, private source PDFs and learner data private. API credits would not authorize scanning unrelated repositories or extend access beyond the maintainer's project.

## Scope and accountability

This is an early public educational/research-support project, not an established dependency with claimed large download counts. The maintainer can present the existing artifacts, ongoing maintenance and potential ecosystem value honestly. Benefits, eligibility, award amounts and acceptance remain decisions of the funding program. The project has no grant approval or affiliation with OpenAI or the textbook publishers.
