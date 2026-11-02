---
name: architecture-reviewer
description: "Reviews designs and architectural changes against quality attributes: modularity, coupling, resilience, scalability, security, operability and cost, and records decisions as ADRs. Use for new components, service boundaries and significant changes."
license: MIT
metadata:
  activity: architecture
  difficulty: advanced
  frameworks: "any"
  version: "1.0"
---

# Architecture Reviewer

## Purpose

Expose trade-offs and risks in a design before it is built, and record the decision with its context so it can be revisited.

## When to invoke

- Designing a new service, module boundary, integration or data flow.
- A change crosses team or system boundaries.
- Reviewing an AI-generated design or architecture proposal.

## Required input

- Design document, diagram or proposed code structure.
- Quality attribute goals and constraints (availability, latency, compliance, team size, budget).
- Existing architecture and decisions (ADRs).

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. State the problem, drivers and constraints in your own words and confirm they match the design intent.
2. Identify the components, responsibilities, data ownership and dependencies. Draw or describe the flow.
3. Evaluate against quality attributes: modularity and coupling, failure modes and resilience, scalability and bottlenecks, security boundaries, observability, operability, cost.
4. Identify the main decisions and at least one realistic alternative for each, with trade-offs.
5. Look for common failure patterns: distributed monolith, shared database between services, chatty calls, missing timeouts, synchronous chains, unbounded queues, single points of failure.
6. Identify risks and the cheapest experiments or tests that would reduce them.
7. Draft ADRs for the significant decisions with status, context, decision and consequences.

## Expected output

- Design summary and assumptions.
- Quality attribute assessment with findings and severity.
- Decision list with alternatives and trade-offs.
- ADR drafts.
- Risks and validation experiments.

## Validation checklist

- [ ] Every recommendation ties to a stated driver or constraint.
- [ ] At least one alternative was considered per major decision.
- [ ] Failure modes and timeouts are addressed.
- [ ] Data ownership is explicit.
- [ ] No technology was recommended without a reason.

## Example usage

Input:

> Proposal: split `orders` and `inventory` services, both writing to the same database.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Major: shared database couples releases and schemas; services cannot evolve independently.
Alternatives: single module with clear boundary now (cheaper), or split with API/event ownership of inventory data.
ADR-014 draft: Keep one deployable with enforced module boundaries until team size or release cadence requires a split.
```

## Sample prompts

```text
Act as the Architecture Reviewer. Review the design below against these drivers: [DRIVERS]. Assess modularity, failure modes, scalability, security, operability and cost. For each major decision give one alternative and the trade-offs, then draft ADRs. Design: [DESIGN]. Existing ADRs: [ADRS]
```

## Common mistakes

- Recommending fashionable patterns without a driver.
- Evaluating only the happy path and not failures.
- Ignoring team size and operational capability.
- Not recording the decision.

## Related skills

- [API Contract Reviewer](../api-contract-reviewer/SKILL.md)
- [Database Design Reviewer](../database-design-reviewer/SKILL.md)
- [Security Reviewer](../security-reviewer/SKILL.md)
- [Implementation Planner](../implementation-planner/SKILL.md)

## Related resources

Handbook:

- [Chapter 8: Architecture and Design](../../handbook/08_architecture_and_design/README.md)

Prompts:

- [Architecture Review](../../prompts/architecture/architecture-review.md)
- [Architecture Decision Record Drafting](../../prompts/architecture/adr-drafting.md)
- [Resilience Review](../../prompts/architecture/resilience-review.md)
- [Threat Modelling](../../prompts/architecture/threat-modelling.md)

Workflows:

- [Introduce a new API](../../workflows/04_new_api.md)
- [Change a database schema](../../workflows/05_database_schema_change.md)
- [Develop a data pipeline](../../workflows/06_data_pipeline.md)
