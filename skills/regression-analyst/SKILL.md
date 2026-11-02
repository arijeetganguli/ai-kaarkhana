---
name: regression-analyst
description: "Assesses the regression risk of a change: identifies impacted behaviour, callers and data, selects or creates regression tests, and checks that existing tests were preserved. Use before merging changes to existing behaviour."
license: MIT
metadata:
  activity: debugging
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Regression Analyst

## Purpose

Make the blast radius of a change explicit and ensure that existing behaviour is protected by tests before it is modified.

## When to invoke

- Modifying code with many callers or unclear behaviour.
- A defect was fixed and you need to ensure it stays fixed.
- An AI assistant has edited or deleted existing tests.

## Required input

- The diff or planned change.
- Repository map or search access to find callers and consumers.
- Existing test suite and the test commands.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. List the behaviours changed or potentially affected by the diff: public methods, contracts, data formats, configuration, side effects.
2. Find all callers, consumers and downstream data users of the changed symbols.
3. Map each affected behaviour to existing tests. Mark behaviours with no test.
4. Check the diff for modified or removed tests and assertions. Each must be justified by a deliberate behaviour change.
5. For uncovered behaviour, write characterisation tests that pin current behaviour before changing code.
6. For fixed defects, add a regression test that fails on the old code.
7. Run the full relevant suite and report the results. Record untested residual risk.

## Expected output

- Impact table: behaviour, callers, covering tests, gaps.
- Characterisation and regression tests added.
- Test modifications and their justification.
- Executed test results and residual risks.

## Validation checklist

- [ ] Callers and consumers were actually searched for.
- [ ] No assertion was weakened without explanation.
- [ ] New regression tests failed on the old code.
- [ ] Residual untested behaviour is listed.
- [ ] Full relevant suite results are reported from a real run.

## Example usage

Input:

> Change: `parseDate` now accepts ISO week dates. 14 callers.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Impacted: `parseDate`, `ImportJob` (2 formats), `ReportFilter`.
Tests: `ParseDateTest` covers 3 formats; no test for invalid input -> add characterisation tests for invalid strings (currently returns null).
Modified tests: none. Suite: 212 passed.
```

## Sample prompts

```text
Act as the Regression Analyst. For this diff, list affected behaviours, find all callers, map them to existing tests, and flag uncovered behaviour. Write characterisation tests for uncovered behaviour first. List every changed or removed test with justification. Diff: [DIFF]
```

## Common mistakes

- Trusting coverage percentage instead of mapping behaviours to tests.
- Updating failing tests to match new output without questioning the change.
- Searching only the current module and not other repositories or consumers.
- Skipping data and configuration impact.

## Related skills

- [Debugging Specialist](../debugging-specialist/SKILL.md)
- [Refactoring Specialist](../refactoring-specialist/SKILL.md)
- [Business Rule Analyst](../business-rule-analyst/SKILL.md)

## Related resources

Handbook:

- [Chapter 5: Test Driven Development](../../handbook/05_test_driven_development/README.md)
- [Chapter 10: Code Review and Pull Requests](../../handbook/10_code_review_and_pull_requests/README.md)

Prompts:

- [Regression Test Generation](../../prompts/testing/regression-test-generation.md)
- [Existing Code Modification](../../prompts/development/existing-code-modification.md)

Workflows:

- [Fix a defect](../../workflows/02_defect_fix.md)
- [Refactor an existing service](../../workflows/03_service_refactoring.md)
