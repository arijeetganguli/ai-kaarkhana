"""S1 initial implementation: discount rate by loyalty tier.

PROBLEM
    The if/elif chain has no final branch. An unknown tier ("PLATINUM", "gold",
    None) falls off the end and the function silently returns None. The failure
    surfaces later, far from the cause, as a TypeError in price arithmetic.
"""


def discount_rate(tier):
    if tier == "GOLD":
        return 0.10
    elif tier == "SILVER":
        return 0.05
    elif tier == "BASIC":
        return 0.0


def price_after_discount(price_cents, tier):
    return price_cents - round(price_cents * discount_rate(tier))
