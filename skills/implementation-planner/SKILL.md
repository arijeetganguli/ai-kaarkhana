---
name: implementation-planner
description: "Produces a small-step, test-first implementation plan for a change, grounded in repository evidence and a scenario matrix. Use after requirements and repository context are clear, before generating code."
license: MIT
metadata:
  activity: planning
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Implementation Planner

## Purpose

Break a change into small, independently verifiable steps with tests, risks and rollback in mind, so that each AI-assisted edit is reviewable.

## When to invoke

- The requirement is specified and the repository has been explored.
- A change touches more than one file, module or layer.
- An AI agent is about to make multi-file edits.

## Required input

- Specification and acceptance criteria, with open questions resolved or flagged.
- Scenario matrix and repository map (see Edge Case Hunter and Repository Explorer).
- Constraints: backward compatibility, release timing, feature flags, data migration.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. State the goal, non-goals and the definition of done in terms of acceptance criteria.
2. List the files and symbols to change, each justified by the repository map.
3. Order the work as thin vertical slices. Each slice is the smallest behaviour that can be tested and merged.
4. For each slice, name the failing test first, then the minimal change, then the refactor.
5. Identify risky steps (schema, public API, concurrency, data migration) and how each will be validated or reverted.
6. Specify the commands that prove each slice: unit tests, integration tests, linters, contract checks.
7. List decisions needing approval and any ADR to write.
8. Stop and ask if a step depends on an unresolved question.

## Expected output

- Goal, non-goals, definition of done.
- Numbered slices: test to write, change to make, files touched, verification command.
- Risk register with mitigations and rollback approach.
- Decisions and questions awaiting a human.

## Validation checklist

- [ ] Each slice can be merged on its own without breaking the build.
- [ ] Every slice begins with a test.
- [ ] Every file in the plan appears in the repository map.
- [ ] Risky steps have a validation and a rollback.
- [ ] Plan contains no steps that depend on unanswered questions.

## Example usage

Input:

> Spec: add optional `reason` to order cancellation, store it, expose it in the API.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Slice 1: test `cancel_without_reason_still_works` (regression). No code change expected; run existing suite.
Slice 2: add nullable column `cancel_reason` (migration, backwards compatible). Verify: migration test against local DB.
Slice 3: test `cancel_stores_reason`, then service and repository change.
Slice 4: contract test for the API field. Rollback: the field is optional so older clients are unaffected.
```

## Sample prompts

```text
Using the Implementation Planner skill, produce a test-first plan of small slices for this change. For each slice give the failing test, the minimal change, files touched and the verification command. Add risks with rollback and any decision I must make. Spec: [SPEC]. Repository map: [MAP]. Scenario matrix: [MATRIX]
```

## Common mistakes

- Planning one large slice ("implement feature") that cannot be verified independently.
- Listing files that were never opened.
- Omitting the rollback story for schema or contract changes.
- Starting implementation while open questions remain.

## Related skills

- [Repository Explorer](../repository-explorer/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 2: Developer Ways of Working](../../handbook/02_developer_ways_of_working/README.md)
- [Chapter 4: AI Assisted Development](../../handbook/04_ai_assisted_development/README.md)

Prompts:

- [Implementation Planning](../../prompts/development/implementation-planning.md)
- [Code Generation From a Plan](../../prompts/development/code-generation.md)
- [Existing Code Modification](../../prompts/development/existing-code-modification.md)

Workflows:

- [Build a new feature](../../workflows/01_feature_development.md)
- [Introduce a new API](../../workflows/04_new_api.md)
- [Change a database schema](../../workflows/05_database_schema_change.md)
