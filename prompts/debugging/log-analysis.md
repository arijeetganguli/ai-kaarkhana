---
id: log-analysis
title: "Log Analysis"
category: debugging
skills: [debugging-specialist]
---

# Log Analysis

## Problem it solves

Logs are voluminous and patterns are missed or hallucinated.

## When to use

Investigating errors, latency or behaviour from log excerpts.

## Required context

- Sanitised log excerpts with timestamps.
- Format description.
- Question being asked.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Analyse these logs to answer one question.

Question: [E.G. WHY DID REQUESTS FAIL BETWEEN 10:02 AND 10:09?]
Log format: [FIELDS]
Logs (sanitised; no secrets or personal data):
[PASTE LOGS]

1. Group entries by error signature and show counts and first and last occurrence. Count only what is present in the excerpt, and say the excerpt may be incomplete.
2. Build a timeline of the key events and correlate by request or trace ID.
3. Identify the earliest anomaly and what changed immediately before it.
4. List patterns suggested by the data and what additional queries would confirm them. Provide the exact queries for [LOG SYSTEM].
5. Separate observations from hypotheses.
Do not extrapolate beyond the supplied lines.
```

## Expected AI output

- Grouped signatures with counts.
- Timeline.
- Hypotheses with confirming queries.

## Validation steps

- [ ] Re-count a signature yourself.
- [ ] Run the suggested queries on the full logs.
- [ ] Logs were sanitised.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
