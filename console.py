import pdb
import repositories.actor_repository as actor_repository
import repositories.director_repository as director_repository
import repositories.genre_repository as genre_repository
import repositories.movie_cast_repository as movie_cast_repository
import repositories.movie_genre_repository as movie_genre_repository
import repositories.movie_repository as movie_repository

from models.actor import Actor
from models.director import Director
from models.genre import Genre
from models.movie import Movie
from models.movie_cast import Movie_Cast
from models.movie_genre import Movie_Genre

actor_repository.delete_all()

actor1 = Actor("John Travolta", 69, "JT Bio")
actor_repository.save(actor1)
actor2 = Actor("Samuel L. Jackson", 74, "SLJ Bio")
actor_repository.save(actor2)



