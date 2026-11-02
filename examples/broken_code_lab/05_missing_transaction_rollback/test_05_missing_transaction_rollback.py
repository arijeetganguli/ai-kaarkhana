import sqlite3

import pytest


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance_cents INTEGER NOT NULL)")
    connection.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 10_000), (2, 500)])
    connection.commit()
    yield connection
    connection.close()


def balances(conn):
    return dict(conn.execute("SELECT id, balance_cents FROM accounts").fetchall())


def test_successful_transfer_moves_the_money(target, conn):
    target.transfer(conn, 1, 2, 2_500)
    assert balances(conn) == {1: 7_500, 2: 3_000}


def test_insufficient_funds_changes_nothing(target, conn):
    with pytest.raises(target.InsufficientFunds):
        target.transfer(conn, 2, 1, 501)
    assert balances(conn) == {1: 10_000, 2: 500}


def test_unknown_target_account_must_not_lose_the_debit(target, conn):
    with pytest.raises(LookupError):
        target.transfer(conn, 1, 999, 2_500)
    assert balances(conn) == {1: 10_000, 2: 500}, "the debit must be rolled back"


def test_unknown_target_does_not_leave_a_half_done_transaction_visible_to_others(target, conn, tmp_path):
    # A second connection must never observe the intermediate state either.
    db = tmp_path / "bank.db"
    first = sqlite3.connect(db)
    first.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance_cents INTEGER NOT NULL)")
    first.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 10_000), (2, 500)])
    first.commit()
    with pytest.raises(LookupError):
        target.transfer(first, 1, 999, 2_500)
    second = sqlite3.connect(db)
    assert balances(second) == {1: 10_000, 2: 500}
    first.close()
    second.close()


@pytest.mark.parametrize("amount", [0, -5])
def test_non_positive_amounts_are_rejected(target, conn, amount):
    with pytest.raises(ValueError):
        target.transfer(conn, 1, 2, amount)
    assert balances(conn) == {1: 10_000, 2: 500}
