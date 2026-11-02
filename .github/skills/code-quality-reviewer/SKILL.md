---
name: code-quality-reviewer
description: "Reviews code for maintainability: clarity, cohesion, coupling, complexity, duplication, naming, SOLID violations and testability, citing concrete locations and proposing proportionate improvements. Use for code review and before refactoring."
license: MIT
metadata:
  activity: quality
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Code Quality Reviewer

## Purpose

Provide specific, prioritised quality findings that a team can act on, separating real maintainability risks from taste.

## When to invoke

- Reviewing a pull request or AI-generated change for maintainability.
- Deciding whether code needs refactoring before adding a feature.
- Setting up or tuning quality gates.

## Required input

- Code or diff under review.
- Project conventions, linter and static analysis configuration.
- Static analysis output if available (complexity, duplication, smells).

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Read the change for intent first. Note what it is meant to do.
2. Check naming, size and cohesion of functions and classes; flag long parameter lists and mixed responsibilities.
3. Measure or estimate complexity: nesting depth, branches per function, and report tool numbers when available.
4. Find duplication and near-duplication and say whether abstraction is warranted yet.
5. Check coupling: dependency direction, hidden global state, concrete types where interfaces help testing.
6. Check tests: do they cover the change, are they readable, would they survive refactoring.
7. Check against project conventions and existing patterns.
8. Classify each finding as Blocker, Major, Minor or Nit, with location and a concrete suggestion.

## Expected output

- Summary of intent and overall assessment.
- Findings table: severity, location, issue, why it matters, suggested change.
- Technical debt items to track rather than fix now.
- Tool results used, with commands.

## Validation checklist

- [ ] Each finding cites a file and line or symbol.
- [ ] Severity is justified by impact, not taste.
- [ ] Suggestions are proportionate to the size of the change.
- [ ] Automated tool results are separated from judgement.
- [ ] Positive observations are included where deserved.

## Example usage

Input:

> A 140-line function `processOrder` with 6 levels of nesting and three payment branches.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Major: `processOrder:12-151` mixes validation, pricing and persistence; extract `validate`, `price`, `persist` (testable units). Characterisation tests first.
Minor: duplicated tax rounding at lines 63 and 98; extract helper only if a third use appears.
Nit: variable `x2` -> `discountedTotal`.
```

## Sample prompts

```text
Review this diff as the Code Quality Reviewer. Report findings with severity (Blocker/Major/Minor/Nit), location, why it matters and a proportionate suggestion. Separate tool-measured facts from judgement. Do not rewrite the code. Diff: [DIFF]. Conventions: [CONVENTIONS]
```

## Common mistakes

- Style nitpicking that linters should handle.
- Recommending patterns and abstractions with no current need.
- Reviewing without reading the tests.
- Giving a score instead of actionable findings.

## Related skills

- [Refactoring Specialist](../refactoring-specialist/SKILL.md)
- [PR Readiness Reviewer](../pr-readiness-reviewer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 7: Code Quality](../../../handbook/07_code_quality/README.md)
- [Chapter 10: Code Review and Pull Requests](../../../handbook/10_code_review_and_pull_requests/README.md)

Prompts:

- [Independent Code Review](../../../prompts/code_review/independent-code-review.md)
- [PR Readiness Assessment](../../../prompts/code_review/pr-readiness-assessment.md)
- [Behaviour Preserving Refactoring](../../../prompts/development/refactoring.md)

Workflows:

- [Refactor an existing service](../../../workflows/03_service_refactoring.md)
- [Review a pull request](../../../workflows/09_pull_request_review.md)
