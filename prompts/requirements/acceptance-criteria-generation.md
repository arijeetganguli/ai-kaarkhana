---
id: acceptance-criteria-generation
title: "Acceptance Criteria Generation"
category: requirements
skills: [requirement-analyst, edge-case-hunter]
---

# Acceptance Criteria Generation

## Problem it solves

Acceptance criteria are missing, vague or not testable.

## When to use

After requirement clarification, before writing tests.

## Required context

- Clarified requirement with answered questions.
- Business rules and parameters (thresholds, rates).
- Any non functional constraints.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Write acceptance criteria for the requirement below.

Requirement and confirmed answers:
[PASTE CLARIFIED REQUIREMENT]

Rules:
- Use the form: Given [state], When [action], Then [observable result].
- One behaviour per criterion. Give each an ID (AC-<requirement>.<n>) and link it to its REQ ID.
- Include at least: the main success path, every boundary of every numeric or date rule (below, at, above), every invalid input, and every failure of a dependency named in the requirement.
- Each Then must be verifiable by an automated test. Reject wording such as "works correctly" or "handles gracefully".
- Where the requirement does not define the outcome, write the criterion with the outcome set to UNSPECIFIED and list the question.
- Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

Finish with a table: AC ID | REQ ID | test level (unit, integration, end to end) | automation priority.
```

## Expected AI output

- Numbered Given/When/Then criteria linked to requirements.
- A table of test level and priority.
- UNSPECIFIED outcomes with questions.

## Validation steps

- [ ] Each Then clause could fail an automated test.
- [ ] Boundaries have three values each.
- [ ] No criterion describes implementation.
- [ ] The product owner has reviewed the UNSPECIFIED items.

## Related skills

- [Requirement Analyst](../../skills/requirement-analyst/SKILL.md)
- [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
