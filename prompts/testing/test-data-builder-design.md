---
id: test-data-builder-design
title: "Test Data Builder Design"
category: testing
skills: [unit-test-engineer]
---

# Test Data Builder Design

## Problem it solves

Tests are cluttered with large object setup, hiding what matters.

## When to use

Tests need complex objects or the same fixtures are copied across files.

## Required context

- The domain types.
- Examples of current painful tests.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Design test data builders for the domain objects below.

Types: [TYPES]
Painful test examples: [TESTS]

Create builders (or factory functions/fixtures idiomatic to [LANGUAGE]) where:
- Defaults produce a valid object that passes all domain validation.
- A test overrides only the fields that matter to that test.
- Names express intent, for example anOrder().withTotal(100).build() or order(total=100).
- No shared mutable state and no random values unless seeded and printed on failure.
- Invalid objects are created explicitly by overriding, never by default.
Rewrite two of the painful tests with the builders and show that they still pass. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Builders or fixtures.
- Two rewritten tests.
- Notes on defaults chosen.

## Validation steps

- [ ] Defaults are valid per domain rules.
- [ ] Tests read as intent.
- [ ] No hidden shared state.

## Related skills

- [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
