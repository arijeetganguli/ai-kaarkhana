---
description: "Performance Review: A change introduces performance regressions that are invisible in small tests."
---
Review this change for performance risks. Do not optimise without evidence; flag and propose measurements.

Diff: [DIFF]
Volumes and rates: [DATA SIZES, REQUESTS PER SECOND]
Targets: [LATENCY, MEMORY, COST]

Identify, with file and line: queries in loops (N+1), unbounded queries or collections, missing pagination, repeated work inside loops, synchronous remote calls in series, blocking calls on async paths, large payload serialisation, quadratic algorithms on user-sized input, locks held across I/O, caches without bounds or invalidation.
For each: the complexity or call count as a function of input size, the risk level given the volumes above, and the cheapest measurement that would confirm it. Suggest a fix only where the risk is high and the fix is simple. Do not give invented timings.

---
Generated from [prompts/code_review/performance-review.md](../../prompts/code_review/performance-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
