---
id: resilience-review
title: "Resilience Review"
category: architecture
skills: [architecture-reviewer, defensive-programming-reviewer]
---

# Resilience Review

## Problem it solves

Services fail badly when dependencies are slow or down.

## When to use

Designing or reviewing code that calls remote services, queues or databases.

## Required context

- Dependency list.
- Call code.
- Availability goals.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review resilience of this component.

Component and dependencies: [DESCRIPTION]
Code for the calls: [CODE]
Availability and latency goals: [GOALS]

For each dependency call report: timeout (connect and read) and what happens when it is missing; retry policy (limits, backoff with jitter, retry only idempotent operations); circuit breaking or load shedding; bulkheads (separate pools); fallback behaviour and whether stale data is acceptable; idempotency of handlers for at-least-once delivery; queue limits, dead-letter handling and poison messages; behaviour at startup and shutdown; observability of failures (metrics, logs, trace IDs).
Output a table: dependency | failure mode | current behaviour | risk | recommended behaviour | test to prove it (fault injection). Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Failure mode table.
- Recommended behaviours.
- Fault injection tests.

## Validation steps

- [ ] Inject each fault in a test environment.
- [ ] Timeouts exist everywhere.
- [ ] Retries are bounded.

## Related skills

- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)
- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
