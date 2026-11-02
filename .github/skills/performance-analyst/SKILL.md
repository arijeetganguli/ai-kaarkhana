---
name: performance-analyst
description: "Analyses performance problems with a measure-first approach: defines the metric, finds the bottleneck from profiles, queries or traces, proposes targeted changes and verifies the improvement. Use for slow endpoints, jobs or queries."
license: MIT
metadata:
  activity: performance
  difficulty: advanced
  frameworks: "any"
  version: "1.0"
---

# Performance Analyst

## Purpose

Prevent speculative optimisation. Tie every change to a measured bottleneck and a before and after comparison.

## When to invoke

- A latency, throughput, memory or cost target is missed.
- A review raises a performance concern without evidence.
- A change adds loops, queries, serialisation or remote calls on a hot path.

## Required input

- The metric and target (for example p95 latency under 300 ms at 50 requests per second).
- Evidence: profile, trace, slow query log, benchmark or metrics.
- The code path and data volumes.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Define the symptom, metric, target and the load profile that reproduces it.
2. Establish a baseline measurement. If none exists, define how to take one before changing code.
3. Locate the bottleneck from evidence: where is time, memory or I/O spent.
4. Check typical causes: N+1 queries, missing indexes, unbounded result sets, synchronous remote calls in loops, repeated serialisation, lock contention, excessive allocation, missing caching with correct invalidation.
5. Propose the smallest change that addresses the measured bottleneck, with expected effect and trade-offs (complexity, staleness, memory).
6. Define the verification: same measurement, same load, compare to baseline.
7. Record regressions risks and add a guard (benchmark, query count test, alert) where practical.

## Expected output

- Symptom, metric, target and measurement method.
- Bottleneck analysis with evidence.
- Ranked options with trade-offs.
- Verification plan and before/after results (only if measured).

## Validation checklist

- [ ] A baseline exists or its collection is the first step.
- [ ] The bottleneck is supported by evidence.
- [ ] No numbers are estimated or invented.
- [ ] Trade-offs and correctness risks (cache invalidation, ordering) are stated.
- [ ] A guard against regression is proposed.

## Example usage

Input:

> Endpoint `/orders` is slow. Trace shows 1 query for orders plus 1 query per order for customer.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Bottleneck: N+1 on `customer`. Evidence: trace spans (1 + N queries).
Option A: join fetch (single query). Option B: batch load by ids. Choose A for page size 50.
Verify: same request at the same data volume, compare query count and p95. Guard: test asserting query count <= 2.
```

## Sample prompts

```text
Act as the Performance Analyst. Symptom: [SYMPTOM]. Metric and target: [TARGET]. Evidence: [PROFILE/TRACE/QUERY PLAN]. Identify the bottleneck from the evidence only, rank options with trade-offs, and give a verification plan. Do not invent measurements. Code: [CODE]
```

## Common mistakes

- Optimising before measuring.
- Adding a cache without an invalidation strategy.
- Reporting improvements that were estimated instead of measured.
- Benchmarking with unrepresentative data volumes.

## Related skills

- [Debugging Specialist](../debugging-specialist/SKILL.md)
- [Database Design Reviewer](../database-design-reviewer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 7: Code Quality](../../../handbook/07_code_quality/README.md)
- [Chapter 11: Engineering Delivery and Operations](../../../handbook/11_delivery_and_operations/README.md)

Prompts:

- [Performance Bottleneck Analysis](../../../prompts/debugging/performance-bottleneck-analysis.md)
- [Performance Review](../../../prompts/code_review/performance-review.md)

Workflows:

- [Handle a production incident](../../../workflows/08_production_incident.md)
- [Refactor an existing service](../../../workflows/03_service_refactoring.md)
