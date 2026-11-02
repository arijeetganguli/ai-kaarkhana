---
id: database-schema-review
title: "Database Schema Review"
category: architecture
skills: [database-design-reviewer]
---

# Database Schema Review

## Problem it solves

Schema changes cause data integrity problems, downtime or slow queries.

## When to use

Creating or altering tables, indexes, constraints or running migrations.

## Required context

- Current and proposed schema.
- Queries and access patterns.
- Volumes and deployment model.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review this database change.

Current schema: [DDL]
Proposed change: [DDL OR MIGRATION]
Access patterns: [MAIN QUERIES]
Volumes: [ROW COUNTS, GROWTH]
Deployment: [ROLLING? ZERO DOWNTIME? DB ENGINE AND VERSION]

Assess: invariants and where each is enforced (constraint versus application only); data types (money, time with zone, identifiers); indexes against the access patterns, redundant indexes and write cost; transaction boundaries and concurrency risks (lost updates, write skew, deadlocks); migration safety (locks, table rewrites, defaults, batched backfills) and compatibility with the application version before and after deploy.
Provide an expand-and-contract migration sequence with verification and rollback for each step, and tests to run (constraint tests, migration on production-like data, rollback rehearsal). Mention engine-specific behaviour only if you are certain of the engine and version given; otherwise say it must be checked in the documentation.
```

## Expected AI output

- Findings.
- Migration sequence with rollback.
- Verification tests.

## Validation steps

- [ ] Rehearse on a production-like copy.
- [ ] Check engine behaviour in vendor docs.
- [ ] Rollback tested.

## Related skills

- [Database Design Reviewer](../../skills/database-design-reviewer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
