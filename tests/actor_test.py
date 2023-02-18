import unittest
from models.actor import Actor


class ActorTest(unittest.TestCase):
    def setUp(self):
        self.actor1 = Actor("John Travolta", 69, "This is a bio")

    def test_actor_has_name(self):
        actual = self.actor1.name
        expected = "John Travolta"
        self.assertEqual(actual, expected)

    def test_actor_has_age(self):
        actual = self.actor1.age
        expected = 69
        self.assertEqual(actual, expected)

    def test_actor_has_bio(self):
        actual = self.actor1.bio
        expected = "This is a bio"
        self.assertEqual(actual, expected)
