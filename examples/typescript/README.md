# TypeScript examples (Vitest)

Nine scenarios from the [scenario catalogue](../scenarios.md). Each has `initial.ts` (defective) and `improved.ts` (fixed) plus a Vitest file. S7 has `lateFee.ts` and `mutants.ts`.

## Requirements

- Node.js 20 or newer
- npm

## Run

```bash
cd examples/typescript
npm ci          # or: npm install
npm run typecheck
npm test
```

Expected: `tsc` reports no errors and all tests pass (103 at the time of writing). S8 starts a local HTTP server on an ephemeral port.

## Layout

| Path | Purpose |
| --- | --- |
| `src/sNN_<name>/initial.ts` | The defective implementation. The comment names the problem. |
| `src/sNN_<name>/improved.ts` | The improved implementation. |
| `tests/sNN_<name>.test.ts` | Tests of the improved code plus a `describe` block with characterisation tests of the defects. |

| Scenario | Folder |
| --- | --- |
| S1 missing else | `s01_missing_else` |
| S2 null handling | `s02_null_handling` |
| S3 boundary | `s03_boundary` |
| S4 exception handling | `s04_exception_handling` |
| S5 boolean logic | `s05_boolean_logic` |
| S6 TDD shipping fee | `s06_tdd_shipping` |
| S7 weak assertions and mutants | `s07_weak_assertions` |
| S8 integration (HTTP) | `s08_integration` |
| S9 refactoring | `s09_refactoring` |

## Try mutation testing for real

[Stryker](https://stryker-mutator.io) supports Vitest through `@stryker-mutator/vitest-runner`. Follow the Stryker documentation to initialise it for your Stryker version (`npm init stryker`) and run it on one scenario folder at a time.

Back to [examples](../README.md).
