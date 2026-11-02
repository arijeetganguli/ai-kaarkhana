# Requirements prompts

Understand and specify before building: clarification, acceptance criteria, business rules, edge cases and traceability.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [Requirement Clarification](requirement-clarification.md) | A requirement is vague or incomplete and is about to be implemented on guesses. | [requirement-analyst](../../skills/requirement-analyst/SKILL.md) |
| [Acceptance Criteria Generation](acceptance-criteria-generation.md) | Acceptance criteria are missing, vague or not testable. | [requirement-analyst](../../skills/requirement-analyst/SKILL.md), [edge-case-hunter](../../skills/edge-case-hunter/SKILL.md) |
| [Business Rule Discovery](business-rule-discovery.md) | Business rules live only inside code or in people's heads, and are about to be changed or reimplemented. | [business-rule-analyst](../../skills/business-rule-analyst/SKILL.md) |
| [Edge Case Discovery](edge-case-discovery.md) | Edge cases are discovered in production instead of during design. | [edge-case-hunter](../../skills/edge-case-hunter/SKILL.md) |
| [Scenario Matrix Generation](scenario-matrix-generation.md) | Tests are written ad hoc, so nobody can say which requirements are covered. | [edge-case-hunter](../../skills/edge-case-hunter/SKILL.md), [requirement-analyst](../../skills/requirement-analyst/SKILL.md), [tdd-engineer](../../skills/tdd-engineer/SKILL.md) |
| [Requirement Traceability Check](requirement-traceability-check.md) | A change claims to implement a requirement but nobody has checked that every criterion is implemented and tested. | [requirement-analyst](../../skills/requirement-analyst/SKILL.md), [pr-readiness-reviewer](../../skills/pr-readiness-reviewer/SKILL.md) |

Related handbook chapter: [Chapter 3: Requirement Engineering](../../handbook/03_requirement_engineering/README.md)

Back to the [prompt library](../README.md).
