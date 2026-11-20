import sqlite3
from pathlib import Path

DB = Path("service.db")


def connect(path=None):
    connection = sqlite3.connect(path or DB)
    connection.row_factory = sqlite3.Row
    return connection


def init(path=None):
    with connect(path) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, body TEXT NOT NULL)"
        )
