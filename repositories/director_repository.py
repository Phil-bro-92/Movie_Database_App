import pdb
from db.run_sql import run_sql
from models.director import Director


def save(director):
    sql = "INSERT INTO directors (name, age, bio) VALUES (%s, %s, %s) RETURNING *"
    values = [director.name, director.age, director.bio]
    result = run_sql(sql, values)
    id = result
    director.id = id
    return director


def delete_all():
    sql = "DELETE FROM directors"
    run_sql(sql)
