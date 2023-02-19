import unittest
from models.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user1 = User("Phil", "Broadley", "phil@user.com")

    def test_user_has_first_name(self):
        actual = self.user1.first_name
        expected = "Phil"
        self.assertEqual(actual, expected)

    def test_user_has_last_name(self):
        actual = self.user1.last_name
        expected = "Broadley"
        self.assertEqual(actual, expected)

    def test_user_has_email(self):
        actual = self.user1.email
        expected = "phil@user.com"
        self.assertEqual(actual, expected)
