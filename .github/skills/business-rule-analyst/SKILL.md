---
name: business-rule-analyst
description: "Extracts and verifies business rules from requirements, code, data and tests, and flags rules that are implicit, contradictory or undocumented. Use when behaviour must be preserved or a rule is unclear."
license: MIT
metadata:
  activity: requirements
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Business Rule Analyst

## Purpose

Make business rules explicit, sourced and testable. Distinguish rules that are documented from rules that merely happen to be implemented.

## When to invoke

- Modernising or refactoring code whose rules are only in the implementation.
- A new requirement interacts with existing pricing, eligibility, approval or state rules.
- Two sources (ticket, code, tests, support knowledge) seem to disagree.

## Required input

- The requirement, and code or data in which rules are implemented.
- Existing tests, which often document intended rules.
- Domain glossary and any policy or regulation references.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Extract each rule as a single sentence in the form: when [condition], then [outcome].
2. Give each rule an ID and cite its source: document section, ticket, file and line, test name.
3. Classify each rule: documented, implemented only, tested only, or inferred.
4. Detect conflicts: rules with overlapping conditions and different outcomes, and conditions that no rule covers.
5. Identify parameters (thresholds, rates, dates) and where each value is configured.
6. For implemented-only rules, ask whether they are intended behaviour or accidental. Do not decide for the business.
7. Produce a decision list for the business owner and a list of rules that need characterisation tests.

## Expected output

- Rule catalogue: ID, rule statement, source, classification, parameters.
- Conflicts and gaps with the rules involved.
- Decisions needed, each with options and consequences.
- Characterisation test candidates for implemented-only rules.

## Validation checklist

- [ ] Every rule cites at least one source.
- [ ] Implemented-only rules are not presented as approved.
- [ ] Overlapping or uncovered conditions were checked.
- [ ] Hard-coded values are listed as parameters with locations.
- [ ] Open decisions are addressed to a business owner.

## Example usage

Input:

> Code: `if (age > 65) discount = 0.10;` Ticket: "Seniors get 10 percent off."

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
BR-1 (implemented only): customers older than 65 get 10 percent off. Source: `PricingService:41`.
BR-2 (documented): "Seniors get 10 percent off", no age defined. Source: ticket.
Conflict candidate: "senior" defined by `> 65` in code; common definitions use `>= 65`. Decision needed from product owner.
Characterisation tests: ages 64, 65, 66.
```

## Sample prompts

```text
Act as the Business Rule Analyst. From the code and tests below, extract every business rule as 'when X then Y' with an ID and source. Classify each as documented, implemented only, tested only or inferred, and list conflicts and uncovered conditions. Do not change anything. Code: [CODE]. Tests: [TESTS]. Documents: [DOCS]
```

## Common mistakes

- Treating current code behaviour as correct requirements.
- Merging two similar rules into one and losing a distinction.
- Not recording where thresholds are configured.
- Resolving a conflict silently instead of escalating it.

## Related skills

- [Requirement Analyst](../requirement-analyst/SKILL.md)
- [Regression Analyst](../regression-analyst/SKILL.md)
- [Refactoring Specialist](../refactoring-specialist/SKILL.md)

## Related resources

Handbook:

- [Chapter 3: Requirement Engineering](../../../handbook/03_requirement_engineering/README.md)

Prompts:

- [Business Rule Discovery](../../../prompts/requirements/business-rule-discovery.md)
- [Requirement Traceability Check](../../../prompts/requirements/requirement-traceability-check.md)

Workflows:

- [Refactor an existing service](../../../workflows/03_service_refactoring.md)
- [Fix a defect](../../../workflows/02_defect_fix.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S3 (boundary)
