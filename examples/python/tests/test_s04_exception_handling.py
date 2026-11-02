import pytest

from kaarkhana.s04_exception_handling import improved, initial


@pytest.mark.parametrize("text,expected", [("1", 1), (" 12 ", 12), ("007", 7)])
def test_valid_quantities(text, expected):
    assert improved.parse_quantity(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "1.5", "0", "-5"])
def test_invalid_text_raises_a_specific_error(text):
    with pytest.raises(improved.InvalidQuantity):
        improved.parse_quantity(text)


def test_non_text_input_is_rejected():
    with pytest.raises(improved.InvalidQuantity, match="must be text"):
        improved.parse_quantity(None)


def test_original_error_is_preserved_as_the_cause():
    with pytest.raises(improved.InvalidQuantity) as info:
        improved.parse_quantity("abc")
    assert isinstance(info.value.__cause__, ValueError)
    assert "'abc'" in str(info.value)


# --- Documented defects of the initial implementation (characterisation) ---


def test_initial_defect_invents_zero_for_garbage_and_none():
    assert initial.parse_quantity("abc") == 0
    assert initial.parse_quantity(None) == 0


def test_initial_defect_accepts_negative_quantities():
    assert initial.parse_quantity("-5") == -5
