from passlib.hash import sha256_crypt
import sqlite3


def encrypt(password):
    password = sha256_crypt.hash(password)
    return password


class LoginDatabase:

    # Connect to the database
    users_db = sqlite3.connect('app/databases/users.db', check_same_thread=False)
    users_db_cursor = users_db.cursor()

    def database_initialise(self):
        self.users_db_cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            staff_id integer,
            username text,
            password text,
            role text
        )""")
        return "Completed"

    def compare(self, username, password):
        try:
            # self.users_db_cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            # password_hash = ' '.join(self.users_db_cursor.fetchone()) # Removes the hash from a tuple as sql exports info as a tuple
            # password = sha256_crypt.verify(password, password_hash)
            self.users_db_cursor.execute("SELECT password FROM users where username = (?)", [username])
            real_password = self.users_db_cursor.fetchone()
            if password == real_password[0]:
                return True
            return False
        except Exception as e:
            print(e)
            return False