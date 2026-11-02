---
description: "Production Incident Analysis: During an incident, teams jump to causes and lose track of facts."
---
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

---
Generated from [prompts/debugging/production-incident-analysis.md](../../prompts/debugging/production-incident-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
