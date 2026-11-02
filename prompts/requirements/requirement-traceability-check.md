---
id: requirement-traceability-check
title: "Requirement Traceability Check"
category: requirements
skills: [requirement-analyst, pr-readiness-reviewer]
---

# Requirement Traceability Check

## Problem it solves

A change claims to implement a requirement but nobody has checked that every criterion is implemented and tested.

## When to use

Before opening a PR, and when reviewing someone else's PR.

## Required context

- Requirement and acceptance criteria.
- The diff including tests.
- Test run results.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Check traceability between the requirement, the implementation and the tests.

Acceptance criteria:
[PASTE AC LIST]

Diff (code and tests):
[PASTE DIFF]

For each acceptance criterion report: implemented where (file and symbol), tested by (test name), test would fail if the behaviour were removed (YES, NO, UNSURE and why), and status (COVERED, WEAK, MISSING).
Then list: behaviour in the diff that no criterion asks for (scope creep or undocumented rules), and criteria that are implemented but untested.
Cite the file and symbol for every claim you make about the code. Do not mark a criterion COVERED unless you read the test and its assertions.
```

## Expected AI output

- A per-criterion table with status.
- Unrequested behaviour in the diff.
- A list of MISSING and WEAK items to fix before review.

## Validation steps

- [ ] Open two COVERED rows and confirm the test asserts the claimed behaviour.
- [ ] All MISSING items were fixed or accepted by the owner.
- [ ] Unrequested behaviour was removed or documented.

## Related skills

- [Requirement Analyst](../../skills/requirement-analyst/SKILL.md)
- [PR Readiness Reviewer](../../skills/pr-readiness-reviewer/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
