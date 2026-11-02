"""S6 initial implementation: what a one-shot generated answer often looks like.

Requirement (see examples/end_to_end/README.md):
    Domestic (DE) orders ship for 4.99 EUR, free from 100.00 EUR. International
    orders ship for a flat 14.99 EUR and are never free. The order total must be
    positive and the country must be a two letter code.

PROBLEMS
    - Ignores the country completely, so every international order is under- or
      over-charged.
    - `>` instead of `>=`: an order of exactly 100.00 pays shipping.
    - Floating point euros instead of integer cents.
    - No validation: a negative total ships for 4.99.
"""


def shipping_fee(total, country):
    if total > 100:
        return 0
    else:
        return 4.99
