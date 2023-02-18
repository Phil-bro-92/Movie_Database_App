import unittest
from models.genre import Genre


class GenreTest(unittest.TestCase):
    def setUp(self):
        self.genre1 = Genre("Action")

    def test_genre_has_type(self):
        actual = self.genre1.type
        expected = "Action"
        self.assertEqual(actual, expected)
