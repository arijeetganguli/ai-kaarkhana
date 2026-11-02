---
description: "Deployment Risk Analysis: Changes reach production without a clear view of what could go wrong."
---
Analyse the risk of deploying this change.

Change set: [DIFF OR RELEASE NOTES]
Deployment method and environment: [ROLLING | BLUE GREEN | CANARY]
Dependencies and consumers: [LIST]

Assess: behaviour changes visible to users or consumers; schema, data and contract changes and their compatibility with old and new versions running together during rollout; configuration and feature flag changes; performance and capacity effects; dependencies deployed in a required order; observability (which metrics and logs will show a problem, and the thresholds that should trigger rollback).
Output: risk table (risk, likelihood, impact, detection, mitigation) with reasons; recommended rollout strategy (flag, canary percentage, timing); go/no-go criteria; open questions. Do not invent likelihood percentages.

---
Generated from [prompts/delivery/deployment-risk-analysis.md](../../prompts/delivery/deployment-risk-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
