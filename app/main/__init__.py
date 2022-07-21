from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import jwt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
app = Flask(__name__)
login = LoginManager(app)
jwt = JWTManager(app)


def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    return app
