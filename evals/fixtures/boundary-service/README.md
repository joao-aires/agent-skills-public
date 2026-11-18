# Search service

Two components share one SQLite database: `app/notes.py` writes notes, `app/search.py`
reads them. `notes` is the current table. Tests: `python3 -m unittest -q`.
