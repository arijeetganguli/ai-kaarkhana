---
id: architecture-review
title: "Architecture Review"
category: architecture
skills: [architecture-reviewer]
---

# Architecture Review

## Problem it solves

Designs are accepted without examining trade-offs, failure modes or alternatives.

## When to use

New services, module boundaries, integrations or major changes.

## Required context

- Design description.
- Drivers and constraints.
- Existing ADRs.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- Assessment per quality attribute.
- Decisions with alternatives.
- Risks and experiments.

## Validation steps

- [ ] Recommendations link to drivers.
- [ ] Alternatives are realistic for your team.
- [ ] Decisions are recorded in ADRs.

## Related skills

- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
