import pytest

from kaarkhana.s03_boundary import improved, initial


@pytest.mark.parametrize("age,expected", [(0, False), (64, False), (65, True), (66, True), (100, True)])
def test_eligibility_below_at_and_above_the_boundary(age, expected):
    assert improved.is_senior(age) is expected


@pytest.mark.parametrize("bad", [-1, "65", 65.0, None, True])
def test_invalid_ages_are_rejected(bad):
    with pytest.raises(ValueError):
        improved.is_senior(bad)


# --- Documented defect of the initial implementation (characterisation) ---


def test_initial_defect_excludes_exactly_65():
    assert initial.is_senior(65) is False  # requirement says 65 is eligible
    assert initial.is_senior(66) is True
