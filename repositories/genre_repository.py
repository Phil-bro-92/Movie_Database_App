import pdb
from db.run_sql import run_sql
from models.genre import Genre

# CREATE A GENRE
def save(genre):
    sql = "INSERT INTO genres (type) VALUES (%s) RETURNING *"
    values = [genre.type]
    result = run_sql(sql, values)
    id = result
    genre.id = id
    return genre


# READ ALL GENRES
def select_all():
    genres = []
    sql = "SELECT * FROM genres"
    results = run_sql(sql)

    for row in results:
        genre = Genre(row["type"], row["id"])
        genres.append(genre)
    return genres


# READ A GENRE
def select(id):
    genre = None
    sql = "SELECT * FROM genres WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        genre = Genre(result["type"], result["id"])
    return genre


# UPDATE A GENRE
def update(genre):
    sql = "UPDATE genres SET (type) = (%s) WHERE id = %s"
    values = [genre.type, genre.id]
    run_sql(sql, values)


# DELETE ALL GENRES
def delete_all():
    sql = "DELETE FROM genres"
    run_sql(sql)


# DELETE A GENRE
def delete(id):
    sql = "DELETE FROM genres WHERE id = %s"
    values = [id]
    run_sql(sql, values)
