import unittest

from notes_search import EmptySearchTerm, normalize_term, search


def note(note_id, text):
    return {"id": note_id, "text": text, "created_at": None}


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.notes = [
            note(1, "Buy milk"),
            note(2, "buy MILK and bread"),
            note(3, "call Ana"),
            note(4, "Straße"),
        ]

    def ids(self, term):
        return [n["id"] for n in search(self.notes, term)]

    def test_matches_ignore_case(self):
        self.assertEqual(self.ids("BUY milk"), [1, 2])

    def test_matches_substring_inside_a_word(self):
        self.assertEqual(self.ids("read"), [2])

    def test_no_match_returns_empty_list(self):
        self.assertEqual(self.ids("zebra"), [])

    def test_preserves_input_order(self):
        self.assertEqual(self.ids("l"), [1, 2, 3])

    def test_whitespace_runs_are_equivalent(self):
        self.assertEqual(self.ids("buy    milk"), [1, 2])

    def test_matches_across_a_stored_newline(self):
        notes = [note(1, "buy\nmilk")]
        self.assertEqual([n["id"] for n in search(notes, "buy milk")], [1])

    def test_unicode_case_folding(self):
        self.assertEqual(self.ids("STRASSE"), [4])

    def test_empty_term_is_rejected(self):
        for term in ("", "   ", "\n\t"):
            with self.subTest(term=term):
                with self.assertRaises(EmptySearchTerm):
                    search(self.notes, term)

    def test_normalize_term_collapses_and_folds(self):
        self.assertEqual(normalize_term("  Buy   MILK "), "buy milk")

    def test_results_are_copies(self):
        results = search(self.notes, "buy")
        results[0]["text"] = "mutated"
        self.assertEqual(self.notes[0]["text"], "Buy milk")

    def test_empty_term_error_is_a_value_error(self):
        self.assertTrue(issubclass(EmptySearchTerm, ValueError))


if __name__ == "__main__":
    unittest.main()
