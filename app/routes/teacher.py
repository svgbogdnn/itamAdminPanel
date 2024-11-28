
from flask import Blueprint, render_template
from app.models import Course


teacher = Blueprint('teacher', __name__, template_folder='templates')


@teacher.route('/attendance')
def attendance():
    return "<h1>Attendance Page</h1>"

@teacher.route('/feedback')
def feedback():
    return "<h1>Feedback Page</h1>"

@teacher.route('/export')
def export():
    return "<h1>Export Page</h1>"

@teacher.route('/courses', methods=['GET'])
def courses():
    # Предположим, что id преподавателя = 1 (заглушка, позже нужно заменить логикой)
    teacher_id = 1
    courses = Course.query.filter_by(tutor_id=teacher_id).all()  # Получаем все курсы преподавателя
    return render_template('teacher/courses.html', courses=courses)
