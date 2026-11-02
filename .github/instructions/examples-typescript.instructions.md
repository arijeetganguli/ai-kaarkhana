---
applyTo: "examples/typescript/**/*.ts"
---

# TypeScript examples

- Source is in `src/sNN_*`, tests in `tests/*.test.ts`, using Vitest and TypeScript with `strict` enabled. Do not add dependencies.
- Keep `initial.ts` (defective, documented in its header comment) next to `improved.ts`; do not fix `initial.ts`. Tests documenting an initial defect live in a `describe` block titled "... documented defects of the initial implementation (characterisation)" or have names starting `initial defect:`.
- Assertions are exact. Avoid `toBeTruthy`, `toBeDefined` and snapshot tests as the only check.
- Run `cd examples/typescript && npm run typecheck && npm test` after any change. Do not commit `node_modules/`.
