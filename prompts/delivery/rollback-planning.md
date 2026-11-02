---
id: rollback-planning
title: "Rollback Planning"
category: delivery
skills: [database-design-reviewer, architecture-reviewer]
---

# Rollback Planning

## Problem it solves

Rollback is assumed to be easy until it is needed and turns out to be impossible.

## When to use

Before any release, especially with data or contract changes.

## Required context

- Change set.
- Deployment tooling.
- Data changes.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Create a rollback plan.

Change set: [DIFF / RELEASE CONTENTS]
Deployment tooling: [TOOL]
Data and contract changes: [MIGRATIONS, EVENTS, APIS]

For each component: what is rolled back and how (redeploy previous version, disable flag, revert configuration), the exact order, who executes, expected duration, and how success is verified.
Address: data written by the new version that the old version cannot read; irreversible migrations (state them clearly and propose expand-and-contract alternatives); messages already published; caches and sessions; downstream consumers; the point of no return.
Define rollback triggers (metric and threshold) and the decision owner. Provide a rehearsal checklist. If a rollback is not possible for part of the change, say so and propose roll-forward steps instead.
```

## Expected AI output

- Step-by-step rollback.
- Triggers and owner.
- Points of no return.
- Rehearsal checklist.

## Validation steps

- [ ] Rehearse in a pre-production environment.
- [ ] Triggers match dashboards that exist.
- [ ] Irreversible steps were approved.

## Related skills

- [Database Design Reviewer](../../skills/database-design-reviewer/SKILL.md)
- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)

Back to [Delivery prompts](README.md) · [Prompt library](../README.md)
