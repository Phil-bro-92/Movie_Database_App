import pdb
from db.run_sql import run_sql
from models.movie_cast import Movie_Cast

# CREATE A MOVIE CAST
def save(movie_cast):
    sql = "INSERT INTO movie_casts (actor1, actor2, actor3) VAlUES(%s, %s, %s) RETURNING *"
    values = [movie_cast.actor1.id, movie_cast.actor2.id, movie_cast.actor3.id]
    result = run_sql(sql, values)
    id = result
    movie_cast.id = id
    return movie_cast


# READ ALL MOVIE CASTS
def select_all():
    movie_casts = []
    sql = "SELECT * FROM movie_casts"
    results = run_sql(sql)

    for row in results:
        movie_cast = Movie_Cast(row.actor1.id, row.actor2.id, row.actor3.id, row["id"])
        movie_casts.append(movie_cast)
    return movie_casts

# DELETE ALL MOVIE CASTS
def delete_all():
    sql = "DELETE FROM movie_casts"
    run_sql(sql)