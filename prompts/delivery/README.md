# Delivery prompts

Release with evidence: deployment risk, rollback, readiness, observability and release notes.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [Deployment Risk Analysis](deployment-risk-analysis.md) | Changes reach production without a clear view of what could go wrong. | [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md), [regression-analyst](../../skills/regression-analyst/SKILL.md) |
| [Rollback Planning](rollback-planning.md) | Rollback is assumed to be easy until it is needed and turns out to be impossible. | [database-design-reviewer](../../skills/database-design-reviewer/SKILL.md), [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md) |
| [Release Readiness Check](release-readiness-check.md) | Releases happen on feeling rather than evidence. | [pr-readiness-reviewer](../../skills/pr-readiness-reviewer/SKILL.md), [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |
| [Observability Gap Analysis](observability-gap-analysis.md) | Failures cannot be detected or diagnosed because the right signals are missing. | [architecture-reviewer](../../skills/architecture-reviewer/SKILL.md), [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |
| [Changelog and Release Notes](changelog-and-release-notes.md) | Release notes are copied commit messages that users cannot use. | [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |

Related handbook chapter: [Chapter 11: Engineering Delivery and Operations](../../handbook/11_delivery_and_operations/README.md)

Back to the [prompt library](../README.md).
