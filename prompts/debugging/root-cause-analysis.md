---
id: root-cause-analysis
title: "Root Cause Analysis"
category: debugging
skills: [debugging-specialist, regression-analyst]
---

# Root Cause Analysis

## Problem it solves

Post-incident reviews stop at the proximate cause and miss systemic gaps.

## When to use

After mitigation, for a blameless review.

## Required context

- Incident timeline and evidence.
- The fix.
- Detection and response details.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- Cause chain with evidence.
- Safeguard gaps.
- Action items with owners and verification.

## Validation steps

- [ ] Each why cites evidence.
- [ ] Action items are measurable.
- [ ] The review is blameless.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)
- [Regression Analyst](../../skills/regression-analyst/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
