---
description: "Business Rule Discovery: Business rules live only inside code or in people's heads, and are about to be changed or reimplemented."
---
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

---
Generated from [prompts/requirements/business-rule-discovery.md](../../prompts/requirements/business-rule-discovery.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
