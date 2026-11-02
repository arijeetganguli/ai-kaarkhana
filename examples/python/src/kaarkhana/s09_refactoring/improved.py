"""S9 refactored implementation: same behaviour, one rule per function.

Refactoring steps (each verified by the characterisation tests):
    1. Extract `_subtotal_and_quantity`.
    2. Extract `_tier_percent` and `_bulk_percent`, replacing the nested ifs.
    3. Extract `_percent_off` to remove three copies of the same arithmetic.
    4. Extract `_apply_promo`.

Behaviour, including quirks, is unchanged. One quirk is deliberately preserved:
an unknown tier is treated as "no tier" instead of being rejected. That is a
decision for the business owner, not part of a refactoring.
"""

_TIER_PERCENT = {"GOLD": 10, "SILVER": 5}
_BULK_THRESHOLD = 10
_PREMIUM_BULK_PERCENT = 5
_STANDARD_BULK_PERCENT = 3
_PROMO_CODE = "WELCOME"
_PROMO_MINIMUM_SUBTOTAL = 2000
_PROMO_OFF = 500


def _subtotal_and_quantity(items):
    subtotal = sum(price * qty for price, qty in items)
    quantity = sum(qty for _, qty in items)
    return subtotal, quantity


def _tier_percent(tier):
    return _TIER_PERCENT.get(tier, 0)


def _bulk_percent(tier, quantity):
    if quantity < _BULK_THRESHOLD:
        return 0
    return _PREMIUM_BULK_PERCENT if tier in _TIER_PERCENT else _STANDARD_BULK_PERCENT


def _percent_off(amount, percent):
    return amount - amount * percent // 100


def _apply_promo(total, subtotal, promo_code):
    if promo_code == _PROMO_CODE and subtotal >= _PROMO_MINIMUM_SUBTOTAL:
        return max(total - _PROMO_OFF, 0)
    return total


def price_order(items, tier, promo_code=None):
    subtotal, quantity = _subtotal_and_quantity(items)
    total = _percent_off(subtotal, _tier_percent(tier))
    total = _percent_off(total, _bulk_percent(tier, quantity))
    return _apply_promo(total, subtotal, promo_code)
