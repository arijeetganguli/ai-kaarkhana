---
description: "Implementation Planning: Large AI edits are hard to review and break things because nothing was planned in small steps."
---
Create a test-first implementation plan. Do not write production code yet.

Specification and acceptance criteria:
[SPEC]

Scenario matrix:
[MATRIX]

Repository map:
[MAP]

Constraints:
[COMPATIBILITY, FEATURE FLAGS, DEADLINES]

Plan as small vertical slices. For each slice give: the failing test to write first (name and what it asserts), the minimal change, files and symbols touched (only files that exist in the map), the command that verifies it, and how it can be reverted.
Also list: goal and non-goals, risky steps (schema, public contract, concurrency, data migration) with validation and rollback, decisions that need a human, and any ADR to write.
If any step depends on an unanswered question, stop the plan at that step and ask.

---
Generated from [prompts/development/implementation-planning.md](../../prompts/development/implementation-planning.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
