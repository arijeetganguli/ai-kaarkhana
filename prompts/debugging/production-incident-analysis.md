---
id: production-incident-analysis
title: "Production Incident Analysis"
category: debugging
skills: [debugging-specialist, performance-analyst]
---

# Production Incident Analysis

## Problem it solves

During an incident, teams jump to causes and lose track of facts.

## When to use

An incident is open and you need structured analysis from the available evidence.

## Required context

- Alert, symptoms and timeline.
- Recent deployments and configuration changes.
- Metrics, logs and traces (sanitised).

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Help analyse a live production incident. Prioritise restoring service over finding the root cause.

Impact: [WHO/WHAT IS AFFECTED, SINCE WHEN]
Timeline of events: [TIMESTAMPED FACTS]
Recent changes: [DEPLOYS, CONFIG, TRAFFIC]
Evidence: [METRICS, LOGS, TRACES - sanitised, no secrets or personal data]

1. Build a fact table: time | fact | source. Separate facts from assumptions.
2. List mitigation options (rollback, feature flag off, scale, failover, rate limit) with the expected effect, risk and how to verify. Recommend the fastest safe mitigation.
3. Give hypotheses about the cause with supporting and contradicting evidence. Say what to check next to discriminate between them.
4. List information still missing and who can supply it.
5. Draft the status update for stakeholders (impact, current action, next update time) in plain language.
Do not state a root cause as fact until evidence confirms it.
```

## Expected AI output

- Fact table.
- Mitigation options.
- Hypotheses and next checks.
- Stakeholder update draft.

## Validation steps

- [ ] Facts have sources.
- [ ] The incident commander approved mitigation.
- [ ] No secrets or personal data were pasted.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)
- [Performance Analyst](../../skills/performance-analyst/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
