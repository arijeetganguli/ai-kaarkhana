---
description: "Acceptance Criteria Generation: Acceptance criteria are missing, vague or not testable."
---
Write acceptance criteria for the requirement below.

Requirement and confirmed answers:
[PASTE CLARIFIED REQUIREMENT]

Rules:
- Use the form: Given [state], When [action], Then [observable result].
- One behaviour per criterion. Give each an ID (AC-<requirement>.<n>) and link it to its REQ ID.
- Include at least: the main success path, every boundary of every numeric or date rule (below, at, above), every invalid input, and every failure of a dependency named in the requirement.
- Each Then must be verifiable by an automated test. Reject wording such as "works correctly" or "handles gracefully".
- Where the requirement does not define the outcome, write the criterion with the outcome set to UNSPECIFIED and list the question.
- Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

Finish with a table: AC ID | REQ ID | test level (unit, integration, end to end) | automation priority.

---
Generated from [prompts/requirements/acceptance-criteria-generation.md](../../prompts/requirements/acceptance-criteria-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
