---
description: "Mutation Testing Analysis: Tests pass but would not catch real defects."
---
Assess how well these tests detect defects.

Code: [CODE]
Tests: [TESTS]
Run the suite first and confirm it is green.

If [PIT | Stryker | mutmut] is configured, run it for the scoped files and report the surviving mutants from its report.
Otherwise mutate manually: flip each comparison operator, negate conditions, change numeric constants by one, remove statements, swap returned values, remove null checks.
For each mutation state whether any test would fail. For survivors: explain the behaviour change, classify (missing test, weak assertion, equivalent mutant, dead code) and write the smallest test that kills it. Show that the new test fails against the mutant and passes against the original.
Report the mutation score only if a tool produced it. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/mutation-testing.md](../../prompts/testing/mutation-testing.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
