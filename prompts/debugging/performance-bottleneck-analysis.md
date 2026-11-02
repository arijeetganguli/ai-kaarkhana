---
id: performance-bottleneck-analysis
title: "Performance Bottleneck Analysis"
category: debugging
skills: [performance-analyst]
---

# Performance Bottleneck Analysis

## Problem it solves

Performance work starts with guesses rather than measurements.

## When to use

Latency, throughput, memory or cost does not meet a target.

## Required context

- Metric and target.
- Profile, trace or query plan.
- Load profile and data volumes.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Find the performance bottleneck from evidence.

Metric and target: [E.G. P95 LATENCY < 300 MS AT 50 RPS]
Current measurement and method: [NUMBERS AND HOW MEASURED]
Evidence: [PROFILE / TRACE / EXPLAIN PLAN / SLOW QUERY LOG]
Code: [CODE]

1. Say where time or resources go according to the evidence only.
2. Identify the probable cause class (N+1 queries, missing index, unbounded result set, synchronous remote calls in a loop, repeated serialisation, lock contention, allocation, missing cache) and quote the evidence.
3. Give ranked options with the expected effect (qualitative unless measured), trade-offs and correctness risks.
4. Define the verification: same measurement and load before and after. Do not invent numbers.
5. Propose a guard against regression (benchmark, query count test, alert).
```

## Expected AI output

- Bottleneck with evidence.
- Ranked options.
- Verification and guard.

## Validation steps

- [ ] Baseline exists.
- [ ] After the change, re-measure with the same method.
- [ ] Correctness tests still pass.

## Related skills

- [Performance Analyst](../../skills/performance-analyst/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
