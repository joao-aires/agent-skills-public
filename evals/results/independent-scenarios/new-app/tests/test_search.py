"""Tests for pure note search behavior."""

import unittest

from notes_app.errors import InputError
from notes_app.search import search_notes
from notes_app.storage import Note


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.notes = [
            Note(id=1, text="Alpha Beta", created_at="2026-01-01T00:00:00Z"),
            Note(id=2, text="literal [draft] .*", created_at="2026-01-01T00:00:00Z"),
            Note(id=3, text="Café ☕", created_at="2026-01-01T00:00:00Z"),
        ]

    def test_match_is_case_insensitive(self):
        self.assertEqual([note.id for note in search_notes(self.notes, "alpha")], [1])
        self.assertEqual([note.id for note in search_notes(self.notes, "BETA")], [1])

    def test_match_is_a_literal_substring_not_a_regex(self):
        self.assertEqual(
            [note.id for note in search_notes(self.notes, "[draft]")], [2]
        )
        self.assertEqual([note.id for note in search_notes(self.notes, ".*")], [2])

    def test_unicode_match_uses_casefold(self):
        self.assertEqual([note.id for note in search_notes(self.notes, "CAFÉ")], [3])

    def test_no_match_returns_empty_list(self):
        self.assertEqual(search_notes(self.notes, "missing"), [])

    def test_blank_term_is_rejected(self):
        for term in ("", "   ", "\t"):
            with self.subTest(term=term):
                with self.assertRaises(InputError):
                    search_notes(self.notes, term)


if __name__ == "__main__":
    unittest.main()
