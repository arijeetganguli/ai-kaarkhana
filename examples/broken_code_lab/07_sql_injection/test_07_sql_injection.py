import sqlite3

import pytest


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    connection.executemany("INSERT INTO users VALUES (?, ?)", [(1, "alice"), (2, "bob"), (3, "O'Brien")])
    connection.commit()
    yield connection
    connection.close()


def test_finds_a_user_by_name(target, conn):
    assert target.find_users_by_name(conn, "alice") == [(1, "alice")]


def test_names_with_an_apostrophe_work(target, conn):
    assert target.find_users_by_name(conn, "O'Brien") == [(3, "O'Brien")]


@pytest.mark.parametrize("payload", ["' OR '1'='1", "x' OR 1=1 --", "' UNION SELECT id, name FROM users --"])
def test_injection_payloads_are_treated_as_data(target, conn, payload):
    assert target.find_users_by_name(conn, payload) == []


def test_stacked_statements_cannot_destroy_data(target, conn):
    try:
        target.find_users_by_name(conn, "x'; DROP TABLE users; --")
    except Exception:
        pass  # a driver may refuse stacked statements; the table must still exist
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 3


def test_delete_removes_exactly_one_user(target, conn):
    assert target.delete_user(conn, 2) == 1
    assert [r[0] for r in conn.execute("SELECT id FROM users ORDER BY id")] == [1, 3]


@pytest.mark.parametrize("bad", ["1 OR 1=1", "2; DELETE FROM users", None, 1.5, True])
def test_delete_rejects_non_integer_ids_instead_of_building_sql_from_them(target, conn, bad):
    with pytest.raises(ValueError):
        target.delete_user(conn, bad)
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 3
