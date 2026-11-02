# Glossary

Terms used in the handbook, with the meaning they have **in this repository**. Where an industry term has several meanings, the definition says which one is used. Entries link to the place where the idea is taught.

## A

**Acceptance criteria.** Observable, testable statements that must be true for a requirement to count as done. Written as Given/When/Then or as plain checkable sentences. See [Chapter 3](../handbook/03_requirement_engineering/README.md) and [Acceptance criteria generation](../prompts/requirements/acceptance-criteria-generation.md).

**Agent.** An AI assistant that can take multi-step actions with tools (read files, run commands, edit code) rather than only answer in chat. The more autonomy an agent has, the stronger the automatic verification must be. See [Chapter 4](../handbook/04_ai_assisted_development/README.md).

**Agent Skills.** An open file format for packaging reusable instructions: a folder with a `SKILL.md` that has `name` and `description` front matter. Assistants load a skill when its description matches the task. The skills in this repository use that format. See [Skills](../skills/README.md).

**ADR (Architecture Decision Record).** A short document that records one significant design decision, its context, the options considered and the consequences. See the [ADR template](../templates/adr_template.md) and [ADR drafting](../prompts/architecture/adr-drafting.md).

**AI native engineering.** Working practices in which AI assistance is part of every stage of the lifecycle, while engineers keep ownership of requirements, design, verification and outcomes. See [Chapter 1](../handbook/01_ai_native_engineering/README.md).

**Assertion.** A statement in a test that fails if the code's behaviour is wrong. A test without a meaningful assertion proves nothing. See [Chapter 5](../handbook/05_test_driven_development/README.md).

## B

**Boundary value.** An input at the edge of a valid range, such as the largest or smallest accepted value and the values just outside it. A common source of off by one defects. See [Boundary testing](../prompts/testing/boundary-testing.md).

**Broken Code Lab.** The collection of deliberately defective programs with tests in [`examples/broken_code_lab`](../examples/broken_code_lab/README.md).

## C

**Characterisation test.** A test that records what existing code *currently does*, so you can change the code and notice any change in behaviour. Used before refactoring untested code. See [Refactoring Specialist](../skills/refactoring-specialist/SKILL.md).

**Context engineering.** Deliberately choosing what information an AI model sees for a task (the relevant code, constraints, examples and what to ignore), because anything outside the model's context window is invisible to it. See [Chapter 2](../handbook/02_developer_ways_of_working/README.md#5-context-engineering) and [Chapter 4](../handbook/04_ai_assisted_development/README.md#4-context-management).

**Contract test.** A test that checks that a provider and its consumers agree on an interface (fields, types, error semantics). See [Contract testing](../prompts/testing/contract-testing.md).

## D

**Defensive programming.** Writing code so that invalid input, missing data and failing dependencies produce deliberate, safe behaviour instead of accidental behaviour. See [Chapter 6](../handbook/06_defensive_programming/README.md).

**DORA metrics.** Software delivery performance measures published by the DORA research programme (classically deployment frequency, lead time for changes, change failure rate and time to restore service). The definitions and the set of metrics have been refined over time, so check [dora.dev](https://dora.dev) for the current ones. See [Chapter 12](../handbook/12_engineering_leadership/README.md#8-measuring-dora-metrics).

## E

**Edge case.** An input or situation at or beyond the normal range of expectations: empty, null, maximum, duplicate, concurrent, slow, out of order. See [Edge Case Hunter](../skills/edge-case-hunter/SKILL.md).

**Equivalent mutant.** A mutant that changes the code but not its observable behaviour, so no test can kill it. Not every surviving mutant is a weak test. See [Chapter 5](../handbook/05_test_driven_development/property_based_and_mutation_testing.md).

## F

**Flaky test.** A test that sometimes passes and sometimes fails without any change to the code. Usually caused by timing, shared state, ordering or external dependencies. See [Flaky test diagnosis](../prompts/testing/flaky-test-diagnosis.md).

## G

**Gate.** A checkpoint in a workflow where work cannot proceed until a condition is met, such as "tests are red for the right reason". Every workflow diagram marks its gates. See [Workflows](../workflows/README.md).

## H

**Hallucination.** Output from an AI model that is fluent and confident but not true: an API that does not exist, a test run that did not happen, a requirement nobody stated. Common failure patterns are catalogued in [Chapter 1](../handbook/01_ai_native_engineering/README.md#6-common-failure-patterns) and [Chapter 7](../handbook/07_code_quality/README.md).

**Human in the loop.** The principle that a person reviews, understands and approves AI-produced work before it has effect. The responsibility model is in [Chapter 1](../handbook/01_ai_native_engineering/README.md#3-developer-accountability).

## I

**Idempotency.** An operation is idempotent if doing it twice has the same effect as doing it once. Essential for safe retries. See [Chapter 6](../handbook/06_defensive_programming/README.md#4-timeouts-retries-and-idempotency).

**Integration test.** A test that exercises real collaboration across a boundary (a database, an HTTP client, a message queue) rather than replacing it with a mock. See [Integration Test Engineer](../skills/integration-test-engineer/SKILL.md).

## M

**Maturity model.** A staged description of how developed a practice is. The one used here has five levels from Ad hoc to Optimising and is this handbook's own framework, not an industry standard. See [Maturity assessment](maturity_assessment.md).

**Mutation testing.** Deliberately introducing small defects ("mutants") into code and checking that the tests fail. Surviving mutants point at missing or weak assertions. See [Mutation Testing Specialist](../skills/mutation-testing-specialist/SKILL.md).

## P

**Property-based testing.** Testing a rule that should hold for many generated inputs ("sorting twice gives the same result as sorting once") instead of a handful of hand-picked examples. See [Chapter 5](../handbook/05_test_driven_development/property_based_and_mutation_testing.md).

**Prompt.** The instructions and context you give an AI model. In this repository a *prompt* is a ready to paste template in [`prompts/`](../prompts/README.md); a *skill* is a reusable capability the assistant loads.

**Prompt injection.** An attack in which untrusted text (a web page, an issue, a file) contains instructions that an AI assistant follows as if they came from the user. See [Chapter 9](../handbook/09_security_engineering/README.md#10-prompt-injection).

## R

**Red, Green, Refactor.** The TDD cycle: write a failing test (red), make it pass with the simplest change (green), then improve the design while the tests stay green (refactor). See [Chapter 5](../handbook/05_test_driven_development/README.md).

**Regression.** A defect in behaviour that used to work. A regression test pins the correct behaviour so it cannot silently break again. See [Regression Analyst](../skills/regression-analyst/SKILL.md).

## S

**Scenario matrix.** A table of inputs and conditions with the expected outcome for each, built before implementation. See the [template](../templates/scenario_matrix_template.md).

**Skill.** A reusable, tool-agnostic capability description with a fixed structure (purpose, inputs, instructions, output, validation checklist). See [Skill registry](../skills/REGISTRY.md).

**SPACE framework.** A research framework that describes developer productivity along five dimensions: satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. See [Chapter 12](../handbook/12_engineering_leadership/README.md#4-evaluating-engineering-productivity).

**STRIDE.** A mnemonic for threat categories: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. See [Chapter 9](../handbook/09_security_engineering/README.md#11-threat-modelling).

## T

**TDD (Test Driven Development).** Developing by writing a failing test before the code that satisfies it. See [Chapter 5](../handbook/05_test_driven_development/README.md).

**Traceability.** The ability to follow a requirement to the scenarios, tests and code that satisfy it, and back. See [Requirement traceability check](../prompts/requirements/requirement-traceability-check.md).

## W

**Workflow.** An ordered, gated sequence of skills and prompts for a kind of work, such as fixing a defect. See [Workflows](../workflows/README.md).

Back to [documentation index](README.md).
