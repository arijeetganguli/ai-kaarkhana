import pytest


def order(**address):
    base = {"line1": "Hauptstr. 1", "line2": None, "postcode": "10115", "city": "Berlin"}
    base.update(address)
    return {"shipping": {"address": base}}


def test_formats_a_full_address(target):
    assert target.format_address(order(line2=" Hinterhaus ")) == "Hauptstr. 1, Hinterhaus, 10115 Berlin"


@pytest.mark.parametrize("line2", [None, "", "   "])
def test_line2_is_optional_and_skipped_when_empty(target, line2):
    assert target.format_address(order(line2=line2)) == "Hauptstr. 1, 10115 Berlin"


def test_missing_line2_key_is_allowed(target):
    o = order()
    del o["shipping"]["address"]["line2"]
    assert target.format_address(o) == "Hauptstr. 1, 10115 Berlin"


@pytest.mark.parametrize("bad", [None, {}, {"shipping": None}, {"shipping": {}}, {"shipping": {"address": None}}])
def test_missing_shipping_address_is_a_clear_error(target, bad):
    with pytest.raises(ValueError, match="shipping address is required"):
        target.format_address(bad)


@pytest.mark.parametrize("field", ["line1", "postcode", "city"])
@pytest.mark.parametrize("value", [None, "", "  "])
def test_required_fields_are_validated_with_their_name(target, field, value):
    with pytest.raises(ValueError, match=field):
        target.format_address(order(**{field: value}))
