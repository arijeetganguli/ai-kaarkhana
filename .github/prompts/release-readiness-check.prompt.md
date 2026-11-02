---
description: "Release Readiness Check: Releases happen on feeling rather than evidence."
---
Assess release readiness against evidence.

Release contents (PRs, tickets): [LIST]
CI and test results: [LINKS OR OUTPUT]
Operational information (monitoring, alerts, runbooks, on-call): [INFO]

For each item mark PASS, FAIL or UNKNOWN with evidence: all PRs merged with required reviews and green checks; acceptance criteria verified for each ticket; regression and smoke tests defined and run; security and dependency scans reviewed; migrations rehearsed; feature flags and defaults checked; monitoring, alerts and dashboards cover the new behaviour; runbooks and release notes updated; rollback plan exists and was reviewed; stakeholders and support informed.
Output a go/no-go recommendation, blockers, and accepted risks that need explicit sign-off. Do not mark PASS without evidence.

---
Generated from [prompts/delivery/release-readiness-check.md](../../prompts/delivery/release-readiness-check.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
