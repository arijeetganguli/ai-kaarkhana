"""Shared pytest setup for the Broken Code Lab.

Every exercise directory contains `broken.py` (the defective code you fix) and
`solution.py` (a reference fix). The tests run against `broken.py` by default;
CI runs them against `solution.py`:

    pytest examples/broken_code_lab                     # your work: starts red
    pytest examples/broken_code_lab --target=solution   # reference: must be green
"""

import importlib.util
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--target",
        action="store",
        default="broken",
        choices=["broken", "solution"],
        help="which module of each exercise to test (default: broken)",
    )


@pytest.fixture
def target(request):
    which = request.config.getoption("--target")
    exercise_dir = Path(request.node.fspath).parent
    path = exercise_dir / f"{which}.py"
    spec = importlib.util.spec_from_file_location(f"lab_{exercise_dir.name}_{which}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
