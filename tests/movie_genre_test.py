import unittest
from models.genre import Genre
from models.movie_genre import Movie_Genre


class Movie_GenreTest(unittest.TestCase):
    def setUp(self):
        self.genre1 = Genre("Action")
        self.genre2 = Genre("Crime")
        self.movie_genre1 = Movie_Genre(self.genre1, self.genre2)

    def test_movie_genre_has_genre1(self):
        actual = self.movie_genre1.genre1
        expected = self.genre1
        self.assertEqual(actual, expected)
    
    def test_movie_genre_has_genre2(self):
        actual = self.movie_genre1.genre2
        expected = self.genre2
        self.assertEqual(actual, expected)
