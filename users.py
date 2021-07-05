from passlib.hash import sha256_crypt
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

def encrypt(password):
    password = sha256_crypt.hash(password)
    return password