import pytest

from kaarkhana.s01_missing_else import improved, initial


@pytest.mark.parametrize("tier,rate", [("BASIC", 0.0), ("SILVER", 0.05), ("GOLD", 0.10)])
def test_known_tiers_have_their_documented_rate(tier, rate):
    assert improved.discount_rate(tier) == rate


@pytest.mark.parametrize("bad", ["PLATINUM", "gold", "", " GOLD", None, 7])
def test_unknown_tier_is_rejected_with_the_value_in_the_message(bad):
    with pytest.raises(improved.UnknownTier, match="unknown loyalty tier"):
        improved.discount_rate(bad)


def test_price_after_discount_applies_the_tier_rate():
    assert improved.price_after_discount(10_000, "GOLD") == 9_000
    assert improved.price_after_discount(10_000, "SILVER") == 9_500
    assert improved.price_after_discount(10_000, "BASIC") == 10_000


def test_unknown_tier_never_reaches_price_arithmetic():
    with pytest.raises(improved.UnknownTier):
        improved.price_after_discount(10_000, "PLATINUM")


# --- Documented defects of the initial implementation (characterisation) ---


def test_initial_defect_returns_none_for_unknown_tier():
    assert initial.discount_rate("PLATINUM") is None


def test_initial_defect_fails_far_from_the_cause():
    with pytest.raises(TypeError):
        initial.price_after_discount(10_000, "PLATINUM")
