def is_coupon_valid(coupon, today, cart_total_cents):
    """A coupon is valid when ALL of the following hold:

    - it has not expired (valid through `expires`, inclusive),
    - the cart total reaches `min_total_cents`,
    - and it is not single use, or it has not been used yet.
    """
    not_expired = today <= coupon["expires"]
    big_enough = cart_total_cents >= coupon["min_total_cents"]
    still_usable = not (coupon["single_use"] and coupon["used"])
    return not_expired and big_enough and still_usable
