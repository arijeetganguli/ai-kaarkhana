---
description: "Database Schema Review: Schema changes cause data integrity problems, downtime or slow queries."
---
Review this database change.

Current schema: [DDL]
Proposed change: [DDL OR MIGRATION]
Access patterns: [MAIN QUERIES]
Volumes: [ROW COUNTS, GROWTH]
Deployment: [ROLLING? ZERO DOWNTIME? DB ENGINE AND VERSION]

Assess: invariants and where each is enforced (constraint versus application only); data types (money, time with zone, identifiers); indexes against the access patterns, redundant indexes and write cost; transaction boundaries and concurrency risks (lost updates, write skew, deadlocks); migration safety (locks, table rewrites, defaults, batched backfills) and compatibility with the application version before and after deploy.
Provide an expand-and-contract migration sequence with verification and rollback for each step, and tests to run (constraint tests, migration on production-like data, rollback rehearsal). Mention engine-specific behaviour only if you are certain of the engine and version given; otherwise say it must be checked in the documentation.

---
Generated from [prompts/architecture/database-schema-review.md](../../prompts/architecture/database-schema-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
