from flask import Blueprint, render_template, request, redirect
from app.utils.models import User
auth_blueprint=Blueprint('auth',__name__,)

@auth_blueprint.route('/')
def index():
    return render_template('index.html')


@auth_blueprint.route('/auth/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if (user.password_hash==password):
             return redirect(f'/student/{user.id}')
    return render_template('login.html')

