# Architecture prompts

Review designs and decisions: architecture, ADRs, APIs, schemas, resilience and threat models.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [Architecture Review](architecture-review.md) | Designs are accepted without examining trade-offs, failure modes or alternatives. | [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md) |
| [Architecture Decision Record Drafting](adr-drafting.md) | Architectural decisions are lost, and future engineers do not know why. | [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md), [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |
| [API Design Review](api-design-review.md) | APIs are designed from the implementation outward and break consumers over time. | [api-contract-reviewer](../../skills/api-contract-reviewer/SKILL.md) |
| [Database Schema Review](database-schema-review.md) | Schema changes cause data integrity problems, downtime or slow queries. | [database-design-reviewer](../../skills/database-design-reviewer/SKILL.md) |
| [Resilience Review](resilience-review.md) | Services fail badly when dependencies are slow or down. | [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md), [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md) |
| [Threat Modelling](threat-modelling.md) | Security design is ad hoc and threats are found after release. | [security-reviewer](../../skills/security-reviewer/SKILL.md), [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md) |

Related handbook chapter: [Chapter 8: Architecture and Design](../../handbook/08_architecture_and_design/README.md)

Back to the [prompt library](../README.md).
