---
description: "Performance Bottleneck Analysis: Performance work starts with guesses rather than measurements."
---
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

---
Generated from [prompts/debugging/performance-bottleneck-analysis.md](../../prompts/debugging/performance-bottleneck-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
