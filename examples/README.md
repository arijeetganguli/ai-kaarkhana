# Examples

Runnable code that shows the handbook's guidance on real defects. Everything here is executable and verified by CI.

| Folder | What it is | Run with |
| --- | --- | --- |
| [`java/`](java/README.md) | 9 scenarios, JUnit 5 and Mockito | `mvn test` |
| [`python/`](python/README.md) | 9 scenarios, pytest | `pytest` |
| [`typescript/`](typescript/README.md) | 9 scenarios, Vitest | `npm test` |
| [`end_to_end/`](end_to_end/README.md) | One feature from raw requirement to passing tests, with real test output | read |
| [`broken_code_lab/`](broken_code_lab/README.md) | 8 defective programs to fix, with tests | `pytest` |
| [`scenarios.md`](scenarios.md) | Scenario catalogue: requirement, problem, fix and why it matters | read |

## The nine scenarios

| ID | Scenario | Defect class |
| --- | --- | --- |
| S1 | Discount by loyalty tier | Missing else behaviour |
| S2 | Greeting for a customer | Missing null handling |
| S3 | Senior discount eligibility | Incorrect boundary condition |
| S4 | Parse an order quantity | Inadequate exception handling |
| S5 | May a user edit a document | Wrong boolean logic |
| S6 | Shipping fee | TDD from requirement to passing tests |
| S7 | Late fee | Weak assertions, mutation testing |
| S8 | Data access or remote call | Missing integration tests |
| S9 | Order pricing | Refactoring exercise |

Details: [scenario catalogue](scenarios.md).

## How to use these examples

- **Learning:** read `initial` first and try to find the defect yourself, then read `improved` and the tests.
- **Teaching:** run the `initial_defect` tests to show each failure, then the improved tests.
- **Practising with AI:** give an assistant the `initial` code with a prompt from the [prompt library](../prompts/README.md) (for example [Missing condition detection](../prompts/code_review/missing-condition-detection.md)) and compare its answer with `improved`. Judge it by whether its fix makes the tests pass, not by how confident it sounds.

## Related

- [Chapter 5: Test Driven Development](../handbook/05_test_driven_development/README.md)
- [Chapter 6: Defensive Programming and Edge Case Engineering](../handbook/06_defensive_programming/README.md)
- [Skills](../skills/README.md) and [workflows](../workflows/README.md)

Back to the [repository README](../README.md).
