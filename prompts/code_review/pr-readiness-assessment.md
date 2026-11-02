---
id: pr-readiness-assessment
title: "PR Readiness Assessment"
category: code_review
skills: [pr-readiness-reviewer]
---

# PR Readiness Assessment

## Problem it solves

Pull requests arrive for review incomplete, wasting reviewer time.

## When to use

Before requesting review and when triaging a PR.

## Required context

- PR diff and description.
- Acceptance criteria.
- CI output.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Assess whether this pull request is ready for human review.

Diff: [DIFF]
Description: [PR DESCRIPTION]
Acceptance criteria: [AC]
CI and test output: [OUTPUT]

Check and report PASS, FAIL or UNKNOWN with evidence for each: single purpose and reviewable size; each acceptance criterion mapped to a test; tests added for behaviour changes and run results real (not claimed); no existing tests weakened, skipped or deleted without justification; error and edge cases handled; security-sensitive paths flagged; migrations and contract changes have rollout and rollback; documentation and release notes updated; description explains what, why, how to verify, risks and limitations.
Give a verdict (READY, READY WITH COMMENTS, NOT READY), the blocking items, and where a human reviewer should spend attention.
```

## Expected AI output

- Per-check results with evidence.
- Verdict.
- Reviewer focus areas.

## Validation steps

- [ ] Every PASS has evidence.
- [ ] NOT READY items were fixed.
- [ ] Description updated.

## Related skills

- [PR Readiness Reviewer](../../skills/pr-readiness-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
