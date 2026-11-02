"""S2 initial implementation: greeting for a customer.

PROBLEM
    `customer` may be None (lookup miss) and `customer.name` may be None
    (incomplete profile). Both raise AttributeError deep in the call stack with
    no hint of which customer or which rule was violated.
"""


def greeting(customer):
    return "Hello, " + customer.name.strip()
