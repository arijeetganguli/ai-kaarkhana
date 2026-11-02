import pytest

from kaarkhana.s06_tdd_shipping import improved, initial

fee = improved.shipping_fee_cents


# SC-01 .. SC-03: domestic fee and the free shipping boundary
def test_domestic_order_below_threshold_pays_standard_fee():
    assert fee(9_999, "DE") == 499


def test_domestic_order_at_threshold_ships_free():
    assert fee(10_000, "DE") == 0


def test_domestic_order_above_threshold_ships_free():
    assert fee(10_001, "DE") == 0


# SC-04 .. SC-05: international orders are never free
def test_international_order_pays_flat_fee():
    assert fee(5_000, "FR") == 1_499


def test_international_order_never_ships_free_even_far_above_threshold():
    assert fee(1_000_000, "US") == 1_499


# SC-06 .. SC-07: smallest valid order and invalid totals
def test_smallest_valid_total_is_accepted():
    assert fee(1, "DE") == 499


@pytest.mark.parametrize("bad", [0, -1, -10_000])
def test_non_positive_totals_are_rejected(bad):
    with pytest.raises(ValueError, match="positive"):
        fee(bad, "DE")


@pytest.mark.parametrize("bad", [100.0, "100", None, True])
def test_non_integer_totals_are_rejected(bad):
    with pytest.raises(ValueError, match="integer"):
        fee(bad, "DE")


# SC-08: invalid country codes
@pytest.mark.parametrize("bad", ["", "D", "DEU", "de", "D1", None, 49])
def test_invalid_country_codes_are_rejected(bad):
    with pytest.raises(ValueError, match="country"):
        fee(5_000, bad)


# --- Documented defects of the initial implementation (characterisation) ---


def test_initial_defect_charges_shipping_at_exactly_the_threshold():
    assert initial.shipping_fee(100, "DE") == 4.99  # should be free


def test_initial_defect_ignores_country():
    assert initial.shipping_fee(5, "US") == 4.99  # should be 14.99


def test_initial_defect_accepts_negative_totals():
    assert initial.shipping_fee(-50, "DE") == 4.99
