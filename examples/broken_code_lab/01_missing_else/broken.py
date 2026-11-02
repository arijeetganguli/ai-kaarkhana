def size_class(weight_kg):
    """Return the parcel size class: S up to 2 kg, M up to 10 kg, L up to 30 kg."""
    if weight_kg <= 2:
        return "S"
    elif weight_kg <= 10:
        return "M"
    elif weight_kg <= 30:
        return "L"
