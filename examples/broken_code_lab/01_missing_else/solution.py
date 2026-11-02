class UnsupportedWeight(ValueError):
    pass


def size_class(weight_kg):
    """Return the parcel size class: S up to 2 kg, M up to 10 kg, L up to 30 kg.

    Parcels over 30 kg and non-positive or non-numeric weights are rejected.
    """
    if isinstance(weight_kg, bool) or not isinstance(weight_kg, (int, float)):
        raise UnsupportedWeight(f"weight must be a number, got {weight_kg!r}")
    if weight_kg <= 0:
        raise UnsupportedWeight(f"weight must be positive, got {weight_kg}")
    if weight_kg <= 2:
        return "S"
    if weight_kg <= 10:
        return "M"
    if weight_kg <= 30:
        return "L"
    raise UnsupportedWeight(f"too heavy for the parcel service: {weight_kg} kg (maximum 30 kg)")
