"""S4 initial implementation: parse an order quantity from user input.

PROBLEM
    `except Exception: return 0` swallows every failure and invents a value.
    "abc" and None become quantity 0, the original error is lost, and "-5" is
    accepted because nothing checks the range.
"""


def parse_quantity(text):
    try:
        return int(text)
    except Exception:
        return 0
