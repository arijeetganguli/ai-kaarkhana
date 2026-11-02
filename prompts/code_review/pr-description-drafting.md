---
id: pr-description-drafting
title: "PR Description Drafting"
category: code_review
skills: [pr-readiness-reviewer, documentation-engineer]
---

# PR Description Drafting

## Problem it solves

PR descriptions restate the diff and omit intent, risk and verification.

## When to use

Opening a pull request.

## Required context

- Diff.
- Requirement link.
- Test results you actually ran.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Draft a pull request description from the material below. Use only facts present in it.

Diff: [DIFF]
Ticket or requirement: [LINK AND TEXT]
Tests I ran and their output: [COMMANDS AND RESULTS]
Decisions I made: [NOTES]

Use these sections: Summary (why, in two or three sentences), What changed (grouped by behaviour not by file), How to verify (commands and expected results), Test evidence (what was run, results), Risks and rollout (including migration and rollback), Known limitations and follow-ups, AI assistance (which parts were AI-assisted and how they were validated).
Rules: do not claim tests passed unless the output above shows it; do not mention behaviour not in the diff; flag anything that needs reviewer attention.
```

## Expected AI output

- A complete PR description.

## Validation steps

- [ ] Every claim matches the diff.
- [ ] Test claims match real output.
- [ ] You can answer questions about each change.

## Related skills

- [PR Readiness Reviewer](../../skills/pr-readiness-reviewer/SKILL.md)
- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
