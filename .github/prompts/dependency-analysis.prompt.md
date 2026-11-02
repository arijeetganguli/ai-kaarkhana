---
description: "Dependency Analysis: Adding or upgrading a dependency without understanding its cost, risk and blast radius."
---
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

---
Generated from [prompts/development/dependency-analysis.md](../../prompts/development/dependency-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
