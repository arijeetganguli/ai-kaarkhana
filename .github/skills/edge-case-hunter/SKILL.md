---
name: edge-case-hunter
description: "Systematically discovers edge cases, boundary conditions, failure modes and negative scenarios for a requirement or function before implementation, and records them as a scenario matrix. Use before writing tests or code."
license: MIT
metadata:
  activity: requirements
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Edge Case Hunter

## Purpose

Find the inputs and situations that break a design while it is still cheap to change, and convert each into a test candidate with an explicit expected behaviour.

## When to invoke

- Before writing tests for a feature (TDD red phase).
- When reviewing a function that handles conditions, collections, money, time or external calls.
- When a defect escaped and you need to know what else is likely to be missed.

## Required input

- Requirement or function signature with its documented behaviour.
- Known business rules and constraints (ranges, enums, state machines).
- Dependencies the code calls (databases, HTTP APIs, queues).

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Enumerate inputs and state: each parameter, each field, each piece of stored state, each dependency response.
2. Walk the eight categories: absent data, boundaries, invalid input, invalid state, dependency failure, time and retries, concurrency, security.
3. For each numeric or ordered input, list the boundary values: below, at and above each limit, plus zero, negative, maximum and overflow.
4. For each condition, list the true case, the false case and the case where neither branch is explicitly specified.
5. For each dependency, list success, empty result, error, timeout, slow response and malformed response.
6. For every scenario, state the expected behaviour. If the requirement does not say, mark it `UNSPECIFIED` and raise a question.
7. Rank by risk (likelihood x impact) and flag which scenarios must be automated.

## Expected output

- A scenario matrix: ID, category, input or state, expected behaviour, source (requirement ID or `UNSPECIFIED`), priority, planned test level.
- A list of unspecified behaviours that need a decision.
- The top five scenarios most likely to be mishandled.

## Validation checklist

- [ ] All eight categories were considered, and skipped ones are justified.
- [ ] Every boundary has below, at and above values.
- [ ] Every scenario has an expected result or an `UNSPECIFIED` flag.
- [ ] No expected behaviour was invented to fill a gap.
- [ ] Scenarios are concrete enough to become test names.

## Example usage

Input:

> Function: `shippingFee(orderTotal, country)`. Rule: free shipping at or above 100.00 for domestic orders.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
SC-01 Boundary: total 99.99, domestic -> fee charged.
SC-02 Boundary: total 100.00, domestic -> free (rule says "at or above").
SC-03 Boundary: total 0.00 -> `UNSPECIFIED` (empty order allowed?).
SC-04 Invalid: total -1 -> reject. Error type `UNSPECIFIED`.
SC-05 Absent: country null -> reject.
SC-06 Unknown country code -> `UNSPECIFIED` (default rate or error?).
```

## Sample prompts

```text
Use the Edge Case Hunter skill on this requirement and code. Produce a scenario matrix with ID, category, input/state, expected behaviour, source and priority. Mark anything the requirement does not define as UNSPECIFIED instead of choosing a behaviour. Requirement: [REQUIREMENT]. Code: [CODE OR SIGNATURE]
```

## Common mistakes

- Producing a generic list ("test null, test empty") that is not tied to this requirement.
- Choosing expected behaviour for unspecified cases instead of asking.
- Covering only invalid inputs and forgetting invalid states and dependency failures.
- Listing scenarios without a priority, so everything becomes a unit test or nothing does.

## Related skills

- [Requirement Analyst](../requirement-analyst/SKILL.md)
- [Business Rule Analyst](../business-rule-analyst/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)
- [Defensive Programming Reviewer](../defensive-programming-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 3: Requirement Engineering](../../../handbook/03_requirement_engineering/README.md)
- [Chapter 6: Defensive Programming and Edge Case Engineering](../../../handbook/06_defensive_programming/README.md)

Prompts:

- [Edge Case Discovery](../../../prompts/requirements/edge-case-discovery.md)
- [Scenario Matrix Generation](../../../prompts/requirements/scenario-matrix-generation.md)
- [Boundary Testing](../../../prompts/testing/boundary-testing.md)
- [Negative Testing](../../../prompts/testing/negative-testing.md)

Workflows:

- [Build a new feature](../../../workflows/01_feature_development.md)
- [Fix a defect](../../../workflows/02_defect_fix.md)

Examples:

- Edge case diagram: [assets/diagrams/edge-case-discovery.svg](../../../assets/diagrams/edge-case-discovery.svg)
