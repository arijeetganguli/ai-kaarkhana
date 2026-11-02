def format_address(order):
    """Return 'line1, line2, postcode city' for the shipping address of an order.

    line2 is optional. An order without a shipping address cannot be formatted.
    """
    address = order["shipping"]["address"]
    parts = [address["line1"].strip(), address["line2"].strip(), address["postcode"] + " " + address["city"]]
    return ", ".join(parts)
