from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    #
    # def validate_username(self, username):
    #     sqldb = Database()
    #     sqldb.users_db_cursor.execute("SELECT username FROM users where username = (?)", [username.data])
    #     valeun = sqldb.users_db_cursor.fetchone()
    #     if valeun is None:
    #         raise ValidationError('This Email ID is not registered. Please register before login')