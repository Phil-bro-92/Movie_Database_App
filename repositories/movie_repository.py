import pdb
from db.run_sql import run_sql
from models.movie import Movie

# CREATE A MOVIE
def save(movie):
    sql = "INSERT INTO movies (title, year, description, director) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [movie.title, movie.year, movie.description, movie.director]
    result = run_sql(sql, values)
    id = result
    movie.id = id
    return movie


# READ ALL MOVIES
def select_all():
    movies = []
    sql = "SELECT * FROM movies;"
    results = run_sql(sql)

    for row in results:
        movie = Movie(
            row["title"], row["year"], row["description"], row["director"], row["id"]
        )
        movies.append(movie)
    return movies


# READ A MOVIE
def select(id):
    movie = None
    sql = "SELECT * FROM movies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        movie = Movie(
            result["title"],
            result["year"],
            result["description"],
            result["director"],
            result["id"],
        )
    return movie


# UPDATE A MOVIE
def update(movie):
    sql = "UPDATE movies SET (title, year, description, director) = (%s, %s, %s, %s) WHERE id = %s"
    values = [movie.title, movie.year, movie.description, movie.director, movie.id]
    run_sql(sql, values)


# DELETE ALL MOVIES
def delete_all():
    sql = "DELETE FROM movies"
    run_sql(sql)


# DELETE A MOVIE
def delete(id):
    sql = "DELETE FROM movies WHERE id = %s"
    values = [id]
    run_sql(sql, values)
