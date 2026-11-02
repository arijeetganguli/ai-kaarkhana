#!/usr/bin/env python3
"""Verify the Broken Code Lab.

For every exercise folder in examples/broken_code_lab/:

  * the tests must FAIL against broken.py  (otherwise the exercise teaches nothing), and
  * the tests must PASS against solution.py (otherwise the reference fix is wrong).

Usage
    python scripts/verify_lab.py            check every exercise
    python scripts/verify_lab.py 04 07      check only the exercises whose folder starts with these prefixes

Requires pytest in the active Python environment. Exit code 0 only if every exercise behaves as expected.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT / "examples" / "broken_code_lab"
SUMMARY = re.compile(r"(\d+) (passed|failed|error|errors)")


def run_pytest(exercise, target):
    cmd = [sys.executable, "-m", "pytest", exercise.name, f"--target={target}", "-q", "-p", "no:cacheprovider"]
    proc = subprocess.run(cmd, cwd=LAB, capture_output=True, text=True, timeout=300)
    counts = {}
    for number, word in SUMMARY.findall(proc.stdout):
        counts["error" if word.startswith("error") else word] = int(number)
    return proc.returncode, counts, proc.stdout + proc.stderr


def describe(counts):
    return ", ".join(f"{n} {k}" for k, n in sorted(counts.items())) or "no tests collected"


def main(argv):
    if not LAB.is_dir():
        print(f"missing {LAB}")
        return 2
    exercises = sorted(p for p in LAB.iterdir() if p.is_dir() and re.match(r"\d\d_", p.name))
    if argv:
        exercises = [e for e in exercises if any(e.name.startswith(a) for a in argv)]
    if not exercises:
        print("no exercises selected")
        return 2

    failures = []
    for ex in exercises:
        for needed in ("broken.py", "solution.py", "CHALLENGE.md"):
            if not (ex / needed).exists():
                failures.append(f"{ex.name}: missing {needed}")
        code_b, counts_b, out_b = run_pytest(ex, "broken")
        code_s, counts_s, out_s = run_pytest(ex, "solution")

        broken_ok = code_b != 0 and counts_b.get("failed", 0) > 0 and counts_b.get("error", 0) == 0
        solution_ok = code_s == 0 and counts_s.get("passed", 0) > 0 and not counts_s.get("failed") and not counts_s.get("error")

        status = "ok " if broken_ok and solution_ok else "FAIL"
        print(f"{status} {ex.name:42s} broken: {describe(counts_b):22s} solution: {describe(counts_s)}")
        if not broken_ok:
            failures.append(f"{ex.name}: expected failing tests against broken.py (got: {describe(counts_b)}, exit {code_b})")
            if counts_b.get("error"):
                print(out_b[-1500:])
        if not solution_ok:
            failures.append(f"{ex.name}: expected all tests to pass against solution.py (got: {describe(counts_s)}, exit {code_s})")
            print(out_s[-1500:])

    if failures:
        print("\nProblems:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"\nall {len(exercises)} exercises behave as designed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
