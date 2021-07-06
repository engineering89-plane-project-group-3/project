from app.database import Database
from flask_login import UserMixin
from app import login


class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.staff_id = chr(id)
        self.username = username
        self.password = password
        self.role = role

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def set_authenticated(self, bool):
        self.authenticated = bool

    def is_active(self):
        return True

    def get_id(self):
        return self.staff_id


@login.user_loader
def load_user(user_id):
    sqldb = Database()
    sqldb.users_db_cursor.execute("SELECT * from users where staff_id = (?)", [user_id])
    lu = sqldb.users_db_cursor.fetchone()
    if lu is None:
        return None
    else:
        print(int(lu[0]), lu[1], lu[2], lu[3])
        return User(int(lu[0]), lu[1], lu[2], lu[3])