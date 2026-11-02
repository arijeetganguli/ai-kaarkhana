---
name: requirement-analyst
description: "Analyses a requirement, user story or ticket before any code is written. Surfaces ambiguity, missing business rules, assumptions and testable acceptance criteria. Use when a task description is vague, new, or about to be implemented."
license: MIT
metadata:
  activity: requirements
  difficulty: beginner
  frameworks: "any"
  version: "1.0"
---

# Requirement Analyst

## Purpose

Turn a raw requirement into a precise, testable specification, and make every gap visible as a question instead of letting the AI (or the developer) silently invent an answer.

## When to invoke

- A ticket, story or chat message is about to be implemented.
- Acceptance criteria are missing, vague or contradict each other.
- You are handed an AI-generated plan and need to check it against the actual requirement.

## Required input

- The requirement text exactly as written (ticket, story, email, spec excerpt).
- Known domain context: glossary terms, existing business rules, related tickets.
- Constraints: deadline, compliance, backwards compatibility, affected systems.
- Optional: relevant code or API contracts, if the requirement changes existing behaviour.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Restate the requirement in one or two sentences. If you cannot, record that as the first ambiguity.
2. Split it into functional requirements and non functional requirements (performance, security, availability, auditability).
3. List every noun and verb that has no definition in the supplied context. Each is a candidate ambiguity.
4. Write the explicit assumptions you would need to make in order to proceed. Mark each as `NEEDS CONFIRMATION`.
5. Draft acceptance criteria as observable behaviour: given a state, when an action happens, then a verifiable result occurs.
6. Identify actors, inputs, outputs, state changes, dependencies and failure modes.
7. Produce prioritised open questions, addressed to a named role (product owner, architect, compliance).
8. Do not propose an implementation. Stop when the specification is testable or when blocked by open questions.

## Expected output

- Restated requirement.
- Functional and non functional requirements, each with an ID (`REQ-1`, `NFR-1`).
- Acceptance criteria with IDs (`AC-1.1`) that map back to requirements.
- Assumptions table: assumption, risk if wrong, who confirms.
- Open questions ordered by impact on design.
- A go / no-go statement: ready to implement, or blocked by questions N, M.

## Validation checklist

- [ ] Every acceptance criterion is observable and could fail a test.
- [ ] No assumption is presented as a fact.
- [ ] No business rule appears that is not in the source material or marked as an assumption.
- [ ] Non functional requirements are stated or explicitly marked as not provided.
- [ ] Open questions name an owner.
- [ ] Output contains no implementation design or code.

## Example usage

Input:

> Story: "Customers get free shipping on large orders."

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Open questions: What is "large" (amount, item count, weight)? Before or after discounts and tax? Does the threshold include shipping itself? Which currencies? Do marketplace-seller items count?
Draft criterion `AC-1.1`: Given an order whose qualifying total is exactly the threshold, when shipping is calculated, then the fee is `<NEEDS CONFIRMATION: charged | free>`.
Verdict: blocked by questions 1, 2 and 3.
```

## Sample prompts

```text
Analyse the requirement below using the Requirement Analyst skill. Output restated requirement, REQ/NFR list, acceptance criteria with IDs, assumptions that need confirmation, and open questions with owners. Do not design or code anything. Requirement: [PASTE REQUIREMENT]
```

```text
Review these acceptance criteria for testability. For each one, say whether a failing automated test can be written from it, and rewrite the ones that cannot: [PASTE CRITERIA]
```

## Common mistakes

- Letting the AI fill gaps with "reasonable defaults" that become undocumented business rules.
- Writing acceptance criteria that describe implementation ("uses a cache") instead of behaviour.
- Skipping non functional requirements because the ticket does not mention them.
- Treating the output as approved. Open questions still need a human answer.

## Related skills

- [Business Rule Analyst](../business-rule-analyst/SKILL.md)
- [Edge Case Hunter](../edge-case-hunter/SKILL.md)
- [Implementation Planner](../implementation-planner/SKILL.md)

## Related resources

Handbook:

- [Chapter 3: Requirement Engineering](../../handbook/03_requirement_engineering/README.md)
- [Chapter 2: Developer Ways of Working](../../handbook/02_developer_ways_of_working/README.md)

Prompts:

- [Requirement Clarification](../../prompts/requirements/requirement-clarification.md)
- [Acceptance Criteria Generation](../../prompts/requirements/acceptance-criteria-generation.md)
- [Requirement Traceability Check](../../prompts/requirements/requirement-traceability-check.md)

Workflows:

- [Build a new feature](../../workflows/01_feature_development.md)
- [Introduce a new API](../../workflows/04_new_api.md)

Examples:

- Boundary example: [examples/python/README.md](../../examples/python/README.md) scenario S3
