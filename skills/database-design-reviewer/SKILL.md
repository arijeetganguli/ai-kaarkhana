---
name: database-design-reviewer
description: "Reviews schemas, queries and migrations for integrity, normalisation, indexing, transactional correctness, backwards-compatible rollout and rollback. Use when designing tables or changing schema."
license: MIT
metadata:
  activity: architecture
  difficulty: advanced
  frameworks: "SQL, any relational database"
  version: "1.0"
---

# Database Design Reviewer

## Purpose

Make data changes safe: correct constraints, efficient access paths, transaction boundaries and migrations that can be deployed without downtime or data loss.

## When to invoke

- Creating or altering tables, indexes or constraints.
- Writing or reviewing queries on large tables or hot paths.
- Planning a data migration or backfill.

## Required input

- Current schema and proposed change.
- Main access patterns and data volumes.
- Deployment model: rolling deploys, zero downtime requirement, rollback expectations.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Model the entities, relationships and invariants. Check each invariant is enforced by a constraint (key, unique, foreign key, check, not null), not only by application code.
2. Check data types: money, time with zone, identifiers, text lengths, enums.
3. Review access patterns against indexes. Identify missing and redundant indexes and the cost of writes.
4. Check transaction boundaries: which operations must be atomic, isolation needs, lost update and write skew risks, locking.
5. Review migrations for safety: expand and contract steps, locks on large tables, default values, backfills in batches, compatibility with old and new application versions.
6. Define the rollback story for each step, including data written by the new version.
7. Define tests: migration on production-like data, constraint tests, query plans, rollback rehearsal.

## Expected output

- Findings table with severity and recommendation.
- Proposed constraints, indexes and migration sequence.
- Transaction and concurrency notes.
- Rollback and verification plan.

## Validation checklist

- [ ] Each invariant has a stated enforcement point.
- [ ] Migration is compatible with the application version before and after deploy.
- [ ] Large table operations account for locks and duration.
- [ ] Rollback is defined and does not lose data.
- [ ] Indexes are justified by access patterns.

## Example usage

Input:

> Add `NOT NULL` column `cancel_reason` to a 40 million row `orders` table.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Risk: table rewrite and lock; old application version cannot insert rows.
Plan: 1) add nullable column; 2) deploy code that writes it; 3) backfill in batches; 4) add constraint after verification. Rollback: steps 1-3 are reversible by ignoring the column.
```

## Sample prompts

```text
Act as the Database Design Reviewer. Review the schema change below for constraints, types, indexes, transaction boundaries and migration safety under rolling deployment. Give an expand-and-contract migration sequence with rollback for each step. Schema: [SCHEMA]. Change: [DDL]. Access patterns: [QUERIES]. Volumes: [VOLUMES]
```

## Common mistakes

- Enforcing invariants only in the application.
- Adding a NOT NULL column with default to a huge table in one step.
- Adding indexes without checking write cost.
- Testing migrations on empty databases only.

## Related skills

- [Architecture Reviewer](../architecture-reviewer/SKILL.md)
- [Integration Test Engineer](../integration-test-engineer/SKILL.md)
- [Performance Analyst](../performance-analyst/SKILL.md)

## Related resources

Handbook:

- [Chapter 8: Architecture and Design](../../handbook/08_architecture_and_design/README.md)

Prompts:

- [Database Schema Review](../../prompts/architecture/database-schema-review.md)
- [Performance Bottleneck Analysis](../../prompts/debugging/performance-bottleneck-analysis.md)

Workflows:

- [Change a database schema](../../workflows/05_database_schema_change.md)
- [Develop a data pipeline](../../workflows/06_data_pipeline.md)

Examples:

- [examples/broken_code_lab/05_missing_transaction_rollback/CHALLENGE.md](../../examples/broken_code_lab/05_missing_transaction_rollback/CHALLENGE.md)
