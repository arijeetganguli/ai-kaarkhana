from types import SimpleNamespace

import pytest

from kaarkhana.s02_null_handling import improved, initial


def test_greets_by_trimmed_name():
    assert improved.greeting(improved.Customer("  Asha ")) == "Hello, Asha"


@pytest.mark.parametrize("name", [None, "", "   "])
def test_missing_or_blank_name_uses_the_specified_default(name):
    assert improved.greeting(improved.Customer(name)) == "Hello, customer"


def test_missing_customer_is_rejected_explicitly():
    with pytest.raises(ValueError, match="customer is required"):
        improved.greeting(None)


# --- Documented defects of the initial implementation (characterisation) ---


def test_initial_defect_missing_customer_raises_attribute_error():
    with pytest.raises(AttributeError):
        initial.greeting(None)


def test_initial_defect_missing_name_raises_attribute_error():
    with pytest.raises(AttributeError):
        initial.greeting(SimpleNamespace(name=None))
