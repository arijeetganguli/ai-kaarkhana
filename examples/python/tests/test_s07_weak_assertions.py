"""S7: line coverage is 100 percent for both suites; only one of them is any good."""

from kaarkhana.s07_weak_assertions.late_fee import late_fee_cents
from kaarkhana.s07_weak_assertions.mutants import MUTANTS


# --- The weak suite: executes every line, asserts almost nothing -----------
def weak_suite(fn):
    assert fn(10) > 0
    assert fn(0) >= 0
    assert fn(1000) > 0


# --- The strong suite: exact values on both sides of every rule ------------
def strong_suite(fn):
    assert fn(0) == 0
    assert fn(3) == 0  # last grace day
    assert fn(4) == 50  # first charged day
    assert fn(10) == 350  # 7 days * 50
    assert fn(43) == 2_000  # exactly reaches the cap
    assert fn(44) == 2_000  # would be 2050 without the cap
    assert fn(1000) == 2_000


def survivors(suite):
    alive = []
    for name, mutant in MUTANTS.items():
        try:
            suite(mutant)
        except AssertionError:
            continue  # the suite noticed: mutant killed
        alive.append(name)
    return alive


def test_both_suites_pass_on_the_original_code():
    weak_suite(late_fee_cents)
    strong_suite(late_fee_cents)


def test_weak_suite_lets_every_mutant_survive():
    assert survivors(weak_suite) == list(MUTANTS)


def test_strong_suite_kills_every_mutant():
    assert survivors(strong_suite) == []
