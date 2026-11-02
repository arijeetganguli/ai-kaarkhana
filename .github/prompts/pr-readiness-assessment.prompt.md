---
description: "PR Readiness Assessment: Pull requests arrive for review incomplete, wasting reviewer time."
---
Assess whether this pull request is ready for human review.

Diff: [DIFF]
Description: [PR DESCRIPTION]
Acceptance criteria: [AC]
CI and test output: [OUTPUT]

Check and report PASS, FAIL or UNKNOWN with evidence for each: single purpose and reviewable size; each acceptance criterion mapped to a test; tests added for behaviour changes and run results real (not claimed); no existing tests weakened, skipped or deleted without justification; error and edge cases handled; security-sensitive paths flagged; migrations and contract changes have rollout and rollback; documentation and release notes updated; description explains what, why, how to verify, risks and limitations.
Give a verdict (READY, READY WITH COMMENTS, NOT READY), the blocking items, and where a human reviewer should spend attention.

---
Generated from [prompts/code_review/pr-readiness-assessment.md](../../prompts/code_review/pr-readiness-assessment.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
