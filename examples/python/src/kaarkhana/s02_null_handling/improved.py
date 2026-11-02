"""S2 improved implementation.

Requirement used in this example (stated, not invented by the code):
    - A greeting needs a customer. A missing customer is a caller error.
    - A customer with a missing or blank name is greeted as "Hello, customer".

The default for a blank name exists because the requirement says so. Without that
sentence in the requirement, the correct move is to ask, not to choose a default.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Customer:
    name: Optional[str]


def greeting(customer):
    if customer is None:
        raise ValueError("customer is required")
    name = (customer.name or "").strip()
    return f"Hello, {name}" if name else "Hello, customer"
