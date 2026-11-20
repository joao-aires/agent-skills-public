from app.db import connect


def create(body, path=None):
    with connect(path) as connection:
        cursor = connection.execute("INSERT INTO notes (body) VALUES (?)", (body,))
        return cursor.lastrowid


def all_notes(path=None):
    with connect(path) as connection:
        return [dict(row) for row in connection.execute("SELECT id, body FROM notes ORDER BY id")]
