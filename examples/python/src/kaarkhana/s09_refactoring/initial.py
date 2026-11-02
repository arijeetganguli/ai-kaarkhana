"""S9 initial implementation: order pricing with nested conditionals.

Behaviour (as implemented; confirmed by characterisation tests):
    - Tier discount: GOLD 10 percent, SILVER 5 percent, anything else 0.
    - Bulk discount when the order has 10 or more units: 5 percent for GOLD and
      SILVER, 3 percent for everyone else. Applied after the tier discount.
    - Promo code WELCOME takes 500 cents off when the undiscounted subtotal is at
      least 2000 cents. The total never goes below zero.

PROBLEM
    Four levels of nesting mix three rules. Adding a rule means editing the
    middle of this function and re-reading all of it.
"""


def price_order(items, tier, promo_code=None):
    subtotal = 0
    quantity = 0
    for unit_price_cents, qty in items:
        subtotal += unit_price_cents * qty
        quantity += qty

    total = subtotal
    if tier == "GOLD":
        total = total - total * 10 // 100
    else:
        if tier == "SILVER":
            total = total - total * 5 // 100

    if quantity >= 10:
        if tier == "GOLD" or tier == "SILVER":
            total = total - total * 5 // 100
        else:
            total = total - total * 3 // 100

    if promo_code == "WELCOME":
        if subtotal >= 2000:
            total = total - 500
            if total < 0:
                total = 0
    return total
