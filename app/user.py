from flask_login import UserMixin


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
