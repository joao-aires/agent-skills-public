import unittest

import inventory


class PaginationTests(unittest.TestCase):
    def setUp(self):
        self.items = ["a", "b", "c", "d", "e"]

    def test_first_page(self):
        self.assertEqual(inventory.paginate(self.items, 1, 2), ["a", "b"])

    def test_second_page(self):
        self.assertEqual(inventory.paginate(self.items, 2, 2), ["c", "d"])

    def test_last_page(self):
        self.assertEqual(inventory.paginate(self.items, 3, 2), ["e"])

    def test_page_count(self):
        self.assertEqual(inventory.page_count(self.items, 2), 3)

    def test_pages_cover_all_items_in_order(self):
        for size in range(1, len(self.items) + 2):
            pages = [
                inventory.paginate(self.items, page, size)
                for page in range(1, inventory.page_count(self.items, size) + 1)
            ]
            self.assertEqual([item for page in pages for item in page], self.items)
            for full_page in pages[:-1]:
                self.assertEqual(len(full_page), size)
            self.assertGreater(len(pages[-1]), 0)
            self.assertLessEqual(len(pages[-1]), size)

    def test_page_after_last_is_empty(self):
        self.assertEqual(inventory.paginate(self.items, 4, 2), [])

    def test_exact_multiple_has_one_page(self):
        self.assertEqual(inventory.page_count(self.items, 5), 1)
        self.assertEqual(inventory.paginate(self.items, 1, 5), self.items)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            inventory.paginate(self.items, 0, 2)
        with self.assertRaises(ValueError):
            inventory.paginate(self.items, 1, 0)
        with self.assertRaises(ValueError):
            inventory.page_count(self.items, 0)


if __name__ == "__main__":
    unittest.main()
