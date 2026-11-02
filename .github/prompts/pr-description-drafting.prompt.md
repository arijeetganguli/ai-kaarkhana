---
description: "PR Description Drafting: PR descriptions restate the diff and omit intent, risk and verification."
---
Draft a pull request description from the material below. Use only facts present in it.

Diff: [DIFF]
Ticket or requirement: [LINK AND TEXT]
Tests I ran and their output: [COMMANDS AND RESULTS]
Decisions I made: [NOTES]

Use these sections: Summary (why, in two or three sentences), What changed (grouped by behaviour not by file), How to verify (commands and expected results), Test evidence (what was run, results), Risks and rollout (including migration and rollback), Known limitations and follow-ups, AI assistance (which parts were AI-assisted and how they were validated).
Rules: do not claim tests passed unless the output above shows it; do not mention behaviour not in the diff; flag anything that needs reviewer attention.

---
Generated from [prompts/code_review/pr-description-drafting.md](../../prompts/code_review/pr-description-drafting.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
