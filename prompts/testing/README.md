# Testing prompts

Test first and test well: TDD, unit, integration, contract, boundary, negative, mutation and regression tests.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [TDD Test Generation](tdd-test-generation.md) | Tests written after the code mirror the implementation instead of specifying behaviour. | [tdd-engineer](../../skills/tdd-engineer/SKILL.md), [unit-test-engineer](../../skills/unit-test-engineer/SKILL.md) |
| [Unit Test Generation](unit-test-generation.md) | Existing code has weak or no unit tests. | [unit-test-engineer](../../skills/unit-test-engineer/SKILL.md) |
| [Integration Test Generation](integration-test-generation.md) | Mocked unit tests pass while the real database query or HTTP call is wrong. | [integration-test-engineer](../../skills/integration-test-engineer/SKILL.md) |
| [Contract Testing](contract-testing.md) | API changes break consumers because the contract is implicit. | [api-contract-reviewer](../../skills/api-contract-reviewer/SKILL.md), [integration-test-engineer](../../skills/integration-test-engineer/SKILL.md) |
| [Boundary Testing](boundary-testing.md) | Off by one and comparison errors survive because only typical values are tested. | [edge-case-hunter](../../skills/edge-case-hunter/SKILL.md), [unit-test-engineer](../../skills/unit-test-engineer/SKILL.md) |
| [Negative Testing](negative-testing.md) | Only success paths are tested, so invalid input behaviour is accidental. | [unit-test-engineer](../../skills/unit-test-engineer/SKILL.md), [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md) |
| [Mutation Testing Analysis](mutation-testing.md) | Tests pass but would not catch real defects. | [mutation-testing-specialist](../../skills/mutation-testing-specialist/SKILL.md) |
| [Regression Test Generation](regression-test-generation.md) | A fixed bug returns, or changed code silently alters behaviour. | [regression-analyst](../../skills/regression-analyst/SKILL.md), [debugging-specialist](../../skills/debugging-specialist/SKILL.md) |
| [Test Data Builder Design](test-data-builder-design.md) | Tests are cluttered with large object setup, hiding what matters. | [unit-test-engineer](../../skills/unit-test-engineer/SKILL.md) |
| [Flaky Test Diagnosis](flaky-test-diagnosis.md) | A test fails intermittently and the team retries instead of fixing. | [debugging-specialist](../../skills/debugging-specialist/SKILL.md), [integration-test-engineer](../../skills/integration-test-engineer/SKILL.md) |

Related handbook chapter: [Chapter 5: Test Driven Development](../../handbook/05_test_driven_development/README.md)

Back to the [prompt library](../README.md).
