from flask import Blueprint, request, jsonify, render_template
from app import db, bcrypt
from app.models import users
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # Отображение HTML-страницы для логина

    if request.method == 'POST':
        data = request.form  # Получить данные из формы
        email_or_username = data.get('email_or_username')
        password = data.get('password')

        user = users.query.filter(
            (users.email == email_or_username) | (users.name == email_or_username)
        ).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Invalid password"}), 401

        user.status = "online"
        user.last_login = datetime.utcnow()
        db.session.commit()

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200

@auth_bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')  # Отображение HTML-страницы для регистрации

    if request.method == 'POST':
        data = request.form
        hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        user = users(
            name=data.get('name'),
            email=data.get('email'),
            password=hashed_password,
            role=data.get('role', 'student')  # Роль по умолчанию — студент
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201

