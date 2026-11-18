import os
import tempfile
import unittest
from pathlib import Path

os.environ["NOTES_DATA"] = str(Path(tempfile.mkdtemp()) / "notes.json")

import notes


class NotesTests(unittest.TestCase):
    def setUp(self):
        if Path(os.environ["NOTES_DATA"]).exists():
            Path(os.environ["NOTES_DATA"]).unlink()

    def test_add_and_load(self):
        notes.add("buy milk")
        self.assertEqual(notes.load()[0]["text"], "buy milk")


if __name__ == "__main__":
    unittest.main()
