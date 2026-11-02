# Scenario catalogue

Nine engineering scenarios, each implemented in Java, Python and TypeScript. Every scenario follows the same pattern:

1. **Initial implementation**: code of the kind that passes a quick review and a happy path demo.
2. **Identified problem**: what is wrong and how it fails.
3. **Improved implementation**: the fix, with the reasoning in the code comments.
4. **Automated tests**: tests for the improved code, plus *characterisation tests* that document the defect of the initial code (named `initial_defect...`).
5. **Why it matters**: below.

| ID | Scenario | Defect class | Java | Python | TypeScript |
| --- | --- | --- | --- | --- | --- |
| S1 | Discount by loyalty tier | Missing else behaviour | [s01](java/src/main/java/io/kaarkhana/examples/s01) | [s01](python/src/kaarkhana/s01_missing_else) | [s01](typescript/src/s01_missing_else) |
| S2 | Greeting for a customer | Missing null handling | [s02](java/src/main/java/io/kaarkhana/examples/s02) | [s02](python/src/kaarkhana/s02_null_handling) | [s02](typescript/src/s02_null_handling) |
| S3 | Senior discount eligibility | Incorrect boundary condition | [s03](java/src/main/java/io/kaarkhana/examples/s03) | [s03](python/src/kaarkhana/s03_boundary) | [s03](typescript/src/s03_boundary) |
| S4 | Parse an order quantity | Inadequate exception handling | [s04](java/src/main/java/io/kaarkhana/examples/s04) | [s04](python/src/kaarkhana/s04_exception_handling) | [s04](typescript/src/s04_exception_handling) |
| S5 | May a user edit a document | Incomplete or wrong boolean logic | [s05](java/src/main/java/io/kaarkhana/examples/s05) | [s05](python/src/kaarkhana/s05_boolean_logic) | [s05](typescript/src/s05_boolean_logic) |
| S6 | Shipping fee | TDD from requirement to passing tests | [s06](java/src/main/java/io/kaarkhana/examples/s06) | [s06](python/src/kaarkhana/s06_tdd_shipping) | [s06](typescript/src/s06_tdd_shipping) |
| S7 | Late fee | Weak assertions and mutation testing | [s07](java/src/main/java/io/kaarkhana/examples/s07) | [s07](python/src/kaarkhana/s07_weak_assertions) | [s07](typescript/src/s07_weak_assertions) |
| S8 | Data access / remote call | Missing integration tests, inadequate unit tests | [s08](java/src/main/java/io/kaarkhana/examples/s08) | [s08](python/src/kaarkhana/s08_integration) | [s08](typescript/src/s08_integration) |
| S9 | Order pricing | Refactoring exercise | [s09](java/src/main/java/io/kaarkhana/examples/s09) | [s09](python/src/kaarkhana/s09_refactoring) | [s09](typescript/src/s09_refactoring) |

The domains are deliberately small so that a defect can be understood in a minute. The *patterns* are the ones that appear in production code.

## S1: Missing else behaviour

- **Requirement:** three loyalty tiers (BASIC 0 percent, SILVER 5 percent, GOLD 10 percent).
- **Problem:** the `if / else if` chain has no final branch. An unknown tier makes the function return null, `None` or `undefined`, and the failure appears later in arithmetic, away from the cause.
- **Improvement:** reject anything outside the three tiers at the boundary, with a message that names the value. In Java and TypeScript the set of tiers becomes a type and the `switch` has no default, so adding a tier is a compile error until it is handled.
- **Why it matters:** the obvious fix, `else return 0`, would turn a misspelt tier into "no discount" and hide a data problem forever. Whether an unknown value should be rejected, defaulted or escalated is a decision. See [why an else block is not always the answer](../handbook/06_defensive_programming/else_is_not_always_the_answer.md).

## S2: Missing null handling

- **Requirement:** greet a customer by trimmed name. A customer with a missing or blank name is greeted as "Hello, customer". A missing customer is a caller error.
- **Problem:** the initial code dereferences possibly-null values; the failure message does not say what was missing. In TypeScript, non-null assertions (`!`) silence the compiler and not the problem.
- **Improvement:** absence is modelled explicitly (Java `Optional` from the repository, validation up front elsewhere); the one default exists because the requirement states it.
- **Why it matters:** null failures are far from their cause. A default that the requirement does not define is an invented business rule.

## S3: Incorrect boundary condition

- **Requirement:** customers aged 65 or older are eligible.
- **Problem:** `age > 65` excludes exactly 65. Tests with ages 30 and 70 pass.
- **Improvement:** inclusive comparison against a named constant, invalid ages rejected, and tests for 64, 65 and 66.
- **Why it matters:** boundary defects are the most common conditional defects, and typical-value tests never find them. Boundary scenarios come from the [Edge Case Hunter](../skills/edge-case-hunter/SKILL.md).

## S4: Inadequate exception handling

- **Requirement:** a quantity is a whole number of at least 1.
- **Problem:** `catch (Exception) { return 0 }` hides every failure, invents a value, loses the cause, and accepts negative numbers. In TypeScript `parseInt("12abc")` silently returns 12.
- **Improvement:** a specific exception that names the input and carries the original cause; range validation; strict parsing.
- **Why it matters:** swallowed exceptions turn bugs into silent data corruption. Handle only what you can handle; translate the rest.

## S5: Incomplete or wrong boolean logic

- **Requirement:** a locked document cannot be edited by anyone; otherwise admins and the owner may edit.
- **Problem:** operator precedence. `admin || owner && !locked` lets admins bypass the lock.
- **Improvement:** check the lock first; test all eight combinations of three booleans as a decision table.
- **Why it matters:** access control and eligibility logic is where precedence bugs cost the most. Enumerate; do not eyeball. See [Control Flow Analyst](../skills/control-flow-analyst/SKILL.md).

## S6: TDD from requirement to passing tests

- **Requirement:** see [the end to end walk-through](end_to_end/README.md).
- **Problem (initial):** a one-shot generated function: floating point money, `>` instead of `>=`, no country handling, no validation.
- **Improvement:** integer cents, rules from the scenario matrix, validation at the boundary, each rule driven by a failing test.
- **Why it matters:** the tests are a by-product of specifying the behaviour first, and each defect in the initial code corresponds to a scenario in the matrix.

## S7: Weak assertions and mutation testing

- **Requirement:** late fee with a 3 day grace period, 50 cents per day, capped at 2000.
- **Problem:** a test suite with 100 percent line coverage that asserts only `fee > 0`. Five hand-made mutants (the kind PIT, Stryker or mutmut generate) all survive.
- **Improvement:** exact values on both sides of every rule. The strong suite kills all five mutants; the tests demonstrate both facts.
- **Why it matters:** coverage measures execution, not verification. One *equivalent mutant* (`<=` to `<` at the grace boundary) is documented in the code to show that a mutation score of 100 percent is not always the goal.

## S8: Missing integration tests and inadequate unit tests

- **Python:** repository on SQLite. **Java and TypeScript:** HTTP client against a pricing service.
- **Problem:** a unit test with a mocked connection or HTTP client passes while the code is wrong. In Python the SQL column order and the mapping disagree; in Java and TypeScript the status code, timeout and malformed body are never handled.
- **Improvement:** tests against a real in-memory database or a real local HTTP server; domain errors for 404, 5xx, malformed body, timeout and refused connection.
- **Why it matters:** mocks encode the author's beliefs; real boundaries contradict them. Each test file contains the mocked test that passes for the defective code, so the gap is visible.

## S9: Refactoring exercise

- **Behaviour:** tier discount, bulk discount and promo code, in nested conditionals.
- **Problem:** four levels of nesting; the rules cannot be changed independently.
- **Improvement:** characterisation tests first, then small extractions, with an equivalence test over a grid of 150 inputs between the old and the new code.
- **Why it matters:** refactoring is only safe with tests that pin current behaviour, quirks included. The unknown-tier quirk is preserved and flagged for the business owner, not "fixed" mid-refactoring. While building the Java version, the first refactored draft threw a `NullPointerException` for a null tier because `Map.of(...).getOrDefault(null, ...)` rejects null keys. The equivalence test found it immediately.

## Naming convention for defect-documenting tests

Tests that document a defect of the initial implementation assert the *defective* behaviour. In Python and Java they carry `initial_defect` or `initialDefect` in their name; in TypeScript they sit in a `describe` block titled "documented defects of the initial implementation". They pass on purpose: if someone "fixes" the initial class, they fail and tell the reader the teaching example has changed.
