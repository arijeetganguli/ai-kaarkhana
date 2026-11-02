"""S8 initial implementation: order repository on SQLite.

PROBLEM
    The SQL selects `id, total_cents, status` but the mapping reads the columns
    as `id, status, total_cents`. A unit test with a mocked connection encodes
    the same wrong belief, so it passes. Only a real database exposes it.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    id: int
    total_cents: int
    status: str


class OrderRepository:
    def __init__(self, conn):
        self._conn = conn

    def find_by_customer(self, customer_id):
        rows = self._conn.execute(
            "SELECT id, total_cents, status FROM orders WHERE customer_id = ?",
            (customer_id,),
        ).fetchall()
        return [Order(id=r[0], status=r[1], total_cents=r[2]) for r in rows]
