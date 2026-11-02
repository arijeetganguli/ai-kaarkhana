---
id: performance-review
title: "Performance Review"
category: code_review
skills: [performance-analyst, code-quality-reviewer]
---

# Performance Review

## Problem it solves

A change introduces performance regressions that are invisible in small tests.

## When to use

Reviewing code on hot paths or that adds queries, loops, remote calls or large allocations.

## Required context

- Diff.
- Typical data volumes and request rates.
- Performance targets.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review this change for performance risks. Do not optimise without evidence; flag and propose measurements.

Diff: [DIFF]
Volumes and rates: [DATA SIZES, REQUESTS PER SECOND]
Targets: [LATENCY, MEMORY, COST]

Identify, with file and line: queries in loops (N+1), unbounded queries or collections, missing pagination, repeated work inside loops, synchronous remote calls in series, blocking calls on async paths, large payload serialisation, quadratic algorithms on user-sized input, locks held across I/O, caches without bounds or invalidation.
For each: the complexity or call count as a function of input size, the risk level given the volumes above, and the cheapest measurement that would confirm it. Suggest a fix only where the risk is high and the fix is simple. Do not give invented timings.
```

## Expected AI output

- Risks with complexity and call counts.
- Measurements to take.
- Simple fixes.

## Validation steps

- [ ] Measure the flagged paths.
- [ ] Check for query count tests.
- [ ] Correctness tests unchanged.

## Related skills

- [Performance Analyst](../../skills/performance-analyst/SKILL.md)
- [Code Quality Reviewer](../../skills/code-quality-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
