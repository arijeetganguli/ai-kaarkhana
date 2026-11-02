# Python examples (pytest)

Nine scenarios from the [scenario catalogue](../scenarios.md), each with `initial.py` (defective), `improved.py` (fixed) and tests. Scenario S7 has `late_fee.py` and `mutants.py` instead.

## Requirements

- Python 3.10 or newer
- pytest 8 or newer

## Run

```bash
cd examples/python
python3 -m venv .venv && source .venv/bin/activate
pip install pytest
pytest
```

Expected: all tests pass (244 at the time of writing, 0 failures). Tests that document a defect of an `initial.py` assert the *defective* behaviour on purpose, so they pass.

## Layout

| Path | Purpose |
| --- | --- |
| `src/kaarkhana/sNN_<name>/initial.py` | The defective implementation. The docstring names the problem. |
| `src/kaarkhana/sNN_<name>/improved.py` | The improved implementation. The docstring explains why. |
| `tests/test_sNN_<name>.py` | Tests of the improved code, plus `initial_defect` characterisation tests. |

| Scenario | Folder |
| --- | --- |
| S1 missing else | `s01_missing_else` |
| S2 null handling | `s02_null_handling` |
| S3 boundary | `s03_boundary` |
| S4 exception handling | `s04_exception_handling` |
| S5 boolean logic | `s05_boolean_logic` |
| S6 TDD shipping fee | `s06_tdd_shipping` (walk-through: [end_to_end](../end_to_end/README.md)) |
| S7 weak assertions and mutants | `s07_weak_assertions` |
| S8 integration (SQLite) | `s08_integration` |
| S9 refactoring | `s09_refactoring` |

## Try mutation testing for real

Scenario S7 demonstrates mutation testing with hand-written mutants. To use a tool on any module, for example [mutmut](https://mutmut.readthedocs.io/):

```bash
pip install mutmut
mutmut run --paths-to-mutate src/kaarkhana/s06_tdd_shipping/improved.py
mutmut results
```

mutmut's command line options differ between major versions. Check its documentation for the version you install.

Back to [examples](../README.md).
