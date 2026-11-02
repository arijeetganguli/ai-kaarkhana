"""The unit test below passes against both versions. Only the integration tests notice the bugs."""

import sqlite3
from unittest.mock import MagicMock

import pytest


def test_unit_test_with_a_mocked_connection_passes_even_for_the_broken_query(target):
    conn = MagicMock()
    conn.execute.return_value.fetchone.return_value = (4_000,)
    assert target.OrderRepository(conn).total_spent_cents(7) == 4_000  # tests the mock, not the SQL


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, "
        "total_cents INTEGER NOT NULL, status TEXT NOT NULL)"
    )
    connection.executemany(
        "INSERT INTO orders (id, customer_id, total_cents, status) VALUES (?, ?, ?, ?)",
        [
            (1, 7, 1_500, "PAID"),
            (2, 7, 2_500, "PAID"),
            (3, 7, 9_900, "CANCELLED"),
            (4, 8, 700, "PAID"),
            (7, 9, 123, "PAID"),  # order id 7 belongs to customer 9: catches `WHERE id = ?`
        ],
    )
    connection.commit()
    yield connection
    connection.close()


def test_sums_only_paid_orders_of_that_customer(target, conn):
    assert target.OrderRepository(conn).total_spent_cents(7) == 4_000


def test_customer_without_orders_has_zero_not_none(target, conn):
    assert target.OrderRepository(conn).total_spent_cents(404) == 0


def test_cancelled_orders_are_excluded(target, conn):
    conn.execute("DELETE FROM orders WHERE status = 'PAID' AND customer_id = 7")
    assert target.OrderRepository(conn).total_spent_cents(7) == 0
