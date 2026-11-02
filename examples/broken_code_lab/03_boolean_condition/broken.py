from datetime import date


def is_coupon_valid(coupon, today, cart_total_cents):
    """A coupon is valid when ALL of the following hold:

    - it has not expired (valid through `expires`, inclusive),
    - the cart total reaches `min_total_cents`,
    - and it is not single use, or it has not been used yet.
    """
    expired = today > coupon["expires"]
    return not expired and cart_total_cents >= coupon["min_total_cents"] or not coupon["single_use"] or not coupon["used"]
