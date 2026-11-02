---
description: "Resilience Review: Services fail badly when dependencies are slow or down."
---
Review resilience of this component.

Component and dependencies: [DESCRIPTION]
Code for the calls: [CODE]
Availability and latency goals: [GOALS]

For each dependency call report: timeout (connect and read) and what happens when it is missing; retry policy (limits, backoff with jitter, retry only idempotent operations); circuit breaking or load shedding; bulkheads (separate pools); fallback behaviour and whether stale data is acceptable; idempotency of handlers for at-least-once delivery; queue limits, dead-letter handling and poison messages; behaviour at startup and shutdown; observability of failures (metrics, logs, trace IDs).
Output a table: dependency | failure mode | current behaviour | risk | recommended behaviour | test to prove it (fault injection). Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/architecture/resilience-review.md](../../prompts/architecture/resilience-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
