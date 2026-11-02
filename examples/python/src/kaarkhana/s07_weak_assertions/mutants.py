"""Hand-written mutants of `late_fee_cents`.

Each function is the original with exactly one small change, the kind of change
a mutation testing tool (PIT, Stryker, mutmut) generates automatically. A test
suite that cannot tell a mutant from the original has a gap.
"""

from .late_fee import CAP_CENTS, GRACE_DAYS, RATE_CENTS_PER_DAY


def m1_grace_boundary_shifted(days_late):  # `<= 3` became `<= 4`
    if days_late <= GRACE_DAYS + 1:
        return 0
    return min((days_late - GRACE_DAYS) * RATE_CENTS_PER_DAY, CAP_CENTS)


def m2_off_by_one_day(days_late):  # `days - 3` became `days - 2`
    if days_late <= GRACE_DAYS:
        return 0
    return min((days_late - GRACE_DAYS + 1) * RATE_CENTS_PER_DAY, CAP_CENTS)


def m3_rate_changed(days_late):  # 50 became 51
    if days_late <= GRACE_DAYS:
        return 0
    return min((days_late - GRACE_DAYS) * (RATE_CENTS_PER_DAY + 1), CAP_CENTS)


def m4_cap_changed(days_late):  # 2000 became 2001
    if days_late <= GRACE_DAYS:
        return 0
    return min((days_late - GRACE_DAYS) * RATE_CENTS_PER_DAY, CAP_CENTS + 1)


def m5_cap_removed(days_late):  # `min(..., cap)` removed
    if days_late <= GRACE_DAYS:
        return 0
    return (days_late - GRACE_DAYS) * RATE_CENTS_PER_DAY


MUTANTS = {
    "m1_grace_boundary_shifted": m1_grace_boundary_shifted,
    "m2_off_by_one_day": m2_off_by_one_day,
    "m3_rate_changed": m3_rate_changed,
    "m4_cap_changed": m4_cap_changed,
    "m5_cap_removed": m5_cap_removed,
}

# Not in MUTANTS on purpose: changing `days_late <= 3` to `days_late < 3`
# changes the result only for days_late == 3, where both branches return 0
# ((3 - 3) * 50). It is an *equivalent mutant*: no test can ever kill it.
