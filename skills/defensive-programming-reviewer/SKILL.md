---
name: defensive-programming-reviewer
description: "Reviews code for unhandled null, empty, invalid, boundary and failure cases, and recommends intentional behaviour for each (reject, default, retry, escalate) with tests. Use when reviewing or writing code that handles external input or dependencies."
license: MIT
metadata:
  activity: quality
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Defensive Programming Reviewer

## Purpose

Ensure every important execution path has intentional behaviour. Not every gap is fixed by adding an else block: each needs a decision.

## When to invoke

- Reviewing code that parses input, calls external services or handles money, time or permissions.
- A crash, silent failure or wrong default occurred in production.
- AI-generated code looks correct on the happy path only.

## Required input

- Code to review and its callers where possible.
- Contract for inputs and outputs, error handling conventions of the project.
- Existing tests.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. List each input and each dependency result that the code consumes.
2. For each, ask what happens on null, empty, wrong type, out of range and unexpected value.
3. Find conditionals, switches and pattern matches. For each, state which cases are handled and which are not.
4. For each unhandled path choose the intended behaviour: reject early, safe default (only if specified), retry, degrade or fail loudly. Record the reasoning.
5. Check error handling: swallowed exceptions, catch-all handlers, lost causes, leaked resources, partial updates without a transaction.
6. Check external calls for timeouts, retries with limits, idempotency and handling of malformed responses.
7. Propose code changes and the tests that prove each decision.
8. Mark decisions that need a business owner instead of choosing a behaviour yourself.

## Expected output

- Findings table: location, unhandled case, risk, recommended behaviour, decision owner.
- Proposed changes with tests.
- Items where the right behaviour is unspecified.

## Validation checklist

- [ ] Every finding names a concrete input or state that triggers it.
- [ ] Recommendations explain why a default is acceptable when one is suggested.
- [ ] No blanket `try/catch` or empty `else` was added to silence a finding.
- [ ] Each recommended behaviour has a test.
- [ ] Business decisions are flagged, not made.

## Example usage

Input:

> `String label(Order o) { if (o.status == PAID) return "Paid"; else if (o.status == SHIPPED) return "Shipped"; }`

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Finding: no `return` for CANCELLED, REFUNDED or null status; compiler may pass it and callers may receive null.
Recommendation: handle all enum values explicitly with an exhaustive switch (compile-time check when new status is added); null status is rejected at the boundary.
Decision owner: product, for the label of REFUNDED.
```

## Sample prompts

```text
Review the code below as the Defensive Programming Reviewer. For each input, dependency result, conditional and exception handler list the unhandled cases, the intended behaviour you recommend with reasoning, and a test. Flag cases where the business must decide. Do not add catch-all handlers or empty else blocks. Code: [CODE]
```

## Common mistakes

- Adding `else { return null; }` or `catch (Exception e) {}` to make the warning go away.
- Substituting default values that quietly hide a bug.
- Validating deep inside the code instead of at the boundary.
- Recommending retries for non idempotent operations.

## Related skills

- [Control Flow Analyst](../control-flow-analyst/SKILL.md)
- [Edge Case Hunter](../edge-case-hunter/SKILL.md)
- [Code Quality Reviewer](../code-quality-reviewer/SKILL.md)
- [Security Reviewer](../security-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 6: Defensive Programming and Edge Case Engineering](../../handbook/06_defensive_programming/README.md)

Prompts:

- [Defensive Coding Pass](../../prompts/development/defensive-coding.md)
- [Null Handling Review](../../prompts/code_review/null-handling-review.md)
- [Exception Handling Review](../../prompts/code_review/exception-handling-review.md)
- [Missing Condition Detection](../../prompts/code_review/missing-condition-detection.md)

Workflows:

- [Build a new feature](../../workflows/01_feature_development.md)
- [Fix a defect](../../workflows/02_defect_fix.md)
- [Review a pull request](../../workflows/09_pull_request_review.md)

Examples:

- [examples/python/README.md](../../examples/python/README.md) scenarios S1, S2, S4
