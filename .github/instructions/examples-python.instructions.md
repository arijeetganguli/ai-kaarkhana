---
applyTo: "examples/python/**/*.py,examples/broken_code_lab/**/*.py"
---

# Python examples and the Broken Code Lab

- Each scenario has `initial.py` (the defective version, documented in its docstring) and `improved.py`. Do not "fix" `initial.py`; its defects are the exercise. Tests that document an initial defect are named `test_initial_defect_...`.
- Tests use pytest with exact assertions. Run `cd examples/python && pytest` after any change.
- Broken Code Lab: every exercise has `broken.py`, `solution.py`, a test file and `CHALLENGE.md`. The tests must **fail** against `broken.py` and **pass** with `--target=solution`. Verify with `python scripts/verify_lab.py`.
- Money is integer cents. No sleeping in tests except where the exercise models a race, and then keep the delay short.
- Standard library plus pytest only. Do not add dependencies.
