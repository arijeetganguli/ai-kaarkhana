---
id: hypothesis-driven-debugging
title: "Hypothesis Driven Debugging"
category: debugging
skills: [debugging-specialist]
---

# Hypothesis Driven Debugging

## Problem it solves

Trial-and-error fixing hides the root cause.

## When to use

Any defect whose cause is not obvious.

## Required context

- Symptom with expected vs actual.
- Reproduction steps or logs.
- Relevant code.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Help me debug using hypotheses. Do not propose a fix yet.

Symptom: [ACTUAL vs EXPECTED]
Reproduction or evidence: [STEPS / LOGS / STACK TRACE]
Relevant code: [CODE]
Recent changes: [COMMITS OR DEPLOYS]

1. Restate the symptom precisely.
2. Give 2 to 4 hypotheses. For each: the mechanism, a prediction that would prove it false, and the cheapest check.
3. Rank by likelihood and cost of checking.
4. Tell me what to run or inspect first. After I report the result, update the ranking.
5. When one hypothesis survives, state the root cause, how it differs from the trigger and the symptom, and propose a failing test that reproduces it.
Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Restated symptom.
- Falsifiable hypotheses with checks.
- Next action.

## Validation steps

- [ ] Each hypothesis could be proven wrong.
- [ ] The root cause is confirmed with evidence.
- [ ] A failing test exists before the fix.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
