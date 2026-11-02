"""S4 improved implementation.

Requirement: a quantity is a whole number of at least 1.

Invalid input raises a specific, documented error that names the input and keeps
the original exception as the cause, so logs and callers can tell what happened.
"""


class InvalidQuantity(ValueError):
    """Raised for text that is not a valid order quantity."""


def parse_quantity(text):
    if not isinstance(text, str):
        raise InvalidQuantity(f"quantity must be text, got {type(text).__name__}")
    try:
        value = int(text.strip())
    except ValueError as exc:
        raise InvalidQuantity(f"not a whole number: {text!r}") from exc
    if value < 1:
        raise InvalidQuantity(f"quantity must be at least 1, got {value}")
    return value
