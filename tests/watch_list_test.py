import unittest
from models.watch_list import Watch_List
from models.user import User
from models.movie import Movie


class Watch_ListTest(unittest.TestCase):
    def setUp(self):
        self.user1 = User("Phil", "Broadley", "phil@user.com")
        self.movie1 = Movie(
            "Pulp Fiction", 1994, "movie description", "Quentin Tarantino"
        )
        self.watch_list1 = Watch_List(self.user1, self.movie1)

    def test_watch_list_has_user(self):
        actual = self.watch_list1.user
        expected = self.user1
        self.assertEqual(actual, expected)

    def test_watch_list_has_movie(self):
        actual = self.watch_list1.movie
        expected = self.movie1
        self.assertEqual(actual, expected)
