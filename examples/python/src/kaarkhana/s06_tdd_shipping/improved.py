"""S6 improved implementation, produced by the TDD cycles in examples/end_to_end.

Money is integer cents. The country is validated at the boundary. Every rule in
the requirement has a named constant and a test.
"""

import re

DOMESTIC_COUNTRY = "DE"
DOMESTIC_FEE_CENTS = 499
FREE_SHIPPING_THRESHOLD_CENTS = 10_000
INTERNATIONAL_FEE_CENTS = 1_499

_COUNTRY = re.compile(r"[A-Z]{2}")


def shipping_fee_cents(total_cents, country):
    if isinstance(total_cents, bool) or not isinstance(total_cents, int):
        raise ValueError(f"total_cents must be an integer, got {total_cents!r}")
    if total_cents < 1:
        raise ValueError(f"total_cents must be positive, got {total_cents}")
    if not isinstance(country, str) or not _COUNTRY.fullmatch(country):
        raise ValueError(f"country must be a two letter upper case code, got {country!r}")

    if country != DOMESTIC_COUNTRY:
        return INTERNATIONAL_FEE_CENTS
    if total_cents >= FREE_SHIPPING_THRESHOLD_CENTS:
        return 0
    return DOMESTIC_FEE_CENTS
