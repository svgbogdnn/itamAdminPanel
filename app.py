import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Инициализация объектов для работы с БД, миграциями и Flask-Login
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


class Config:
    # Настройки подключения к базе данных
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/dbitam"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Секретный ключ для безопасности сессий и куков
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")


def create_app():
    # Создание приложения Flask
    app = Flask(__name__, template_folder='D:/Apps/PyCharm/itam/templates')    # Загрузка конфигурации
    app.config.from_object(Config)

    # Инициализация приложений с базой данных, миграциями и авторизацией
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Указание страницы, куда перенаправлять пользователей, если они не авторизованы
    login_manager.login_view = 'auth.login'

    from app.routes.auth import auth
    from app.routes.teacher import teacher

    app.register_blueprint(teacher, url_prefix='/student/dashboard')
    app.register_blueprint(teacher, url_prefix='/student/attendance')
    app.register_blueprint(teacher, url_prefix='/student/courses')
    app.register_blueprint(teacher, url_prefix='/student/feedback')

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(teacher, url_prefix='/teacher')
    return app