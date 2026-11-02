# Code review prompts

Review independently and precisely: control flow, missing conditions, null and exception handling, security, performance and PR readiness.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [Control Flow Review](control-flow-review.md) | Branching logic hides missing branches, precedence mistakes and boundary errors. | [control-flow-analyst](../../skills/control-flow-analyst/SKILL.md) |
| [Missing Condition Detection](missing-condition-detection.md) | A branch exists for some cases and silently ignores others. | [control-flow-analyst](../../skills/control-flow-analyst/SKILL.md), [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md) |
| [Null Handling Review](null-handling-review.md) | Null or absent values cause crashes or silent wrong results far from their source. | [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md) |
| [Exception Handling Review](exception-handling-review.md) | Exceptions are swallowed, over-caught or lose context, so failures are invisible or mishandled. | [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md) |
| [Security Review](security-review.md) | Security defects are introduced in generated or hand-written code and not noticed. | [security-reviewer](../../skills/security-reviewer/SKILL.md) |
| [Performance Review](performance-review.md) | A change introduces performance regressions that are invisible in small tests. | [performance-analyst](../../skills/performance-analyst/SKILL.md), [code-quality-reviewer](../../skills/code-quality-reviewer/SKILL.md) |
| [Independent Code Review](independent-code-review.md) | The same assistant that wrote the code reviews it and shares its blind spots. | [code-quality-reviewer](../../skills/code-quality-reviewer/SKILL.md), [pr-readiness-reviewer](../../skills/pr-readiness-reviewer/SKILL.md) |
| [PR Readiness Assessment](pr-readiness-assessment.md) | Pull requests arrive for review incomplete, wasting reviewer time. | [pr-readiness-reviewer](../../skills/pr-readiness-reviewer/SKILL.md) |
| [PR Description Drafting](pr-description-drafting.md) | PR descriptions restate the diff and omit intent, risk and verification. | [pr-readiness-reviewer](../../skills/pr-readiness-reviewer/SKILL.md), [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |

Related handbook chapter: [Chapter 10: Code Review and Pull Requests](../../handbook/10_code_review_and_pull_requests/README.md)

Back to the [prompt library](../README.md).
