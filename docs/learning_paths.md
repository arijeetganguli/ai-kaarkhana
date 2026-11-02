# Learning paths

Three paths, from first contact with AI assisted engineering to leading adoption in a team. Each path lists what to read, what to practise and how to know you are ready to move on. Times are rough guides for a focused learner, not promises: take the time you need.

| Path | For | Focus | Rough effort |
| --- | --- | --- | --- |
| [Beginner](#beginner-path) | New to AI assistants, or new to engineering discipline | Ask clearly, verify everything, write tests | 1 to 2 weeks, a few hours per week |
| [Intermediate](#intermediate-path) | Comfortable day to day with an assistant | Test first workflow, defensive design, review | 3 to 4 weeks |
| [Advanced](#advanced-path) | Senior engineers, tech leads, architects | Architecture, security, delivery, team practice | 4 to 6 weeks, alongside real work |

You do not need to finish a path in order to be productive. Skip what you already know, and use the **ready when** checks to decide.

## Beginner path

**Goal:** use an assistant without giving up your own judgement.

### Read

1. [Chapter 1: AI Native Engineering](../handbook/01_ai_native_engineering/README.md), especially developer accountability and common failure patterns.
2. [Chapter 2: Developer Ways of Working](../handbook/02_developer_ways_of_working/README.md), sections on asking good questions and validating generated code.
3. [Chapter 3: Requirement Engineering](../handbook/03_requirement_engineering/README.md), the parts on clarifying and acceptance criteria.

### Use

- Skills: [Requirement Analyst](../skills/requirement-analyst/SKILL.md), [Repository Explorer](../skills/repository-explorer/SKILL.md), [Unit Test Engineer](../skills/unit-test-engineer/SKILL.md), [Documentation Engineer](../skills/documentation-engineer/SKILL.md), [PR Readiness Reviewer](../skills/pr-readiness-reviewer/SKILL.md).
- Prompts: [Requirement clarification](../prompts/requirements/requirement-clarification.md), [Repository exploration](../prompts/development/repository-exploration.md), [Unit test generation](../prompts/testing/unit-test-generation.md).

### Practise

1. Read scenarios S1 to S3 in the [scenario catalogue](../examples/scenarios.md). Before you open `improved`, find the defect in `initial` yourself.
2. Run the tests for one language (see [Getting started](getting_started.md#path-4-run-the-examples)).
3. Do Lab exercises [01 Missing else](../examples/broken_code_lab/01_missing_else/CHALLENGE.md), [02 Null dereference](../examples/broken_code_lab/02_null_dereference/CHALLENGE.md) and [07 SQL injection](../examples/broken_code_lab/07_sql_injection/CHALLENGE.md). Try first without an assistant, then with one, and compare.
4. Take your own next ticket through [Requirement Analyst](../skills/requirement-analyst/SKILL.md) before writing code.

### Ready when

- You can explain why "the assistant said it works" is not evidence.
- You ask for clarification questions before asking for code.
- You never commit code you cannot explain line by line.
- You have fixed three Lab exercises and each fix is backed by a test.

## Intermediate path

**Goal:** make test first, edge-case-aware development your default way of working with an assistant.

### Read

1. [Chapter 4: AI Assisted Development](../handbook/04_ai_assisted_development/README.md).
2. [Chapter 5: Test Driven Development](../handbook/05_test_driven_development/README.md), including [test design](../handbook/05_test_driven_development/test_design.md) and [TDD with AI](../handbook/05_test_driven_development/tdd_with_ai.md).
3. [Chapter 6: Defensive Programming and Edge Case Engineering](../handbook/06_defensive_programming/README.md) and [else is not always the answer](../handbook/06_defensive_programming/else_is_not_always_the_answer.md).
4. [Chapter 7: Code Quality](../handbook/07_code_quality/README.md) and [Chapter 10: Code Review and Pull Requests](../handbook/10_code_review_and_pull_requests/README.md).

### Use

- Skills: [Edge Case Hunter](../skills/edge-case-hunter/SKILL.md), [Implementation Planner](../skills/implementation-planner/SKILL.md), [TDD Engineer](../skills/tdd-engineer/SKILL.md), [Control Flow Analyst](../skills/control-flow-analyst/SKILL.md), [Defensive Programming Reviewer](../skills/defensive-programming-reviewer/SKILL.md), [Debugging Specialist](../skills/debugging-specialist/SKILL.md), [Refactoring Specialist](../skills/refactoring-specialist/SKILL.md), [Integration Test Engineer](../skills/integration-test-engineer/SKILL.md).
- Workflows: [Feature development](../workflows/01_feature_development.md), [Defect fix](../workflows/02_defect_fix.md), [Unit and integration testing](../workflows/07_unit_and_integration_testing.md).
- Templates: [scenario matrix](../templates/scenario_matrix_template.md), [test plan](../templates/test_plan_template.md).

### Practise

1. Work through the [end to end example](../examples/end_to_end/README.md), then repeat the method on a small feature of your own.
2. Scenarios S4 to S9 in the [catalogue](../examples/scenarios.md): note which defect class each one belongs to.
3. Lab exercises [03](../examples/broken_code_lab/03_boolean_condition/CHALLENGE.md), [05](../examples/broken_code_lab/05_missing_transaction_rollback/CHALLENGE.md), [06](../examples/broken_code_lab/06_inadequate_exception_handling/CHALLENGE.md) and [08](../examples/broken_code_lab/08_missing_integration_test/CHALLENGE.md).
4. Read the pairs in the [prompt playground](../prompts/playground.md) and rewrite one of your own weak prompts.
5. Review one pull request using the [AI code review checklist](../templates/ai_code_review_checklist.md).

### Ready when

- Every change you make starts with a scenario matrix, and the failing test comes first.
- You can say, for any test, which defect would make it fail.
- You see the red test fail for the right reason before accepting a green one.
- You write pull request descriptions that state what was verified and how.

## Advanced path

**Goal:** shape the architecture, safety and delivery practices that make AI assisted work reliable for a whole team.

### Read

1. [Chapter 8: Architecture and Design](../handbook/08_architecture_and_design/README.md).
2. [Chapter 9: Security Engineering](../handbook/09_security_engineering/README.md), including prompt injection and threat modelling.
3. [Chapter 11: Engineering Delivery and Operations](../handbook/11_delivery_and_operations/README.md).
4. [Chapter 12: Engineering Leadership](../handbook/12_engineering_leadership/README.md).
5. [Property based and mutation testing](../handbook/05_test_driven_development/property_based_and_mutation_testing.md).

### Use

- Skills: [Architecture Reviewer](../skills/architecture-reviewer/SKILL.md), [API Contract Reviewer](../skills/api-contract-reviewer/SKILL.md), [Database Design Reviewer](../skills/database-design-reviewer/SKILL.md), [Security Reviewer](../skills/security-reviewer/SKILL.md), [Performance Analyst](../skills/performance-analyst/SKILL.md), [Mutation Testing Specialist](../skills/mutation-testing-specialist/SKILL.md), [Regression Analyst](../skills/regression-analyst/SKILL.md), [Business Rule Analyst](../skills/business-rule-analyst/SKILL.md).
- Workflows: [New API](../workflows/04_new_api.md), [Database schema change](../workflows/05_database_schema_change.md), [Production incident](../workflows/08_production_incident.md), [Production release](../workflows/10_production_release.md).
- Templates: [technical design](../templates/technical_design_template.md), [ADR](../templates/adr_template.md).

### Practise

1. Run the [maturity assessment](maturity_assessment.md) with your team and choose one or two improvements.
2. Install the skills and principles into a team repository with the [adapters](../tools/README.md), and agree which are mandatory.
3. Lab exercise [04 Race condition](../examples/broken_code_lab/04_race_condition/CHALLENGE.md).
4. Run a [skill of the week](skill_of_the_week.md) rotation for a month, and collect feedback on what to improve.
5. Contribute: add or improve a skill, prompt or example following the [contribution guide](../CONTRIBUTING.md).

### Ready when

- Your team has repository instruction files, agreed review gates and a way to disclose AI assistance.
- Risky changes (security, data, money, concurrency) get independent review and extra verification.
- You can describe your delivery baseline and know what you will change next.
- Guidance is maintained: owners, review dates and a way to retire what no longer helps.

Back to [documentation index](README.md).
