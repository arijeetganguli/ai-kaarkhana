---
description: "Null Handling Review: Null or absent values cause crashes or silent wrong results far from their source."
---
Review null and absent value handling.

Code: [CODE]
Nullability facts (schema, API contract, annotations): [FACTS]

1. For every parameter, field, return value and lookup, state whether null/absent is possible according to the facts above. Where the facts are silent, say UNKNOWN.
2. Trace each possibly-null value to where it is dereferenced or used in a decision. Report unguarded uses with file and line.
3. For each, recommend: reject at the boundary, model absence explicitly (Optional, option types, empty collection), or provide a default only if the requirement defines it. Explain the choice.
4. Identify places where null is silently converted into a default, empty string or zero, hiding data problems.
5. Provide a failing test for each unguarded use.
Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/code_review/null-handling-review.md](../../prompts/code_review/null-handling-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
