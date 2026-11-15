import json
import tempfile
import unittest
from pathlib import Path

import notes_store
from notes_store import NoteNotFound, NoteStore, StoreError


class StoreTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.path = self.root / "notes.json"
        self.store = NoteStore(self.path)

    def read_raw(self):
        return self.path.read_text(encoding="utf-8")

    def write_raw(self, text):
        self.path.write_text(text, encoding="utf-8")


class AddAndListTests(StoreTestCase):
    def test_missing_file_reads_as_empty(self):
        self.assertEqual(self.store.list_notes(), [])
        self.assertFalse(self.path.exists())

    def test_add_assigns_increasing_ids(self):
        first = self.store.add("buy milk")
        second = self.store.add("call Ana")
        self.assertEqual(first["id"], 1)
        self.assertEqual(second["id"], 2)
        self.assertEqual([n["id"] for n in self.store.list_notes()], [1, 2])
        self.assertEqual([n["text"] for n in self.store.list_notes()], ["buy milk", "call Ana"])

    def test_add_persists_across_instances(self):
        self.store.add("persisted")
        other = NoteStore(self.path)
        self.assertEqual(other.list_notes()[0]["text"], "persisted")

    def test_add_records_a_utc_timestamp(self):
        note = self.store.add("timestamped")
        self.assertRegex(note["created_at"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

    def test_add_creates_parent_directories(self):
        nested = self.root / "a" / "b" / "notes.json"
        note = NoteStore(nested).add("nested")
        self.assertEqual(note["id"], 1)
        self.assertTrue(nested.exists())

    def test_file_is_readable_json_with_schema_fields(self):
        self.store.add("one")
        data = json.loads(self.read_raw())
        self.assertEqual(data["version"], 1)
        self.assertEqual(data["next_id"], 2)
        self.assertEqual(data["notes"][0]["text"], "one")

    def test_unicode_is_stored_unescaped(self):
        self.store.add("café – 日本語")
        self.assertIn("café – 日本語", self.read_raw())
        self.assertEqual(self.store.list_notes()[0]["text"], "café – 日本語")

    def test_list_returns_copies(self):
        self.store.add("original")
        notes = self.store.list_notes()
        notes[0]["text"] = "changed"
        self.assertEqual(self.store.list_notes()[0]["text"], "original")

    def test_no_temporary_files_remain(self):
        self.store.add("one")
        self.store.delete(1)
        leftovers = list(self.root.glob(".notes-*"))
        self.assertEqual(leftovers, [])


class DeleteTests(StoreTestCase):
    def test_delete_removes_one_note(self):
        self.store.add("keep")
        second = self.store.add("remove")
        removed = self.store.delete(second["id"])
        self.assertEqual(removed["text"], "remove")
        self.assertEqual([n["text"] for n in self.store.list_notes()], ["keep"])

    def test_deleted_ids_are_not_reused(self):
        first = self.store.add("one")
        self.store.delete(first["id"])
        second = self.store.add("two")
        self.assertEqual(second["id"], 2)

    def test_delete_unknown_id_raises_and_leaves_file_untouched(self):
        self.store.add("one")
        before = self.read_raw()
        with self.assertRaises(NoteNotFound):
            self.store.delete(99)
        self.assertEqual(self.read_raw(), before)

    def test_note_not_found_is_a_store_error(self):
        self.assertTrue(issubclass(NoteNotFound, StoreError))


class CorruptFileTests(StoreTestCase):
    def test_invalid_json_raises_and_preserves_bytes(self):
        broken = '{"notes": ['
        self.write_raw(broken)
        with self.assertRaises(StoreError):
            self.store.list_notes()
        with self.assertRaises(StoreError):
            self.store.add("would overwrite")
        self.assertEqual(self.read_raw(), broken)

    def test_empty_file_raises(self):
        self.write_raw("   \n")
        with self.assertRaises(StoreError):
            self.store.list_notes()

    def test_non_object_document_raises(self):
        self.write_raw("[1, 2, 3]")
        with self.assertRaises(StoreError):
            self.store.list_notes()

    def test_notes_must_be_an_array(self):
        self.write_raw('{"version": 1, "notes": {}}')
        with self.assertRaises(StoreError):
            self.store.list_notes()

    def test_duplicate_ids_are_rejected(self):
        self.write_raw(
            '{"version": 1, "next_id": 3, "notes": ['
            '{"id": 1, "text": "a"}, {"id": 1, "text": "b"}]}'
        )
        with self.assertRaises(StoreError):
            self.store.list_notes()

    def test_unsupported_schema_version_is_rejected(self):
        self.write_raw('{"version": 99, "notes": []}')
        with self.assertRaises(StoreError):
            self.store.list_notes()

    def test_missing_next_id_is_repaired(self):
        self.write_raw('{"version": 1, "notes": [{"id": 7, "text": "hand edited"}]}')
        note = self.store.add("next")
        self.assertEqual(note["id"], 8)

    def test_stale_next_id_is_raised_above_existing_ids(self):
        self.write_raw('{"version": 1, "next_id": 1, "notes": [{"id": 4, "text": "a"}]}')
        note = self.store.add("b")
        self.assertEqual(note["id"], 5)


class PathResolutionTests(unittest.TestCase):
    def test_override_is_used(self):
        path = notes_store.resolve_path({notes_store.ENV_VAR: "/tmp/custom.json"})
        self.assertEqual(path, Path("/tmp/custom.json"))

    def test_default_when_unset(self):
        path = notes_store.resolve_path({})
        self.assertEqual(path, Path(notes_store.DEFAULT_PATH).expanduser())

    def test_empty_override_falls_back_to_default(self):
        path = notes_store.resolve_path({notes_store.ENV_VAR: ""})
        self.assertEqual(path, Path(notes_store.DEFAULT_PATH).expanduser())

    def test_tilde_is_expanded(self):
        path = notes_store.resolve_path({notes_store.ENV_VAR: "~/notes-test.json"})
        self.assertNotIn("~", str(path))


if __name__ == "__main__":
    unittest.main()
