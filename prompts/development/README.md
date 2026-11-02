# Development prompts

Plan and change code safely: exploration, planning, generation, modification, refactoring and defensive coding.

Each prompt lists the problem it solves, when to use it, the context to prepare, a copy-ready prompt, the output to expect and how to validate that output.

| Prompt | Problem it solves | Skills |
| --- | --- | --- |
| [Repository Exploration](repository-exploration.md) | You must change code you do not know, and the assistant is guessing at structure and conventions. | [repository-explorer](../../skills/repository-explorer/SKILL.md) |
| [Implementation Planning](implementation-planning.md) | Large AI edits are hard to review and break things because nothing was planned in small steps. | [implementation-planner](../../skills/implementation-planner/SKILL.md), [repository-explorer](../../skills/repository-explorer/SKILL.md) |
| [Code Generation From a Plan](code-generation.md) | Generated code ignores the plan, over-builds and arrives without evidence that it works. | [tdd-engineer](../../skills/tdd-engineer/SKILL.md), [implementation-planner](../../skills/implementation-planner/SKILL.md) |
| [Existing Code Modification](existing-code-modification.md) | Changing legacy code without understanding its current behaviour causes regressions. | [regression-analyst](../../skills/regression-analyst/SKILL.md), [tdd-engineer](../../skills/tdd-engineer/SKILL.md) |
| [Behaviour Preserving Refactoring](refactoring.md) | Refactoring requests turn into rewrites that change behaviour. | [refactoring-specialist](../../skills/refactoring-specialist/SKILL.md), [regression-analyst](../../skills/regression-analyst/SKILL.md) |
| [Defensive Coding Pass](defensive-coding.md) | Code handles the happy path only and fails unpredictably on missing data, bad input or dependency failure. | [defensive-programming-reviewer](../../skills/defensive-programming-reviewer/SKILL.md), [edge-case-hunter](../../skills/edge-case-hunter/SKILL.md) |
| [Dependency Analysis](dependency-analysis.md) | Adding or upgrading a dependency without understanding its cost, risk and blast radius. | [repository-explorer](../../skills/repository-explorer/SKILL.md), [security-reviewer](../../skills/security-reviewer/SKILL.md) |
| [Documentation Update](documentation-update.md) | Documentation lags the code, or is AI-written with invented behaviour. | [documentation-engineer](../../skills/documentation-engineer/SKILL.md) |

Related handbook chapter: [Chapter 8: Architecture and Design](../../handbook/08_architecture_and_design/README.md)

Back to the [prompt library](../README.md).
