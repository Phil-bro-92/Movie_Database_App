import pdb
from db.run_sql import run_sql
from models.director import Director

# CREATE A DIRECTOR
def save(director):
    sql = "INSERT INTO directors (name, age, bio) VALUES (%s, %s, %s) RETURNING *"
    values = [director.name, director.age, director.bio]
    result = run_sql(sql, values)
    id = result
    director.id = id
    return director


# READ ALL DIRECTORS
def select_all():
    directors = []
    sql = "SELECT * FROM directors"
    results = run_sql(sql)

    for row in results:
        director = Director(row["name"], row["age"], row["bio"], row["id"])
        directors.append(director)
    return directors


# READ A DIRECTOR
def select(id):
    director = None
    sql = "SELECT * FROM directors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        director = Director(result["name"], result["age"], result["bio"], result["id"])
    return director


# UPDATE A DIRECTOR
def update(director):
    sql = "UPDATE directors SET (name, age, bio) = (%s, %s, %s) WHERE id = %s"
    values = [director.name, director.age, director.bio, director.id]
    run_sql(sql, values)


# DELETE ALL DIRECTORS
def delete_all():
    sql = "DELETE FROM directors"
    run_sql(sql)


# DELETE A DIRECTOR
def delete(id):
    sql = "DELETE FROM directors WHERE id = %s"
    values = [id]
    run_sql(sql, values)
