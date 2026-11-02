---
id: independent-code-review
title: "Independent Code Review"
category: code_review
skills: [code-quality-reviewer, pr-readiness-reviewer]
---

# Independent Code Review

## Problem it solves

The same assistant that wrote the code reviews it and shares its blind spots.

## When to use

Before human review of any significant AI-assisted change. Run in a fresh session without the authoring conversation.

## Required context

- Diff and tests.
- The requirement.
- Project conventions.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
You are an independent reviewer who did not write this code. Review it as a sceptical senior engineer.

Requirement and acceptance criteria: [REQUIREMENT]
Diff including tests: [DIFF]
Conventions: [CONVENTIONS]

Report findings in a table: severity (Blocker, Major, Minor, Nit) | file:line | what is wrong | why it matters | suggested change.
Review for: correctness against each acceptance criterion, unhandled cases (null, empty, boundary, error, concurrency), security, test quality (weak assertions, mocks hiding behaviour, tests changed to fit code), unrequested behaviour, maintainability and conventions.
Rules:
- Verify claims by reading the code. Do not assume the author's description is true.
- Prefer a few well-evidenced findings to many speculative ones; mark speculation as such.
- Do not rewrite the code. Do not approve; give a recommendation (approve, approve with comments, request changes) with the reasons.
Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Findings table by severity.
- Recommendation with reasons.

## Validation steps

- [ ] Triage each Blocker and Major yourself before acting.
- [ ] The review ran in a clean context.
- [ ] Human reviewer still reviews.

## Related skills

- [Code Quality Reviewer](../../skills/code-quality-reviewer/SKILL.md)
- [PR Readiness Reviewer](../../skills/pr-readiness-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
