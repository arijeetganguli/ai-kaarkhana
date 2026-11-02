---
id: deployment-risk-analysis
title: "Deployment Risk Analysis"
category: delivery
skills: [architecture-reviewer, regression-analyst]
---

# Deployment Risk Analysis

## Problem it solves

Changes reach production without a clear view of what could go wrong.

## When to use

Before deploying a risky change or preparing a release.

## Required context

- Diff or release contents.
- Deployment method.
- Dependencies and consumers.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Analyse the risk of deploying this change.

Change set: [DIFF OR RELEASE NOTES]
Deployment method and environment: [ROLLING | BLUE GREEN | CANARY]
Dependencies and consumers: [LIST]

Assess: behaviour changes visible to users or consumers; schema, data and contract changes and their compatibility with old and new versions running together during rollout; configuration and feature flag changes; performance and capacity effects; dependencies deployed in a required order; observability (which metrics and logs will show a problem, and the thresholds that should trigger rollback).
Output: risk table (risk, likelihood, impact, detection, mitigation) with reasons; recommended rollout strategy (flag, canary percentage, timing); go/no-go criteria; open questions. Do not invent likelihood percentages.
```

## Expected AI output

- Risk table.
- Rollout recommendation.
- Go/no-go criteria.

## Validation steps

- [ ] Mitigations are in place before deploy.
- [ ] Rollback thresholds are agreed.
- [ ] Compatibility was verified.

## Related skills

- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)
- [Regression Analyst](../../skills/regression-analyst/SKILL.md)

Back to [Delivery prompts](README.md) · [Prompt library](../README.md)
