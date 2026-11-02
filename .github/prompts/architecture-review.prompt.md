---
description: "Architecture Review: Designs are accepted without examining trade-offs, failure modes or alternatives."
---
Review this design as an architecture reviewer.

Design: [DESIGN / DIAGRAM DESCRIPTION]
Drivers and constraints (availability, latency, compliance, team size, budget): [DRIVERS]
Existing decisions: [ADRS]

1. Restate the problem and drivers; flag any you think are missing.
2. Identify components, responsibilities, data ownership and dependencies.
3. Assess against quality attributes: modularity and coupling, failure modes and resilience, scalability and bottlenecks, security boundaries, observability and operability, cost, and team fit.
4. For each major decision give one realistic alternative and the trade-offs.
5. Look for: shared databases between services, synchronous chains, missing timeouts, unbounded queues, single points of failure, chatty calls, unclear ownership.
6. List risks and the cheapest experiment or spike that would reduce each.
Tie every recommendation to a stated driver. Do not recommend technology for its own sake.

---
Generated from [prompts/architecture/architecture-review.md](../../prompts/architecture/architecture-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
