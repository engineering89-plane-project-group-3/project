from flask import Flask
from flask_login import LoginManager

flask_app = Flask(__name__)
flask_app.secret_key = '266091f8165a9b3870bf9ba2'
login = LoginManager(flask_app)

from app import routes