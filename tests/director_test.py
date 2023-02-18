import unittest
from models.director import Director


class DirectorTest(unittest.TestCase):
    def setUp(self):
        self.director1 = Director("Quentin Tarantino", 59, "This is a bio")

    def test_director_has_name(self):
        actual = self.director1.name
        expected = "Quentin Tarantino"
        self.assertEqual(actual, expected)

    def test_director_has_age(self):
        actual = self.director1.age
        expected = 59
        self.assertEqual(actual, expected)

    def test_director_has_bio(self):
        actual = self.director1.bio
        expected = "This is a bio"
        self.assertEqual(actual, expected)
