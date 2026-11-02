def find_users_by_name(conn, name):
    """Return the (id, name) rows of users whose name equals `name`."""
    return conn.execute("SELECT id, name FROM users WHERE name = ?", (name,)).fetchall()


def delete_user(conn, user_id):
    """Delete one user by id. Return the number of deleted rows."""
    if isinstance(user_id, bool) or not isinstance(user_id, int):
        raise ValueError(f"user_id must be an integer, got {user_id!r}")
    cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return cursor.rowcount
