---
description: "Rollback Planning: Rollback is assumed to be easy until it is needed and turns out to be impossible."
---
Create a rollback plan.

Change set: [DIFF / RELEASE CONTENTS]
Deployment tooling: [TOOL]
Data and contract changes: [MIGRATIONS, EVENTS, APIS]

For each component: what is rolled back and how (redeploy previous version, disable flag, revert configuration), the exact order, who executes, expected duration, and how success is verified.
Address: data written by the new version that the old version cannot read; irreversible migrations (state them clearly and propose expand-and-contract alternatives); messages already published; caches and sessions; downstream consumers; the point of no return.
Define rollback triggers (metric and threshold) and the decision owner. Provide a rehearsal checklist. If a rollback is not possible for part of the change, say so and propose roll-forward steps instead.

---
Generated from [prompts/delivery/rollback-planning.md](../../prompts/delivery/rollback-planning.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
