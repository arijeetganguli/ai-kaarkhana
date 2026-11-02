# Templates

Reusable starting points for the artefacts that make AI assisted engineering reviewable. Copy a template, fill it in, and delete the instructions at the top. Placeholders are written as `<angle brackets>` or `[BRACKETED]` so they cannot be mistaken for real content.

## Engineering artefacts

| Template | Use it to | Related workflow |
| --- | --- | --- |
| [Requirement](requirement_template.md) | Turn an ambiguous request into rules, acceptance criteria, edge behaviour and open questions | [Feature development](../workflows/01_feature_development.md) |
| [Scenario matrix](scenario_matrix_template.md) | List every distinguishable behaviour with exact expected results; this is the test plan | [Feature development](../workflows/01_feature_development.md), [Testing](../workflows/07_unit_and_integration_testing.md) |
| [Technical design](technical_design_template.md) | Compare options against quality attributes and record failure, security and rollout behaviour | [New API](../workflows/04_new_api.md), [Database schema change](../workflows/05_database_schema_change.md) |
| [ADR](adr_template.md) | Record one significant decision, its alternatives and consequences | [New API](../workflows/04_new_api.md) |
| [Test plan](test_plan_template.md) | Plan test levels, data, environments and the checks that prove the tests are strong | [Testing](../workflows/07_unit_and_integration_testing.md) |
| [AI task](ai_task_template.md) | Hand a bounded piece of work to an assistant with context, constraints and evidence rules | All |

## Review and delivery

| Template | Use it to | Related workflow |
| --- | --- | --- |
| [Pull request](pull_request_template.md) | Describe a change with risk, test evidence, rollback and honest AI disclosure | [Pull request review](../workflows/09_pull_request_review.md) |
| [Code review](code_review_template.md) | Record what was and was not reviewed, with severity labelled findings | [Pull request review](../workflows/09_pull_request_review.md) |
| [AI code review checklist](ai_code_review_checklist.md) | Review any change, with extra checks for AI generated code | [Pull request review](../workflows/09_pull_request_review.md) |

## For contributors

| Template | Use it to |
| --- | --- |
| [Skill](skill_template.md) | Add a skill to [`skills/`](../skills/README.md) |
| [Prompt](prompt_template.md) | Add a prompt to [`prompts/`](../prompts/README.md) |
| [Handbook chapter](handbook_chapter_template.md) | Add or extend a [handbook](../handbook/README.md) chapter |

The contributor templates include a *quality bar* at the end. Delete that section from the file you create, but do check your work against it. See [CONTRIBUTING](../CONTRIBUTING.md).

## Notes

- Templates are exempt from some checks that apply to the rest of the repository (they contain placeholders by design). `scripts/validate_docs.py` skips them for placeholder detection but still checks that they are non empty and that any links inside them resolve.
- The GitHub pull request template that GitHub shows automatically is in [`.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md); the longer [pull request template](pull_request_template.md) here is the full version for substantial changes.

[Back to the repository README](../README.md)
