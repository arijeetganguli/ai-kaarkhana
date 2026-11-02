import itertools
from datetime import date

import pytest

TODAY = date(2026, 6, 15)


def coupon(expired, single_use, used):
    return {
        "expires": date(2026, 6, 14) if expired else date(2026, 6, 15),  # inclusive: today is valid
        "min_total_cents": 5_000,
        "single_use": single_use,
        "used": used,
    }


@pytest.mark.parametrize(
    "expired,big_enough,single_use,used",
    list(itertools.product([False, True], repeat=4)),
)
def test_every_combination_matches_the_rule(target, expired, big_enough, single_use, used):
    total = 5_000 if big_enough else 4_999
    expected = (not expired) and big_enough and not (single_use and used)
    assert target.is_coupon_valid(coupon(expired, single_use, used), TODAY, total) is expected


def test_expiry_date_itself_is_still_valid(target):
    assert target.is_coupon_valid(coupon(False, False, False), TODAY, 5_000) is True


def test_total_exactly_at_the_minimum_is_valid(target):
    assert target.is_coupon_valid(coupon(False, False, False), TODAY, 5_000) is True
    assert target.is_coupon_valid(coupon(False, False, False), TODAY, 4_999) is False
