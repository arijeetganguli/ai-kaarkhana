import pytest


@pytest.mark.parametrize(
    "weight,expected",
    [(0.1, "S"), (2, "S"), (2.01, "M"), (10, "M"), (10.01, "L"), (30, "L")],
)
def test_size_classes_at_and_around_every_boundary(target, weight, expected):
    assert target.size_class(weight) == expected


@pytest.mark.parametrize("weight", [30.01, 31, 500])
def test_parcels_over_30_kg_are_rejected_not_ignored(target, weight):
    with pytest.raises(ValueError, match="too heavy"):
        target.size_class(weight)


@pytest.mark.parametrize("weight", [0, -1, None, "5", True])
def test_invalid_weights_are_rejected(target, weight):
    with pytest.raises(ValueError):
        target.size_class(weight)
