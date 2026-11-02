---
id: changelog-and-release-notes
title: "Changelog and Release Notes"
category: delivery
skills: [documentation-engineer]
---

# Changelog and Release Notes

## Problem it solves

Release notes are copied commit messages that users cannot use.

## When to use

Preparing a release.

## Required context

- Merged PRs and commits since the last release.
- Audience.
- Format convention.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Draft release notes and a changelog entry.

Previous release: [VERSION]
Changes since then (PR titles, descriptions, commit messages): [LIST]
Audience: [USERS | API CONSUMERS | OPERATORS]
Format: Keep a Changelog sections (Added, Changed, Deprecated, Removed, Fixed, Security)

Rules:
- Use only the information above. Do not invent changes or version numbers.
- Describe the effect for the audience, not the implementation.
- Call out breaking changes, migrations and required configuration separately with exact steps.
- Group related changes. Link PR numbers as given.
- Suggest the semantic version bump (major, minor, patch) with the reason; a human decides.
End with items you could not classify.
```

## Expected AI output

- Changelog entry.
- Release notes for the audience.
- Breaking change section.
- Version bump suggestion.

## Validation steps

- [ ] Every statement maps to a merged change.
- [ ] Breaking changes are complete.
- [ ] Version bump reviewed by a human.

## Related skills

- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Delivery prompts](README.md) · [Prompt library](../README.md)
