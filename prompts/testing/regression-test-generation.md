---
id: regression-test-generation
title: "Regression Test Generation"
category: testing
skills: [regression-analyst, debugging-specialist]
---

# Regression Test Generation

## Problem it solves

A fixed bug returns, or changed code silently alters behaviour.

## When to use

After fixing a defect, or before changing code with weak tests.

## Required context

- Defect report and the fix, or the code to be changed.
- Existing tests.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Create regression tests.

Mode: [DEFECT FIX | CHARACTERISATION BEFORE CHANGE]
Defect description or code to be changed: [TEXT / CODE]
Fix (if any): [DIFF]

For a defect fix: write the smallest test that reproduces the original defect; run it against the code before the fix (use git stash or checkout of the previous commit) and show it fails; run it with the fix and show it passes. Then add tests for two neighbouring inputs that share the root cause.
For characterisation: write tests that pin current behaviour for each branch and caller-visible output, run them on the unchanged code and show they pass. Mark behaviours that look wrong with SUSPECT.
Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Reproduction test failing before and passing after.
- Neighbouring tests.
- SUSPECT behaviours.

## Validation steps

- [ ] The test fails on the pre-fix commit.
- [ ] Names describe the bug, not the ticket number alone.
- [ ] SUSPECT items were triaged.

## Related skills

- [Regression Analyst](../../skills/regression-analyst/SKILL.md)
- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
