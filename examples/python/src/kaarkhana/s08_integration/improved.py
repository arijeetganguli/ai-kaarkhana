"""S8 improved implementation: columns are read by name and the result is ordered."""

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    id: int
    total_cents: int
    status: str


class OrderRepository:
    def __init__(self, conn):
        conn.row_factory = sqlite3.Row
        self._conn = conn

    def find_by_customer(self, customer_id):
        rows = self._conn.execute(
            "SELECT id, total_cents, status FROM orders WHERE customer_id = ? ORDER BY id",
            (customer_id,),
        ).fetchall()
        return [Order(id=r["id"], total_cents=r["total_cents"], status=r["status"]) for r in rows]
