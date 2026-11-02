---
id: existing-code-modification
title: "Existing Code Modification"
category: development
skills: [regression-analyst, tdd-engineer]
---

# Existing Code Modification

## Problem it solves

Changing legacy code without understanding its current behaviour causes regressions.

## When to use

Before modifying code that already has callers and behaviour.

## Required context

- The code to change.
- Existing tests.
- The intended change.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
I need to change existing code. First protect current behaviour, then change it.

Intended change:
[CHANGE]

Code:
[CODE OR FILE PATHS]

Do the following in order:
1. List the current observable behaviours of this code (inputs, outputs, errors, side effects) and every caller you can find. Cite the file and symbol for every claim you make about the code.
2. Map each behaviour to an existing test. For behaviour with no test, write characterisation tests that pin the current behaviour, including quirks. Run them against the unchanged code and show they pass.
3. Write the failing test for the intended change. Show it failing.
4. Make the smallest change that passes. Run the full relevant suite.
5. List each existing test you changed and why. Changing an existing assertion needs an explicit behaviour change in the requirement.

Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Behaviour and caller inventory.
- Characterisation tests passing before the change.
- Failing then passing test for the change.
- List of any modified tests with justification.

## Validation steps

- [ ] Characterisation tests pass on the original code.
- [ ] Modified tests are justified by the requirement.
- [ ] Callers were searched in all relevant repositories.

## Related skills

- [Regression Analyst](../../skills/regression-analyst/SKILL.md)
- [TDD Engineer](../../skills/tdd-engineer/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
