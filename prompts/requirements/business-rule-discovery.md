---
id: business-rule-discovery
title: "Business Rule Discovery"
category: requirements
skills: [business-rule-analyst]
---

# Business Rule Discovery

## Problem it solves

Business rules live only inside code or in people's heads, and are about to be changed or reimplemented.

## When to use

Before modernising, refactoring or extending rule-heavy code such as pricing, eligibility or approvals.

## Required context

- The code that implements the rules.
- Existing tests.
- Any specification, policy or ticket text.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Extract business rules from the material below. Do not change any code.

Code:
[PASTE CODE OR FILE PATHS]

Tests:
[PASTE TESTS OR FILE PATHS]

Documents:
[PASTE SPEC EXCERPTS]

For each rule produce: ID (BR-n), statement in the form "When [condition], then [outcome]", source (file and line, test name or document section), classification (documented, implemented only, tested only, inferred), and the parameters it depends on with where each is configured.

Then list:
- Conflicts: rules whose conditions overlap with different outcomes.
- Gaps: input combinations that no rule covers.
- Implemented-only rules that look accidental (for example off by one boundaries, magic numbers). Do not decide they are wrong; list them as decisions for the business owner.
- Characterisation tests needed to pin current behaviour before any change.

Cite the file and symbol for every claim you make about the code. Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.
```

## Expected AI output

- Rule catalogue with sources and classification.
- Conflicts and gaps.
- Decision list for the business owner.
- List of characterisation tests.

## Validation steps

- [ ] Spot check five rules against the code yourself.
- [ ] Every rule has a source.
- [ ] Implemented-only rules are not treated as approved.
- [ ] Decisions were reviewed by the business owner.

## Related skills

- [Business Rule Analyst](../../skills/business-rule-analyst/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
