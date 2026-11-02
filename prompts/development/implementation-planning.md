---
id: implementation-planning
title: "Implementation Planning"
category: development
skills: [implementation-planner, repository-explorer]
---

# Implementation Planning

## Problem it solves

Large AI edits are hard to review and break things because nothing was planned in small steps.

## When to use

After requirements and repository context are clear and before generating code.

## Required context

- Acceptance criteria and scenario matrix.
- Repository map.
- Constraints such as compatibility or rollout.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- Goal and non-goals.
- Ordered slices with test, change, files, command and revert.
- Risk register.
- Decisions for humans.

## Validation steps

- [ ] Each slice builds and passes tests on its own.
- [ ] Every listed file exists.
- [ ] Risky steps have a rollback.
- [ ] You agree with the order before any code is generated.

## Related skills

- [Implementation Planner](../../skills/implementation-planner/SKILL.md)
- [Repository Explorer](../../skills/repository-explorer/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
