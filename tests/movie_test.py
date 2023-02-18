import unittest
from models.movie_cast import Movie_Cast
from models.movie_genre import Movie_Genre
from models.movie import Movie
from models.actor import Actor
from models.director import Director
from models.genre import Genre


class MovieTest(unittest.TestCase):
    def setUp(self):
        self.actor1 = Actor("John Travolta", 69, "This is JT bio")
        self.actor2 = Actor("Samuel L. Jackson", 74, "This is SLJ bio")
        self.actor3 = Actor("Uma Thurman", 52, "This is UT bio")
        self.movie_cast1 = Movie_Cast(self.actor1, self.actor2, self.actor3)
        self.genre1 = Genre("Action")
        self.genre2 = Genre("Crime")
        self.movie_genre1 = Movie_Genre(self.genre1, self.genre2)
        self.director1 = Director("Quentin Tarantino", 59, "This is a bio")
        self.movie1 = Movie(
            "Pulp Fiction",
            1994,
            "This is a description",
            self.movie_cast1,
            self.movie_genre1,
            self.director1,
        )

    def test_movie_has_title(self):
        actual = self.movie1.title
        expected = "Pulp Fiction"
        self.assertEqual(actual, expected)

    def test_movie_has_year(self):
        actual = self.movie1.year
        expected = 1994
        self.assertEqual(actual, expected)

    def test_movie_has_description(self):
        actual = self.movie1.description
        expected = "This is a description"
        self.assertEqual(actual, expected)

    def test_movie_has_cast(self):
        actual = self.movie1.cast
        expected = self.movie_cast1
        self.assertEqual(actual, expected)

    def test_movie_has_genre(self):
        actual = self.movie1.genre
        expected = self.movie_genre1
        self.assertEqual(actual, expected)

    def test_movie_has_director(self):
        actual = self.movie1.director
        expected = self.director1
        self.assertEqual(actual, expected)
