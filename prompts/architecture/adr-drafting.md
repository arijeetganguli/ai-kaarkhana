---
id: adr-drafting
title: "Architecture Decision Record Drafting"
category: architecture
skills: [architecture-reviewer, documentation-engineer]
---

# Architecture Decision Record Drafting

## Problem it solves

Architectural decisions are lost, and future engineers do not know why.

## When to use

After a significant technical decision has been discussed.

## Required context

- Discussion notes.
- Options considered.
- Constraints.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Draft an Architecture Decision Record from the notes below. Use only information contained in the notes.

Notes: [MEETING NOTES / THREAD]
Options considered: [OPTIONS]
Drivers: [DRIVERS]

Format: Title (short, decision as a statement) | Status (Proposed) | Date: [DATE] | Context (forces and constraints) | Decision (what we will do, in active voice) | Alternatives considered (each with why not) | Consequences (positive, negative, risks, follow-up work) | Validation (how we will know it works or when to revisit).
If a section cannot be filled from the notes, write TO BE CONFIRMED rather than inventing content. Keep it to one page.
```

## Expected AI output

- An ADR in the template format.

## Validation steps

- [ ] Participants confirm accuracy.
- [ ] TO BE CONFIRMED items resolved.
- [ ] ADR committed next to the code.

## Related skills

- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)
- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
