---
description: "Root Cause Analysis: Post-incident reviews stop at the proximate cause and miss systemic gaps."
---
Prepare a blameless root cause analysis.

Incident summary and timeline: [TIMELINE]
Evidence: [LOGS, GRAPHS, DIFFS]
Fix applied: [FIX]
Detection and response: [HOW DETECTED, TIME TO DETECT/MITIGATE]

Produce:
1. Trigger, proximate cause and contributing factors (separate them).
2. A five whys chain where each step cites evidence; stop where evidence ends and mark it as hypothesis.
3. Why existing safeguards (tests, review, monitoring, rollout) did not prevent or catch it.
4. What went well.
5. Action items: each with an owner role, a preventive or detective category, a verification method and priority. Prefer systemic fixes (tests, automation, alerts) over 'be more careful'.
Do not assign blame to individuals. Do not invent timings, numbers or evidence.

---
Generated from [prompts/debugging/root-cause-analysis.md](../../prompts/debugging/root-cause-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
