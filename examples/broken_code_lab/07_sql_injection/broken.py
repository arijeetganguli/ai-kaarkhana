def find_users_by_name(conn, name):
    """Return the (id, name) rows of users whose name equals `name`."""
    query = "SELECT id, name FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()


def delete_user(conn, user_id):
    """Delete one user by id. Return the number of deleted rows."""
    cursor = conn.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()
    return cursor.rowcount
