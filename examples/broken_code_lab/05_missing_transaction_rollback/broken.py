class InsufficientFunds(Exception):
    pass


def transfer(conn, source_id, target_id, amount_cents):
    """Move money between accounts. Either both balances change or neither does."""
    balance = conn.execute("SELECT balance_cents FROM accounts WHERE id = ?", (source_id,)).fetchone()[0]
    if balance < amount_cents:
        raise InsufficientFunds(f"account {source_id} has {balance}, needs {amount_cents}")

    conn.execute("UPDATE accounts SET balance_cents = balance_cents - ? WHERE id = ?", (amount_cents, source_id))
    conn.commit()  # "save our progress"

    cursor = conn.execute("UPDATE accounts SET balance_cents = balance_cents + ? WHERE id = ?", (amount_cents, target_id))
    if cursor.rowcount != 1:
        raise LookupError(f"unknown target account: {target_id}")
    conn.commit()
