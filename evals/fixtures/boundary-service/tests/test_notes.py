import tempfile
import unittest
from pathlib import Path

from app import db
from app.notes import all_notes, create
from app.search import search


class NoteTests(unittest.TestCase):
    def setUp(self):
        self.path = str(Path(tempfile.mkdtemp()) / "service.db")
        db.init(self.path)

    def test_create_and_search(self):
        create("queue export", self.path)
        self.assertEqual(len(all_notes(self.path)), 1)
        self.assertEqual(search("export", self.path)[0]["body"], "queue export")


if __name__ == "__main__":
    unittest.main()
