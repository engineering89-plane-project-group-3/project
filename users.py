import sqlite3

# Connect to the database
users_db = sqlite3.connect('databases/users.db')
users_db_cursor = users_db.cursor()


def database_initialise():
    users_db_cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        staff_id integer,
        username text,
        password text,
        role text
    )""")
    return "Completed"

def add_user(staff_id, username, password, role):
    users_db_cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (staff_id, username, password, role))
    users_db.commit()
    return "User added"

def all_users():
    users_db_cursor.execute("SELECT * FROM users")
    return users_db_cursor.fetchall()

database_initialise()
add_user(
    int(input("Enter staff id: ")),
    str(input("Enter username: ")),
    str(input("Enter password: ")),
    str(input(("Enter role: ")))
)
print(all_users())
