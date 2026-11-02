---
id: scenario-matrix-generation
title: "Scenario Matrix Generation"
category: requirements
skills: [edge-case-hunter, requirement-analyst, tdd-engineer]
---

# Scenario Matrix Generation

## Problem it solves

Tests are written ad hoc, so nobody can say which requirements are covered.

## When to use

After acceptance criteria and edge cases exist; before TDD.

## Required context

- Acceptance criteria with IDs.
- Edge case list.
- Test framework and level conventions.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Create a scenario matrix that links requirements to tests.

Acceptance criteria:
[PASTE AC LIST]

Edge cases:
[PASTE EDGE CASES]

Output a Markdown table with columns: Scenario ID (SC-n) | REQ ID | AC ID | Category | Given (state and inputs) | When | Expected result | Test level | Proposed test name | Priority.
Rules:
- Every AC has at least one scenario; every scenario traces to an AC or to an edge case marked as derived.
- Boundary scenarios use exact values.
- Test names describe behaviour, for example ships_free_when_total_equals_threshold.
- Mark scenarios whose expected result is UNSPECIFIED and do not propose a test name for them yet.
- Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

After the table list: ACs with no scenario, scenarios with no AC, and the scenarios you recommend automating first.
```

## Expected AI output

- A traceability matrix.
- Coverage gaps in both directions.
- Recommended order of automation.

## Validation steps

- [ ] Every AC appears at least once.
- [ ] Test names read as behaviour sentences.
- [ ] Unspecified results were resolved or deferred.
- [ ] The matrix is saved with the PR (template: templates/scenario_matrix_template.md).

## Related skills

- [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md)
- [Requirement Analyst](../../skills/requirement-analyst/SKILL.md)
- [TDD Engineer](../../skills/tdd-engineer/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
