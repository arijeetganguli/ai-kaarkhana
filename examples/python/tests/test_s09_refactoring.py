import itertools

import pytest

from kaarkhana.s09_refactoring import improved, initial

TIERS = ["GOLD", "SILVER", "BASIC", None, "UNKNOWN"]
PROMOS = [None, "WELCOME", "OTHER"]
CARTS = [
    [],
    [(100, 1)],
    [(1999, 1)],
    [(2000, 1)],
    [(500, 4)],
    [(100, 9)],
    [(100, 10)],
    [(333, 3), (101, 7)],
    [(10_000, 12)],
    [(1, 1)],
]


@pytest.mark.parametrize("tier,promo,cart", list(itertools.product(TIERS, PROMOS, CARTS)))
def test_refactoring_preserves_behaviour_over_the_whole_grid(tier, promo, cart):
    assert improved.price_order(cart, tier, promo) == initial.price_order(cart, tier, promo)


# Characterisation tests: written first, run against the initial code, then kept.
@pytest.mark.parametrize(
    "cart,tier,promo,expected",
    [
        ([(1000, 2)], "GOLD", None, 1800),
        ([(1000, 2)], "SILVER", None, 1900),
        ([(1000, 2)], "BASIC", None, 2000),
        ([(100, 10)], "BASIC", None, 970),
        ([(100, 10)], "GOLD", None, 855),
        ([(1000, 2)], "BASIC", "WELCOME", 1500),
        ([(900, 2)], "BASIC", "WELCOME", 1800),  # subtotal 1800 < 2000: promo not applied
        ([(1000, 2)], "GOLD", "WELCOME", 1300),
        ([], "GOLD", "WELCOME", 0),
    ],
)
def test_characterisation_of_current_behaviour(cart, tier, promo, expected):
    got = initial.price_order(cart, tier, promo)
    assert got == improved.price_order(cart, tier, promo)
    assert got == expected


def test_quirk_unknown_tier_is_treated_as_no_tier():
    assert improved.price_order([(1000, 2)], "PLATINUM") == improved.price_order([(1000, 2)], "BASIC")
