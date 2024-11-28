'''from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            flash('Login successful!', category='success')
            return redirect(url_for('auth.success'))
        else:
            flash('Invalid email or password', category='error')
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        num_of_course = request.form.get('num_of_course')
        university = request.form.get('university')  # доп поля
        group = request.form.get('group')

        # Проверяем, что обязательные поля не пустые
        if not num_of_course or not university or not group:
            flash('All fields are required!', category='error')
            return redirect(url_for('auth.register'))

        new_user = User(
            email=email,
            full_name=full_name,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256'),
            role='student',
            num_of_course=num_of_course,
            university=university,
            group=group,
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/success')
def success():
    return render_template('success.html')
'''
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
from app.utils.validators import (
    validate_full_name,
    validate_email,
    validate_nickname,
    validate_passwords,
    validate_phone_number,
    validate_date_of_birth,
    validate_accept_policy,
)

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            flash('Login successful!', category='success')
            return redirect(url_for('auth.dashboard'))
        if user and check_password_hash(user.password_hash, password):
            flash('Login successful!', category='success')
            return redirect(url_for('auth.success'))
        else:
            flash('Invalid email or password', category='error')
    return render_template('login.html')



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Собираем данные из формы
        full_name = request.form.get('full_name')
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        phone_number = request.form.get('phone_number')
        date_of_birth = request.form.get('date_of_birth')
        num_of_course = request.form.get('num_of_course')
        university = request.form.get('university')
        group = request.form.get('group')
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
        if not all([full_name, nickname, email, role, password, confirm_password,
                    date_of_birth, num_of_course, university, group]):
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

        new_user = User(
            full_name=full_name,
            nickname=nickname,
            email=email,
            role=role,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256'),
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            num_of_course=num_of_course,
            university=university,
            group=group,
            accept_policy=True if accept_policy == 'on' else False,
        )
        db.session.add(new_user)
        db.session.commit()
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
    if request.method == 'POST':
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        new_password = request.form.get('new_password')

        # Проверка пользователя по email и телефону
        user = User.query.filter_by(email=email, phone_number=phone_number).first()

        if user:
            user.password_hash = generate_password_hash(new_password, method='pbkdf2:sha256')
            db.session.commit()
            flash('Password successfully updated!', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid email or phone number!', category='error')
    return render_template('forgot_password.html')

@auth.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

