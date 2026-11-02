---
id: null-handling-review
title: "Null Handling Review"
category: code_review
skills: [defensive-programming-reviewer]
---

# Null Handling Review

## Problem it solves

Null or absent values cause crashes or silent wrong results far from their source.

## When to use

Reviewing code that consumes external data, optional fields or lookups.

## Required context

- Code.
- Data contracts or schema nullability.
- Null handling conventions.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review null and absent value handling.

Code: [CODE]
Nullability facts (schema, API contract, annotations): [FACTS]

1. For every parameter, field, return value and lookup, state whether null/absent is possible according to the facts above. Where the facts are silent, say UNKNOWN.
2. Trace each possibly-null value to where it is dereferenced or used in a decision. Report unguarded uses with file and line.
3. For each, recommend: reject at the boundary, model absence explicitly (Optional, option types, empty collection), or provide a default only if the requirement defines it. Explain the choice.
4. Identify places where null is silently converted into a default, empty string or zero, hiding data problems.
5. Provide a failing test for each unguarded use.
Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Nullability table.
- Unguarded uses.
- Recommended modelling per case.
- Tests.

## Validation steps

- [ ] UNKNOWN items were resolved with the data owner.
- [ ] Defaults are justified by requirements.
- [ ] Tests reproduce the failure.

## Related skills

- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
