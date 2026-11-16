"""Tests for the JSON note storage layer."""

import json
import re
import tempfile
import unittest
from pathlib import Path

from notes_app.errors import DataError, InputError, NoteNotFound
from notes_app.storage import (
    NoteStore,
    default_data_path,
    resolve_data_path,
)


class NoteStoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.path = Path(self.temporary_directory.name) / "notes.json"
        self.store = NoteStore(self.path)

    def test_missing_file_loads_as_empty_notebook(self):
        self.assertEqual(self.store.load(), [])

    def test_zero_byte_file_loads_as_empty_notebook(self):
        self.path.write_text("", encoding="utf-8")
        self.assertEqual(self.store.load(), [])

    def test_add_persists_note_and_advances_next_id(self):
        first = self.store.add("Buy milk")
        second = self.store.add("Call the dentist")

        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)
        self.assertRegex(
            first.created_at,
            re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"),
        )

        payload = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(payload["version"], 1)
        self.assertEqual(payload["next_id"], 3)
        self.assertEqual(
            [note["text"] for note in payload["notes"]],
            ["Buy milk", "Call the dentist"],
        )

        reloaded = NoteStore(self.path).load()
        self.assertEqual([note.text for note in reloaded], ["Buy milk", "Call the dentist"])

    def test_outer_whitespace_is_preserved(self):
        self.store.add("  padded note  ")
        self.assertEqual(self.store.load()[0].text, "  padded note  ")

    def test_whitespace_only_note_is_rejected(self):
        with self.assertRaises(InputError):
            self.store.add("   \n\t ")
        self.assertFalse(self.path.exists())

    def test_delete_removes_note(self):
        self.store.add("one")
        self.store.add("two")

        deleted = self.store.delete(1)

        self.assertEqual(deleted.id, 1)
        self.assertEqual([note.id for note in self.store.load()], [2])

    def test_delete_missing_note_raises(self):
        with self.assertRaises(NoteNotFound):
            self.store.delete(42)

    def test_deleted_highest_id_is_not_reused(self):
        self.store.add("one")
        self.store.add("two")
        self.store.delete(2)

        third = self.store.add("three")

        self.assertEqual(third.id, 3)
        self.assertEqual([note.id for note in self.store.load()], [1, 3])

    def test_invalid_json_raises_data_error(self):
        self.path.write_text("{not json", encoding="utf-8")
        with self.assertRaises(DataError) as context:
            self.store.load()
        self.assertIn("Invalid JSON", str(context.exception))

    def test_duplicate_ids_raise_data_error(self):
        self.path.write_text(
            json.dumps(
                {
                    "version": 1,
                    "next_id": 3,
                    "notes": [
                        {"id": 1, "text": "a", "created_at": "2026-01-01T00:00:00Z"},
                        {"id": 1, "text": "b", "created_at": "2026-01-01T00:00:00Z"},
                    ],
                }
            ),
            encoding="utf-8",
        )
        with self.assertRaises(DataError) as context:
            self.store.load()
        self.assertIn("Duplicate note id 1", str(context.exception))

    def test_next_id_must_exceed_every_note_id(self):
        self.path.write_text(
            json.dumps(
                {
                    "version": 1,
                    "next_id": 1,
                    "notes": [
                        {"id": 1, "text": "a", "created_at": "2026-01-01T00:00:00Z"}
                    ],
                }
            ),
            encoding="utf-8",
        )
        with self.assertRaises(DataError):
            self.store.load()

    def test_write_leaves_no_temporary_file(self):
        self.store.add("one")
        self.assertEqual(
            [entry.name for entry in self.path.parent.iterdir()],
            ["notes.json"],
        )


class DataPathTests(unittest.TestCase):
    def test_default_path_is_beside_the_entry_point(self):
        expected = Path(__file__).resolve().parents[1] / "notes.json"
        self.assertEqual(default_data_path(), expected)
        self.assertEqual(resolve_data_path({}), expected)

    def test_notes_data_overrides_default(self):
        self.assertEqual(
            resolve_data_path({"NOTES_DATA": "/tmp/custom-notes.json"}),
            Path("/tmp/custom-notes.json"),
        )

    def test_notes_data_expands_home(self):
        self.assertEqual(
            resolve_data_path({"NOTES_DATA": "~/notes.json"}),
            Path.home() / "notes.json",
        )

    def test_empty_notes_data_is_rejected(self):
        with self.assertRaises(InputError):
            resolve_data_path({"NOTES_DATA": "   "})


if __name__ == "__main__":
    unittest.main()
