---
id: dependency-analysis
title: "Dependency Analysis"
category: development
skills: [repository-explorer, security-reviewer]
---

# Dependency Analysis

## Problem it solves

Adding or upgrading a dependency without understanding its cost, risk and blast radius.

## When to use

Before adding, upgrading or removing a library, or when asked 'what depends on this?'.

## Required context

- Dependency name and versions.
- Build files and lock files.
- Where it is used.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Analyse this dependency decision.

Dependency and proposed change:
[NAME, CURRENT VERSION, TARGET VERSION OR "NEW"]

Repository:
[ACCESS TO BUILD FILES, LOCK FILES AND SOURCE]

Report:
1. Where and how it is used in this repository (files, symbols, count). Cite the file and symbol for every claim you make about the code.
2. Transitive dependencies added or changed (from the lock file or the build tool output; run the tool if possible).
3. Breaking changes between the versions according to the project's release notes or changelog. If you cannot access them, say so rather than recalling from memory.
4. Licence and maintenance signals you can verify from the repository metadata. Mark anything unverified.
5. Alternatives including doing without it (standard library or small internal code) with trade-offs.
6. A test plan: what existing tests cover the usage and what needs adding.
7. Recommendation with the reasons and the rollback approach.
Do not state vulnerability or version facts that you did not verify.
```

## Expected AI output

- Usage inventory.
- Transitive impact.
- Verified breaking changes and licence info.
- Alternatives and recommendation.

## Validation steps

- [ ] Check version and licence facts in the official source.
- [ ] Run the dependency scanner.
- [ ] Run the full test suite on the upgrade branch.

## Related skills

- [Repository Explorer](../../skills/repository-explorer/SKILL.md)
- [Security Reviewer](../../skills/security-reviewer/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
