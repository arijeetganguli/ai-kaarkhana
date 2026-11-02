---
id: requirement-clarification
title: "Requirement Clarification"
category: requirements
skills: [requirement-analyst]
---

# Requirement Clarification

## Problem it solves

A requirement is vague or incomplete and is about to be implemented on guesses.

## When to use

Before planning or coding any story, ticket or change request, and whenever acceptance criteria are missing.

## Required context

- Requirement text exactly as written.
- Domain glossary or related tickets.
- Constraints such as deadlines, compliance and affected systems.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
You are acting as a requirements analyst. Do not design or write code.

Requirement:
[PASTE REQUIREMENT]

Domain context:
[GLOSSARY, RELATED RULES, CONSTRAINTS]

Produce:
1. The requirement restated in one or two sentences.
2. Functional requirements (REQ-n) and non functional requirements (NFR-n).
3. Every term, condition or number that is undefined or ambiguous.
4. Assumptions you would have to make to proceed, each marked NEEDS CONFIRMATION with the risk if wrong.
5. Open questions ordered by impact on design, each addressed to a role (product owner, architect, compliance, operations).
6. A verdict: READY TO IMPLEMENT or BLOCKED BY QUESTIONS (list numbers).

Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.
```

## Expected AI output

- Restated requirement.
- REQ and NFR lists with IDs.
- Ambiguities, assumptions and owner-addressed questions.
- A READY or BLOCKED verdict.

## Validation steps

- [ ] Every assumption is marked, none stated as fact.
- [ ] Questions are answerable by a named person.
- [ ] Send the question list to the owner before implementing.
- [ ] No design or code appears in the output.

## Related skills

- [Requirement Analyst](../../skills/requirement-analyst/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
