import sqlite3
from unittest.mock import MagicMock

import pytest

from kaarkhana.s08_integration import improved, initial


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, "
        "total_cents INTEGER NOT NULL, status TEXT NOT NULL)"
    )
    connection.executemany(
        "INSERT INTO orders (id, customer_id, total_cents, status) VALUES (?, ?, ?, ?)",
        [(2, 7, 2500, "SHIPPED"), (1, 7, 1500, "PAID"), (3, 8, 999, "PAID")],
    )
    connection.commit()
    yield connection
    connection.close()


# --- Why the mocked unit test is not enough --------------------------------
def test_unit_test_with_mocked_connection_passes_even_though_the_mapping_is_wrong():
    mock_conn = MagicMock()
    # The test author wrote the rows in the order the (wrong) code reads them.
    mock_conn.execute.return_value.fetchall.return_value = [(1, "PAID", 1500)]
    orders = initial.OrderRepository(mock_conn).find_by_customer(7)
    assert orders == [initial.Order(id=1, total_cents=1500, status="PAID")]


def test_initial_defect_real_database_exposes_the_swapped_columns(conn):
    orders = initial.OrderRepository(conn).find_by_customer(7)
    assert {o.status for o in orders} == {1500, 2500}  # numbers where statuses belong
    assert {o.total_cents for o in orders} == {"PAID", "SHIPPED"}  # statuses where numbers belong


# --- Integration tests of the improved repository --------------------------
def test_returns_the_customers_orders_with_correct_fields_in_id_order(conn):
    orders = improved.OrderRepository(conn).find_by_customer(7)
    assert orders == [
        improved.Order(id=1, total_cents=1500, status="PAID"),
        improved.Order(id=2, total_cents=2500, status="SHIPPED"),
    ]


def test_other_customers_orders_are_not_returned(conn):
    orders = improved.OrderRepository(conn).find_by_customer(8)
    assert [o.id for o in orders] == [3]


def test_unknown_customer_has_no_orders(conn):
    assert improved.OrderRepository(conn).find_by_customer(404) == []


def test_sql_metacharacters_in_the_customer_id_are_treated_as_data(conn):
    assert improved.OrderRepository(conn).find_by_customer("7 OR 1=1") == []
