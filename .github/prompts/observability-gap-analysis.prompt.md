---
description: "Observability Gap Analysis: Failures cannot be detected or diagnosed because the right signals are missing."
---
Find observability gaps.

Feature or component: [DESCRIPTION / CODE]
Existing telemetry (metrics, logs, traces, alerts, dashboards): [LIST]
Service level objectives: [SLOS OR 'none']

For each user-visible operation and each dependency call identify: how we would know it failed, how we would know it is slow, how we would find the cause for one failing request, and who is alerted.
Check: structured logs with correlation IDs; no secrets or personal data in logs; metrics for rate, errors and duration; traces across service boundaries; business metrics for the new behaviour; alerts based on symptoms with actionable runbooks; dashboards for rollout comparison.
Output: gap table (scenario, missing signal, proposed signal, effort, priority) and the minimum set needed before release.

---
Generated from [prompts/delivery/observability-gap-analysis.md](../../prompts/delivery/observability-gap-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
