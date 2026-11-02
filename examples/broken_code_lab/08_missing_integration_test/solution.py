class OrderRepository:
    """Reads order totals for a customer from the `orders` table."""

    def __init__(self, conn):
        self._conn = conn

    def total_spent_cents(self, customer_id):
        """Sum of `total_cents` of all PAID orders of the customer; 0 when there are none."""
        row = self._conn.execute(
            "SELECT COALESCE(SUM(total_cents), 0) FROM orders WHERE customer_id = ? AND status = 'PAID'",
            (customer_id,),
        ).fetchone()
        return row[0]
