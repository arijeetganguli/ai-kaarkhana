---
id: mutation-testing
title: "Mutation Testing Analysis"
category: testing
skills: [mutation-testing-specialist]
---

# Mutation Testing Analysis

## Problem it solves

Tests pass but would not catch real defects.

## When to use

After tests exist for important logic, or when coverage is high but quality is doubtful.

## Required context

- Code and passing tests.
- Mutation tool availability (PIT, Stryker, mutmut).

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Assess how well these tests detect defects.

Code: [CODE]
Tests: [TESTS]
Run the suite first and confirm it is green.

If [PIT | Stryker | mutmut] is configured, run it for the scoped files and report the surviving mutants from its report.
Otherwise mutate manually: flip each comparison operator, negate conditions, change numeric constants by one, remove statements, swap returned values, remove null checks.
For each mutation state whether any test would fail. For survivors: explain the behaviour change, classify (missing test, weak assertion, equivalent mutant, dead code) and write the smallest test that kills it. Show that the new test fails against the mutant and passes against the original.
Report the mutation score only if a tool produced it. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Surviving mutants table.
- Killing tests.
- Tool-based score or an explicit 'not measured'.

## Validation steps

- [ ] Each new test fails against its mutant.
- [ ] Equivalent mutants are justified.
- [ ] Score comes from a tool run.

## Related skills

- [Mutation Testing Specialist](../../skills/mutation-testing-specialist/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
