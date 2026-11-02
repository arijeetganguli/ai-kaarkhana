---
id: observability-gap-analysis
title: "Observability Gap Analysis"
category: delivery
skills: [architecture-reviewer, documentation-engineer]
---

# Observability Gap Analysis

## Problem it solves

Failures cannot be detected or diagnosed because the right signals are missing.

## When to use

Designing a feature, after an incident, or before release.

## Required context

- Code or design.
- Existing metrics, logs, traces and alerts.
- Service level objectives.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Find observability gaps.

Feature or component: [DESCRIPTION / CODE]
Existing telemetry (metrics, logs, traces, alerts, dashboards): [LIST]
Service level objectives: [SLOS OR 'none']

For each user-visible operation and each dependency call identify: how we would know it failed, how we would know it is slow, how we would find the cause for one failing request, and who is alerted.
Check: structured logs with correlation IDs; no secrets or personal data in logs; metrics for rate, errors and duration; traces across service boundaries; business metrics for the new behaviour; alerts based on symptoms with actionable runbooks; dashboards for rollout comparison.
Output: gap table (scenario, missing signal, proposed signal, effort, priority) and the minimum set needed before release.
```

## Expected AI output

- Gap table.
- Minimum set for release.
- Alert and runbook needs.

## Validation steps

- [ ] Trigger each failure in a test environment and observe the signal.
- [ ] Logs contain no secrets.
- [ ] Alerts have runbooks.

## Related skills

- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)
- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Delivery prompts](README.md) · [Prompt library](../README.md)
