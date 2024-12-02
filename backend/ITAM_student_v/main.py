from app.utils.models import db
from flask import Flask
from app.routes.student import student_blueprint
from app.routes.auth import auth_blueprint
from app.routes.courses import courses_blueprint
from flask_sqlalchemy import SQLAlchemy
from app.utils.models import User

app=Flask(__name__, template_folder='C:/Users/Maria/PycharmProjects/ITAM_student_v/templates')
#создаем объект класса Flask

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///itam.db' #местоположение, соединение
# с бд
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) #инициализация бд

app.register_blueprint(student_blueprint) ## register routes from main_panel
app.register_blueprint(auth_blueprint)
app.register_blueprint(courses_blueprint)

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)
