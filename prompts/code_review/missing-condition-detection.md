---
id: missing-condition-detection
title: "Missing Condition Detection"
category: code_review
skills: [control-flow-analyst, defensive-programming-reviewer]
---

# Missing Condition Detection

## Problem it solves

A branch exists for some cases and silently ignores others.

## When to use

Reviewing if/else chains, switch statements, pattern matches and state handling.

## Required context

- Code.
- The domain enumeration or state machine.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Find missing conditions in this code.

Code: [CODE]
Domain values or state machine: [ENUM VALUES / STATES / TRANSITIONS]

For each if/else chain, switch, match and ternary list: the values or states it handles, the values or states it does not handle (from the domain list above, including null and values added in future), and what the code does for them today (falls through, returns null, returns a default, throws).
For each unhandled case recommend one of: explicit handling with defined behaviour, exhaustive match so the compiler flags new values, rejection with a specific error, or DECISION NEEDED. Explain why simply adding an else block would or would not be correct.
Provide a failing test for each case you recommend handling. Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Handled/unhandled table.
- Recommended behaviour per case.
- Tests.

## Validation steps

- [ ] The unhandled list matches the domain list.
- [ ] No empty else was added.
- [ ] New enum values would trigger a failing test or compile error.

## Related skills

- [Control Flow Analyst](../../skills/control-flow-analyst/SKILL.md)
- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
