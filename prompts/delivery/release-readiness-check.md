---
id: release-readiness-check
title: "Release Readiness Check"
category: delivery
skills: [pr-readiness-reviewer, documentation-engineer]
---

# Release Readiness Check

## Problem it solves

Releases happen on feeling rather than evidence.

## When to use

Before a production release.

## Required context

- Release contents.
- CI results.
- Operational readiness information.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Assess release readiness against evidence.

Release contents (PRs, tickets): [LIST]
CI and test results: [LINKS OR OUTPUT]
Operational information (monitoring, alerts, runbooks, on-call): [INFO]

For each item mark PASS, FAIL or UNKNOWN with evidence: all PRs merged with required reviews and green checks; acceptance criteria verified for each ticket; regression and smoke tests defined and run; security and dependency scans reviewed; migrations rehearsed; feature flags and defaults checked; monitoring, alerts and dashboards cover the new behaviour; runbooks and release notes updated; rollback plan exists and was reviewed; stakeholders and support informed.
Output a go/no-go recommendation, blockers, and accepted risks that need explicit sign-off. Do not mark PASS without evidence.
```

## Expected AI output

- Checklist with evidence.
- Recommendation and blockers.
- Accepted risks.

## Validation steps

- [ ] UNKNOWN items resolved.
- [ ] A human with authority signs off.
- [ ] Evidence links are stored with the release.

## Related skills

- [PR Readiness Reviewer](../../skills/pr-readiness-reviewer/SKILL.md)
- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Delivery prompts](README.md) · [Prompt library](../README.md)
