import unittest

from auth import authenticate


class AuthTests(unittest.TestCase):
    def test_bearer_token_is_accepted(self):
        self.assertEqual(authenticate({"Authorization": "Bearer alice"}, {}), "alice")


if __name__ == "__main__":
    unittest.main()
