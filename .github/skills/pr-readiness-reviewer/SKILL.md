---
name: pr-readiness-reviewer
description: "Checks whether a pull request is ready for human review: scope, tests and their evidence, description, risks, documentation and quality gates. Use before requesting review, and as an independent pass."
license: MIT
metadata:
  activity: review
  difficulty: beginner
  frameworks: "any"
  version: "1.0"
---

# PR Readiness Reviewer

## Purpose

Save reviewers' time and prevent avoidable defects by verifying readiness against objective criteria before review begins.

## When to invoke

- Before marking a pull request as ready for review.
- When reviewing a pull request you did not write, to triage it.
- As a final gate before merge.

## Required input

- The diff and the PR description.
- Linked requirement or ticket and acceptance criteria.
- CI results and test run output.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Check scope: one purpose, no unrelated changes, size reviewable in one sitting.
2. Check traceability: each acceptance criterion maps to a test or an explanation.
3. Check test evidence: tests added or changed, run results are real, failing-before and passing-after for defects.
4. Check that existing tests were not weakened, skipped or deleted without justification.
5. Check risk areas: security, data migration, public contracts, concurrency, configuration and rollout.
6. Check documentation, release notes and operational impact (monitoring, alerts, rollback).
7. Check the description: what, why, how to verify, risks, known limitations.
8. Return a verdict: ready, ready with comments, or not ready, with a list of blocking items.

## Expected output

- Verdict and blocking items.
- Checklist results with evidence.
- Risk summary and suggested reviewer focus areas.
- Suggested improvements to the PR description.

## Validation checklist

- [ ] Every claim of passing tests is backed by output or a CI link.
- [ ] Acceptance criteria are mapped.
- [ ] Unrelated changes are called out.
- [ ] Rollback and monitoring are addressed for risky changes.
- [ ] Verdict follows from the evidence.

## Example usage

Input:

> PR: 'Add cancellation reason', 18 files, tests added, description is two lines.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Verdict: not ready.
Blocking: AC-3 (reason max length 200) has no test. Migration is irreversible, rollback not described.
Comments: split the unrelated formatter change into its own PR. Reviewer focus: migration and `OrderService.cancel`.
```

## Sample prompts

```text
Act as the PR Readiness Reviewer. Assess this pull request against the checklist: scope, acceptance criteria traceability, test evidence, weakened tests, risks, documentation, rollback and description quality. Give a verdict and blocking items. Diff: [DIFF]. Description: [DESCRIPTION]. Acceptance criteria: [AC]. CI output: [CI]
```

## Common mistakes

- Accepting 'tests pass' without evidence.
- Reviewing style while ignoring risk.
- Approving large mixed PRs.
- Letting the AI approve its own work in the same context.

## Related skills

- [Code Quality Reviewer](../code-quality-reviewer/SKILL.md)
- [Security Reviewer](../security-reviewer/SKILL.md)
- [Regression Analyst](../regression-analyst/SKILL.md)

## Related resources

Handbook:

- [Chapter 10: Code Review and Pull Requests](../../../handbook/10_code_review_and_pull_requests/README.md)

Prompts:

- [PR Readiness Assessment](../../../prompts/code_review/pr-readiness-assessment.md)
- [PR Description Drafting](../../../prompts/code_review/pr-description-drafting.md)
- [Independent Code Review](../../../prompts/code_review/independent-code-review.md)

Workflows:

- [Review a pull request](../../../workflows/09_pull_request_review.md)
- [Build a new feature](../../../workflows/01_feature_development.md)

Examples:

- Checklist: [templates/ai_code_review_checklist.md](../../../templates/ai_code_review_checklist.md)
