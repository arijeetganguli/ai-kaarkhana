---
description: "Test Data Builder Design: Tests are cluttered with large object setup, hiding what matters."
---
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

---
Generated from [prompts/testing/test-data-builder-design.md](../../prompts/testing/test-data-builder-design.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
