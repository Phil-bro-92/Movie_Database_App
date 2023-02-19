class Movie:
    def __init__(self, title, year, description, director, id=None):
        self.title = title
        self.year = year
        self.description = description
        self.cast = []
        self.director = director
        self.genres = []
        self.id = id

    def add_actor_to_movie_cast(self, actor):
        self.cast.append(actor)

    def add_genre_to_genre_list(self, genre):
        self.genres.append(genre)
