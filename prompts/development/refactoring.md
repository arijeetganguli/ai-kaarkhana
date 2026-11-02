---
id: refactoring
title: "Behaviour Preserving Refactoring"
category: development
skills: [refactoring-specialist, regression-analyst]
---

# Behaviour Preserving Refactoring

## Problem it solves

Refactoring requests turn into rewrites that change behaviour.

## When to use

Code is hard to change and you want structure improved without behaviour change.

## Required context

- The code and its tests.
- The structural problem to solve.
- Public API constraints.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Refactor the code below without changing behaviour.

Goal: [WHAT SHOULD BE EASIER AFTER THE REFACTORING]
Public API that must not change: [SIGNATURES]
Code: [CODE OR FILE PATHS]

Process:
1. Run the existing tests and show the result. If coverage of this code is weak, write characterisation tests first, run them and show they pass on the unchanged code.
2. Propose an ordered list of small named refactorings (extract function, rename, introduce parameter object, replace conditional, inline).
3. Apply one refactoring at a time. After each, run the tests and show the result.
4. If you notice a bug or odd behaviour, do not fix it. Log it under "Observations".
5. Stop when the goal is met. Do not add features.

Finish with the list of refactorings, test results after each step, and observations. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Baseline test result.
- Ordered refactorings with test results.
- Observations log.

## Validation steps

- [ ] The diff between steps is reviewable.
- [ ] Behaviour change is nil, check with the baseline tests.
- [ ] Observed bugs are tracked separately.

## Related skills

- [Refactoring Specialist](../../skills/refactoring-specialist/SKILL.md)
- [Regression Analyst](../../skills/regression-analyst/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
