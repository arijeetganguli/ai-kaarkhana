class OrderRepository:
    """Reads order totals for a customer from the `orders` table."""

    def __init__(self, conn):
        self._conn = conn

    def total_spent_cents(self, customer_id):
        """Sum of `total_cents` of all PAID orders of the customer; 0 when there are none."""
        row = self._conn.execute(
            "SELECT SUM(total_cents) FROM orders WHERE id = ? AND status = 'PAID'",
            (customer_id,),
        ).fetchone()
        return row[0]
