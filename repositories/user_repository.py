import pdb
from db.run_sql import run_sql
from models.user import User

# CREATE A USER
def save(user):
    sql = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING *"
    values = [user.first_name, user.last_name, user.email]
    result = run_sql(sql, values)
    id = result
    user.id = id
    return user


# READ ALL USERS
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row["first_name"], row["last_name"], row["email"], row["id"])
        users.append(user)
    return users


# READ A USER
def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        user = User(
            result["first_name"], result["last_name"], result["email"], result["id"]
        )
    return user


# UPDATE A USER
def update(user):
    sql = "UPDATE users SET (first_name, last_name, email) = (%s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.email, user.id]
    run_sql(sql, values)


# DELETE ALL USERS
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


# DELETE A USER
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)
