from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.utils.validators import (
    validate_full_name,
    validate_email,
    validate_nickname,
    validate_passwords,
    validate_phone_number,
    validate_date_of_birth,
    validate_accept_policy,
)
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    from app.models import User  # импорт внутри функции для избежания круговой зависимости

    if current_user.is_authenticated:
        return redirect(url_for('teacher.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', category='success')
            return redirect(url_for('teacher.dashboard'))

        flash('Invalid email or password', category='error')

    return render_template('login.html')


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    from app.models import User
    if request.method == 'POST':
        # Собираем данные из формы
        full_name = request.form.get('full_name')
        university = request.form.get('university')
        num_of_course = request.form.get('num_of_course')
        institute = request.form.get('institute')
        group = request.form.get('group')
        role = request.form.get('role')
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        phone_number = request.form.get('phone_number')
        date_of_birth = request.form.get('date_of_birth')
        accept_policy = request.form.get('accept_policy')

        # validation
        validations = [
            validate_full_name(full_name),
            validate_email(email),
            validate_nickname(nickname),
            validate_passwords(password, confirm_password),
            validate_phone_number(phone_number),
            validate_date_of_birth(date_of_birth),
            validate_accept_policy(accept_policy),
        ]

        for is_valid, error_message in validations:
            if not is_valid:
                flash(error_message, category='error')
                return redirect(url_for('auth.register'))

        # Проверка обязательных полей
        if not all([full_name, university, num_of_course, institute, group,
                    role, email, nickname, password, confirm_password, phone_number,
                    date_of_birth]):
            flash('All fields are required!', category='error')
            return redirect(url_for('auth.register'))

        # Проверка совпадения паролей
        if password != confirm_password:
            flash('Passwords do not match!', category='error')
            return redirect(url_for('auth.register'))

        # Проверка принятия политики
        if not accept_policy:
            flash('You must accept the site policy to register.', category='error')
            return redirect(url_for('auth.register'))

        # Проверка уникальности email
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email is already registered!', category='error')
            return redirect(url_for('auth.register'))

        # Создание нового пользователя
        new_user = User(
            full_name=full_name,
            university=university,
            num_of_course=num_of_course,
            institute=institute,
            group=group,
            role=role,
            email=email,
            nickname=nickname,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256'),
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            accept_policy=True if accept_policy == 'on' else False,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Account created successfully!', category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

# site policy
@auth.route('/register/policy')
def policy():
    return render_template('policy.html')

# change password
@auth.route('/login/repassword', methods=['GET', 'POST'])
def forgot_password():
    from app.models import User
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        new_password = request.form.get('new_password')

        # Проверка пользователя по ФИО, email и телефону
        user = User.query.filter_by(full_name=full_name, email=email, phone_number=phone_number).first()

        if user:
            new_password = request.form['new_password']
            user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            flash('Password successfully updated', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid full name, email, or phone number!', category='error')
    return render_template('forgot_password.html')

@auth.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

