import pdb
from db.run_sql import run_sql
from models.actor import Actor


# CREATE ACTOR
def save(actor):
    sql = "INSERT INTO actors (name, age, bio) VALUES (%s, %s, %s) RETURNING *"
    values = [actor.name, actor.age, actor.bio]
    result = run_sql(sql, values)
    id = result
    actor.id = id
    return actor


# READ ALL ACTORS
def select_all():
    actors = []
    sql = "SELECT * FROM actors"
    results = run_sql(sql)

    for row in results:
        actor = Actor(row["name"], row["age"], row["bio"], row["id"])
        actors.append(actor)
    return actors


# READ ACTOR BY ID
def select(id):
    actor = None
    sql = "SELECT * FROM actors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        actor = Actor(result["name"], result["age"], result["bio"], result["id"])
    return actor


# UPDATE ACTOR BY ID
def update(actor):
    sql = "UPDATE actors SET (name, age, bio) = (%s, %s, %s) WHERE id = %s"
    values = [actor.name, actor.age, actor.bio, actor.id]
    run_sql(sql, values)
    return actor

# DELETE ALL ACTORS
def delete_all():
    sql = "DELETE FROM actors"
    run_sql(sql)


# DELETE ACTOR BY ID
def delete(id):
    sql = "DELETE FROM actors WHERE id = %s"
    values = [id]
    run_sql(sql, values)
