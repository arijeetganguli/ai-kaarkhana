def format_address(order):
    """Return 'line1, line2, postcode city' for the shipping address of an order.

    line2 is optional. An order without a shipping address cannot be formatted.
    """
    shipping = (order or {}).get("shipping") or {}
    address = shipping.get("address")
    if not address:
        raise ValueError("shipping address is required")

    for field in ("line1", "postcode", "city"):
        if not (address.get(field) or "").strip():
            raise ValueError(f"shipping address field is required: {field}")

    parts = [address["line1"].strip()]
    line2 = (address.get("line2") or "").strip()
    if line2:
        parts.append(line2)
    parts.append(f"{address['postcode'].strip()} {address['city'].strip()}")
    return ", ".join(parts)
