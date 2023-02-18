import unittest
from models.movie_cast import Movie_Cast
from models.actor import Actor


class Movie_CastTest(unittest.TestCase):
    def setUp(self):
        self.actor1 = Actor("John Travolta", 69, "This is JT bio")
        self.actor2 = Actor("Samuel L. Jackson", 74, "This is SLJ bio")
        self.actor3 = Actor("Uma Thurman", 52, "This is UT bio")
        self.movie_cast1 = Movie_Cast(self.actor1, self.actor2, self.actor3)

    def test_movie_has_actor1(self):
        actual = self.movie_cast1.actor1
        expected = self.actor1
        self.assertEqual(actual, expected)
    
    def test_movie_has_actor2(self):
        actual = self.movie_cast1.actor2
        expected = self.actor2
        self.assertEqual(actual, expected)
    
    def test_movie_has_actor3(self):
        actual = self.movie_cast1.actor3
        expected = self.actor3
        self.assertEqual(actual, expected)
