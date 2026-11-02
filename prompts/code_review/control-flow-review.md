---
id: control-flow-review
title: "Control Flow Review"
category: code_review
skills: [control-flow-analyst]
---

# Control Flow Review

## Problem it solves

Branching logic hides missing branches, precedence mistakes and boundary errors.

## When to use

Reviewing code with several conditions, switches or boolean expressions.

## Required context

- The function.
- The rules it should implement.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review the control flow of this function by enumeration, not by reading.

Rules it must implement: [RULES]
Function: [CODE]

1. List every atomic condition and the variables it reads.
2. Build a decision table of condition combinations (use equivalence classes and boundaries if there are more than four conditions; say what you grouped).
3. For each row trace the code and state the actual outcome. Do this before comparing to the rules.
4. Compare to the rules. Mark mismatches and rows with no defined intended outcome.
5. Look specifically for: missing else or default, unreachable branches, conditions that are always true or false, && / || precedence, negation errors, < versus <=, switch fall-through, enum values not handled.
6. For each defect give the smallest fix and the test row that fails before and passes after.
Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Condition inventory.
- Decision table with actual vs intended.
- Defects with fixes and tests.

## Validation steps

- [ ] Spot check three table rows by tracing yourself.
- [ ] Each defect has a failing test.
- [ ] Unspecified rows were decided by the owner.

## Related skills

- [Control Flow Analyst](../../skills/control-flow-analyst/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
