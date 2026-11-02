class InsufficientFunds(Exception):
    pass


def transfer(conn, source_id, target_id, amount_cents):
    """Move money between accounts. Either both balances change or neither does."""
    if amount_cents < 1:
        raise ValueError(f"amount must be positive, got {amount_cents}")
    if source_id == target_id:
        raise ValueError("source and target must differ")

    with conn:  # one transaction: commit on success, roll back on any exception
        row = conn.execute("SELECT balance_cents FROM accounts WHERE id = ?", (source_id,)).fetchone()
        if row is None:
            raise LookupError(f"unknown source account: {source_id}")
        if row[0] < amount_cents:
            raise InsufficientFunds(f"account {source_id} has {row[0]}, needs {amount_cents}")

        conn.execute("UPDATE accounts SET balance_cents = balance_cents - ? WHERE id = ?", (amount_cents, source_id))
        cursor = conn.execute(
            "UPDATE accounts SET balance_cents = balance_cents + ? WHERE id = ?", (amount_cents, target_id)
        )
        if cursor.rowcount != 1:
            raise LookupError(f"unknown target account: {target_id}")
