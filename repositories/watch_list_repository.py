import pdb
from db.run_sql import run_sql
from models.watch_list import Watch_List

# CREATE A WATCH LIST
def save(watch_list):
    sql = "INSERT INTO watch_lists (user_id, movie_id) VALUES (%s, %s) RETURNING *"
    values = [watch_list.user.id, watch_list.movie.id]
    result = run_sql(sql, values)
    id = result
    watch_list.id = id
    return watch_list


# READ ALL WATCH LISTS
def select_all():
    watch_lists = []
    sql = "SELECT * FROM watch_lists"
    results = run_sql(sql)

    for row in results:
        watch_list = Watch_List(row["user"], row["movie"], row["id"])
        watch_lists.append(watch_list)
    return watch_lists


# READ A WATCH LIST
def select(id):
    watch_list = None
    sql = "SELECT * FROM watch_lists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        watch_list = Watch_List(result["user"], result["movie"], result["id"])
    return watch_list


# UPDATE A WATCH_LIST
def update(watch_list):
    sql = "UPDATE watch_lists SET (user_id, movie_id) = (%s, %s) WHERE id = %s"
    values = [watch_list.user.id, watch_list.user.id, watch_list.id]
    run_sql(sql, values)

# DELETE ALL WATCH LISTS
def delete_all():
    sql = "DELETE FROM watch_lists"
    run_sql(sql)

# DELETE A WATCH LIST
def delete(id):
    sql = "DELETE FROM watch_lists WHERE id = %s"
    values = [id]
    run_sql(sql, values)