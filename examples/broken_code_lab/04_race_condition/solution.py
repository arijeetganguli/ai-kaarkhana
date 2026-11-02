import threading
import time


class Inventory:
    """Stock of one product. `reserve` may be called from many threads."""

    def __init__(self, stock):
        self.stock = stock
        self._lock = threading.Lock()

    def reserve(self, qty):
        """Reserve `qty` units. Return True if reserved, False if not enough stock."""
        if qty < 1:
            raise ValueError(f"qty must be at least 1, got {qty}")
        with self._lock:  # check and update are one atomic step
            if self.stock >= qty:
                time.sleep(0.001)  # simulates a database round trip
                self.stock -= qty
                return True
            return False
