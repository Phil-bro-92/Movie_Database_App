import pdb
import repositories.actor_repository as actor_repository
import repositories.director_repository as director_repository
import repositories.genre_repository as genre_repository
import repositories.movie_repository as movie_repository
import repositories.user_repository as user_repository
import repositories.watch_list_repository as watch_list_repository

from models.actor import Actor
from models.director import Director
from models.genre import Genre
from models.movie import Movie
from models.user import User
from models.watch_list import Watch_List


actor_repository.delete_all()
director_repository.delete_all()
genre_repository.delete_all()
user_repository.delete_all()


actor1 = Actor("John Travolta", 69, "JT Bio")
actor_repository.save(actor1)
actor2 = Actor("Samuel L. Jackson", 74, "SLJ Bio")
actor_repository.save(actor2)
actor3 = Actor("Uma Thurman", 52, "UT Bio")
actor_repository.save(actor3)

director1 = Director("Quentin Tarantino", 59, "QT Bio")
director_repository.save(director1)
director2 = Director("Martin Scorsese", 80, "MS Bio")
director_repository.save(director2)

genre1 = Genre("Action")
genre_repository.save(genre1)
genre2 = Genre("Crime")
genre_repository.save(genre2)

user1 = User("Phil", "Broadley", "phil@user.com")
user_repository.save(user1)
user2 = User("Frank", "Paul", "frank@user.com")
user_repository.save(user2)
