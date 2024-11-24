from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:1234@localhost/Itam project"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Загрузка конфигурации из файла config.py или .env
    app.config.from_object('app.config.Config')

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Регистрация маршрутов
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

