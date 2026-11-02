import time


class Inventory:
    """Stock of one product. `reserve` may be called from many threads."""

    def __init__(self, stock):
        self.stock = stock

    def reserve(self, qty):
        """Reserve `qty` units. Return True if reserved, False if not enough stock."""
        if self.stock >= qty:
            time.sleep(0.001)  # simulates a database round trip between check and update
            self.stock -= qty
            return True
        return False
