import unittest
from models.movie import Movie
from models.actor import Actor
from models.director import Director
from models.genre import Genre


class MovieTest(unittest.TestCase):
    def setUp(self):
        self.actor1 = Actor("John Travolta", 69, "This is JT bio")
        self.actor2 = Actor("Samuel L. Jackson", 74, "This is SLJ bio")
        self.actor3 = Actor("Uma Thurman", 52, "This is UT bio")
        self.genre1 = Genre("Action")
        self.genre2 = Genre("Crime")
        self.director1 = Director("Quentin Tarantino", 59, "This is a bio")
        self.movie1 = Movie(
            "Pulp Fiction",
            1994,
            "This is a description",
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

    def test_movie_has_director(self):
        actual = self.movie1.director
        expected = self.director1
        self.assertEqual(actual, expected)

    def test_add_actor_to_movie_cast(self):
        self.movie1.add_actor_to_movie_cast(self.actor1)
        self.movie1.add_actor_to_movie_cast(self.actor2)
        actual = self.movie1.cast
        expected = [self.actor1, self.actor2]
        self.assertEqual(actual, expected)

    def test_add_genre_to_genre_list(self):
        self.movie1.add_genre_to_genre_list(self.genre1)
        self.movie1.add_genre_to_genre_list(self.genre2)
        actual = self.movie1.genres
        expected = [self.genre1, self.genre2]
        self.assertEqual(actual, expected)
