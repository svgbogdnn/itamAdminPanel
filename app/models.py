from app import db
from sqlalchemy.orm import relationship

# Таблица пользователей
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)  # Никнейм
    university = db.Column(db.String(255), nullable=False)  # Университет
    num_of_course = db.Column(db.String(10), nullable=False)  # Номер курса
    institute = db.Column(db.String(255), nullable=True)  # Институт
    group = db.Column(db.String(50), nullable=False)  # Группа
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # student, teacher, admin
    password_hash = db.Column(db.Text, nullable=False)
    registration_date = db.Column(db.DateTime, default=db.func.now())
    status = db.Column(db.String(50), default='offline')  # online/offline
    last_login = db.Column(db.DateTime)
    profile_picture = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date, nullable=False)  # Дата рождения
    accept_policy = db.Column(db.Boolean, nullable=False)  # Чекбокс принятия политики

# Таблица курсов
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    status = db.Column(db.String(50), default='active')  # active/finished
    duration = db.Column(db.Interval)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    course_code = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(100))
    students = db.relationship(
        'Student',
        secondary='course_student',
        back_populates='courses'
    )
    lessons = db.relationship(
        'Lesson',
        backref='course',
        cascade="all, delete-orphan"
    )
    feedback = db.relationship(
        'Feedback',
        backref='course',
        cascade="all, delete-orphan"
    )
    @property
    def students_count(self):
        return len(self.students)


# Таблица студентов
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)  # Полное имя
    email = db.Column(db.String(255), unique=True, nullable=False)  # Email
    phone_number = db.Column(db.String(20))  # Телефон
    date_of_birth = db.Column(db.Date)  # Дата рождения
    registration_date = db.Column(db.DateTime, default=db.func.now())  # Дата регистрации
    group = db.Column(db.String(50))  # Группа студента
    university = db.Column(db.String(255))  # Институт или университет
    status = db.Column(db.String(50), default='active')  # Статус (active/finished)

    # Связь с курсами через промежуточную таблицу
    courses = db.relationship(
        'Course',
        secondary='course_student',
        back_populates='students'
    )

# for temporary
course_student_association = db.Table(
        'course_student',
        db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
        db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    )


# Таблица занятий
class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete="CASCADE"))
    date = db.Column(db.Date, nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time)
    location = db.Column(db.String(255))

# Таблица посещаемости
class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id', ondelete="CASCADE"))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    status = db.Column(db.String(50), nullable=False)  # was/not
    comments = db.Column(db.Text)
    reason_of_excuse = db.Column(db.Text)

# Таблица отзывов
class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id', ondelete="CASCADE"))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete="CASCADE"))
    mark = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    exact_time = db.Column(db.DateTime, default=db.func.now())
    anonymous = db.Column(db.Boolean, default=False)
    type = db.Column(db.String(50))
    response_on_feedback = db.Column(db.Text)

# Таблица уведомлений
class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    status = db.Column(db.String(50), default='unread')  # read/unread
    date_time = db.Column(db.DateTime, default=db.func.now())
    type = db.Column(db.String(50))

# Таблица ролей
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), unique=True, nullable=False)
    permission_list = db.Column(db.JSON, nullable=False)
    description = db.Column(db.Text)

# Таблица статистики
class Statistic(db.Model):
    __tablename__ = 'statistics'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete="CASCADE"))
    type = db.Column(db.String(50), nullable=False)  # attendance/feedback
    parameters = db.Column(db.JSON)
    generated_at = db.Column(db.DateTime, default=db.func.now())

# Таблица дополнительных материалов
class ExtraMaterial(db.Model):
    __tablename__ = 'extra_materials'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete="CASCADE"))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.Text, nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.now())

# Таблица логов
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    action = db.Column(db.String(255), nullable=False)
    target_id = db.Column(db.Integer)
    target_type = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=db.func.now())
