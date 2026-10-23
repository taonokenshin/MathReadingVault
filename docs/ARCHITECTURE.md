# Architecture: a small control plane around substantial mathematics

The learner defines a total objective: a book or topic, desired rigor, source boundaries and what useful understanding should look like. The agent turns that objective into mathematical routes, bounded sessions and exact continuations. Deterministic code owns operational decisions; mathematical reasoning remains in the notes.

## Layers

1. **Intent and mathematical route.** The learner chooses the project. The agent plans near-term dependencies and a main question, with adjacent candidates if work finishes early. Different books and unrelated mathematical questions remain separate reading units.
2. **Control plane.** One JSON decision authorizes work or exits. Directory locks bind the current task, batch and occurrence. Heartbeat silence and an absolute lease independently bound failure. Fixed batches require manual reactivation after a confirmed terminal pause.
3. **Mathematical record.** Notes connect definitions, statements, proof steps, examples, cited inputs and explicit gaps. A run record states what actually changed and leaves exact source/input/lemma pointers.
4. **Source and transport tools.** Small PDF windows support precise local source comparison. Markdown checks catch selected transport problems; source hashes and public manifests make file identity inspectable.

## Recovery and honesty

An expired owner cannot use a new heartbeat to revive an absolute lease. Recovery releases stale ownership without pretending that mathematical work has finished. The next authorized session resumes the same uncounted occurrence from its durable continuation. The explicit administrative-credit path requires separate user authorization and keeps interruption history; it is not a blanket rule that every timeout counts as successful work.

Elapsed-time checks cannot measure thought or correctness. The reading protocol targets about 50 minutes of direct mathematical attention in a roughly 55–60 minute main session; file maintenance and waiting are excluded. These are operating goals, not evidence of measured attention. A true blocker can end an uncounted session.

The controller requests a pause; an external scheduler adapter performs it and confirms the paused configuration. The public extraction includes no account integration or scheduler registration. Historical named lane mappings and migration behavior remain explicit technical debt.

## Demonstrated checks and limits

The copied 41 controller tests passed locally on 23 October 2026. Tests use temporary roots and include ownership replacement, twelve-session terminal behavior, elapsed-time contracts, stale recovery, pause retries and idempotent user-authorized credit. The synthetic demo exercises activation, heartbeat, a competing claim and noncounted abort. See tools/verification_results.json.

The code is local coordination in a trusted account, not a hostile-process security boundary or a formal concurrent database. Runtime and lock-owner files are not a single multi-file transaction. The source cache is keyed by metadata, not authenticated content. No mathematical proof audit, learning-outcome study, model comparison or cross-platform validation was performed for publication.
