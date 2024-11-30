from flask import render_template, request, redirect, url_for, flash, Blueprint
from app.models import Course
from app import db
from app.models import Lesson, Attendance, Feedback
from datetime import datetime

teacher = Blueprint('teacher', __name__, template_folder='templates')

@teacher.route('/attendance', methods=['GET'])
def attendance():
    teacher_id = 44
    courses = Course.query.filter_by(tutor_id=teacher_id).all()
    lessons = Lesson.query.filter(Lesson.course_id.in_([course.id for course in courses])).all()
    return render_template('teacher/attendance.html', courses=courses, lessons=lessons)

@teacher.route('/feedback', methods=['GET'])
def feedback():
    teacher_id = 44
    courses = Course.query.filter_by(tutor_id=teacher_id).all()
    feedback_records = []

    # Получаем отзывы для каждого курса и урока
    for course in courses:
        lessons = Lesson.query.filter_by(course_id=course.id).all()
        for lesson in lessons:
            feedback_records.extend(Feedback.query.filter_by(lesson_id=lesson.id).all())

    # Фильтрация и сортировка
    sort_by = request.args.get('sort_by', 'date')  # По умолчанию сортируем по дате
    sort_order = request.args.get('sort_order', 'asc')  # По умолчанию по возрастанию

    if sort_by == 'mark':
        feedback_records = sorted(feedback_records, key=lambda f: f.mark, reverse=(sort_order == 'desc'))
    elif sort_by == 'date':
        feedback_records = sorted(feedback_records, key=lambda f: f.exact_time, reverse=(sort_order == 'desc'))

    # Добавляем среднюю оценку и описание качества курса
    for course in courses:
        course.avg_rating = course.average_rating  # Средняя оценка
        course.quality = course.course_quality  # Качество курса

    return render_template('teacher/feedback.html', courses=courses, feedback_records=feedback_records)

@teacher.route('/feedback/response/<int:feedback_id>', methods=['POST'])
def reply_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    response = request.form['response']
    feedback.response_on_feedback = response  # Ответ преподавателя

    db.session.commit()

    flash('Response added successfully!', 'success')
    return redirect(url_for('teacher.feedback'))

@teacher.route('/feedback/hide/<int:feedback_id>', methods=['POST'])
def hide_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    feedback.is_hidden = True  # Скрываем фидбек (нужно добавить поле в модели)

    db.session.commit()

    flash('Feedback hidden successfully!', 'success')
    return redirect(url_for('teacher.feedback'))
@teacher.route('/feedback/unhide/<int:feedback_id>', methods=['POST'])

def unhide_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    feedback.is_hidden = False  # Восстанавливаем фидбек

    db.session.commit()

    flash('Feedback restored successfully!', 'success')
    return redirect(url_for('teacher.feedback'))

@teacher.route('/feedback/<int:lesson_id>', methods=['GET', 'POST'])
def submit_feedback(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    feedbacks = Feedback.query.filter_by(lesson_id=lesson_id).all()
    if request.method == 'POST':
        # Получаем данные формы
        mark = request.form['mark']
        comment = request.form['comment']
        anonymous = 'anonymous' in request.form
        feedback_type = request.form['type']
        student_id = request.form['student_id']  # Здесь получаем ID студента из формы

        # Создаем новый объект Feedback
        feedback = Feedback(
            lesson_id=lesson.id,
            student_id=student_id,  # Используем переданный ID студента
            mark=mark,
            comment=comment,
            anonymous=anonymous,
            type=feedback_type
        )

        db.session.add(feedback)
        db.session.commit()

        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('teacher.feedback', lesson_id=lesson.id))

    return render_template('teacher/manage_feedback.html', lesson=lesson)

@teacher.route('/courses', methods=['GET'])
def courses():
    teacher_id = 44
    courses = Course.query.filter_by(tutor_id=teacher_id).all()
    return render_template('teacher/courses.html', courses=courses)

@teacher.route('/courses/<int:course_id>/lessons', methods=['GET'])
def lessons(course_id):
    teacher_id = 44
    return f"Lessons for course ID: {course_id}"

@teacher.route('/courses/<int:course_id>')
def course_details(course_id):
    teacher_id = 44
    course = Course.query.filter_by(id=course_id, tutor_id=teacher_id).first_or_404()
    return f"Details for course: {course.name}"

@teacher.route('/courses/<int:course_id>/students', methods=['GET'])
def view_students(course_id):
    teacher_id = 44
    course = Course.query.filter_by(id=course_id, tutor_id=teacher_id).first()
    if not course:
        flash('Course not found!', category='error')
        return redirect(url_for('teacher.courses'))
    students = course.students
    return render_template('teacher/view_students.html', course=course, students=students)


@teacher.route('/courses/<int:course_id>/feedback', methods=['GET'])
def analyze_feedback(course_id):
    teacher_id = 44  # Заглушка для текущего учителя
    course = Course.query.filter_by(id=course_id, tutor_id=teacher_id).first()
    if not course:
        flash('Course not found!', category='error')
        return redirect(url_for('teacher.courses'))

    feedback = course.feedback  # Получение всех фидбеков курса
    feedback_summary = {
        "average_rating": round(sum(f.mark for f in feedback) / len(feedback), 2) if feedback else 0,
        "total_comments": len([f.comment for f in feedback if f.comment]),
        "positive_comments": len([f for f in feedback if f.mark >= 4]),
        "negative_comments": len([f for f in feedback if f.mark < 4]),
    }

    return render_template('teacher/analyze_feedback.html', course=course, feedback_summary=feedback_summary)

@teacher.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        course_code = request.form.get('course_code')
        category = request.form.get('category')

        # Заглушка для ID преподавателя
        teacher_id = 44

        new_course = Course(
            name=name,
            description=description,
            tutor_id=teacher_id,
            start_date=start_date,
            end_date=end_date,
            course_code=course_code,
            category=category
        )
        db.session.add(new_course)
        db.session.commit()
        flash('Course added successfully!', category='success')
        return redirect(url_for('teacher.courses'))
    return render_template('teacher/add_course.html')

@teacher.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        course.name = request.form.get('name')
        course.description = request.form.get('description')
        course.start_date = request.form.get('start_date')
        course.end_date = request.form.get('end_date')
        course.course_code = request.form.get('course_code')
        course.category = request.form.get('category')
        db.session.commit()
        flash('Course updated successfully!', category='success')
        return redirect(url_for('teacher.courses'))
    return render_template('teacher/edit_course.html', course=course)

@teacher.route('/courses/<int:course_id>/delete', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted successfully!', category='success')
    return redirect(url_for('teacher.courses'))


@teacher.route('/attendance/<int:lesson_id>', methods=['GET', 'POST'])
def manage_attendance(lesson_id):
    # Получаем урок
    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        flash('Lesson not found!', category='error')
        return redirect(url_for('teacher.attendance'))

    # Получаем курс, связанный с уроком
    course = Course.query.get(lesson.course_id)
    if not course:
        flash('Course not found!', category='error')
        return redirect(url_for('teacher.attendance'))

    # Получаем студентов и их посещаемость
    attendance_records = Attendance.query.filter_by(lesson_id=lesson_id).all()

    if request.method == 'POST':
        # Обработка изменения статуса студентов
        for record in attendance_records:
            status = request.form.get(f'status_{record.id}')
            comment = request.form.get(f'comment_{record.id}')
            reason = request.form.get(f'reason_{record.id}')
            record.status = status
            record.comments = comment
            record.reason_of_excuse = reason
        db.session.commit()
        flash('Attendance updated successfully!', category='success')
        return redirect(url_for('teacher.manage_attendance', lesson_id=lesson_id))

    return render_template('teacher/manage_attendance.html', lesson=lesson, course=course,
                           attendance_records=attendance_records)
