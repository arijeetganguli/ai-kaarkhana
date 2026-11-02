"""S1 improved implementation.

WHY THIS IS NOT JUST "ADD AN ELSE"
    `else: return 0.0` would turn a misspelt or new tier into "no discount" and
    hide the data problem. The requirement defines exactly three tiers, so any
    other value is an invalid input and is rejected at the boundary with a
    message that names the offending value.
"""


class UnknownTier(ValueError):
    """Raised when a tier is not one of the tiers defined by the requirement."""


_RATES = {"BASIC": 0.0, "SILVER": 0.05, "GOLD": 0.10}


def discount_rate(tier):
    if not isinstance(tier, str) or tier not in _RATES:
        raise UnknownTier(f"unknown loyalty tier: {tier!r}")
    return _RATES[tier]


def price_after_discount(price_cents, tier):
    return price_cents - round(price_cents * discount_rate(tier))
