"""S7 code under test: late fee for a returned item.

Requirement:
    - The first 3 days late are a grace period: no fee.
    - From day 4 the fee is 50 cents per day beyond the grace period.
    - The fee never exceeds 2000 cents.
"""

GRACE_DAYS = 3
RATE_CENTS_PER_DAY = 50
CAP_CENTS = 2_000


def late_fee_cents(days_late):
    if days_late <= GRACE_DAYS:
        return 0
    return min((days_late - GRACE_DAYS) * RATE_CENTS_PER_DAY, CAP_CENTS)
