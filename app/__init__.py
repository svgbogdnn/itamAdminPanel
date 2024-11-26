from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.routes.auth import auth

def create_app():
    app = Flask(__name__, template_folder='D:/Apps/PyCharm/itam/templates')
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth, url_prefix='/auth')
    return app

