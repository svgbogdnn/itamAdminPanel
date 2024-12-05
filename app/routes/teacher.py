from flask import render_template, request, redirect, url_for, flash, Blueprint, Response, jsonify
from app.models import Course
from app import db
from app.models import Lesson, Attendance, Feedback, Course, Lesson
from datetime import datetime, timedelta
from sqlalchemy.sql import func
#for export
import csv
from io import StringIO
from openpyxl import Workbook
from io import BytesIO
from flask import send_file
from flask_login import current_user, login_required
#maintain my man

teacher = Blueprint('teacher', __name__, template_folder='templates')

'''Overall settings'''
@teacher.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    from app.models import User
    from app.models import course_student
    user = User.query.filter_by(id=current_user.id).first()

    current_user_data = User.query.get(current_user.id)
    user_name = current_user_data.full_name  # Или другой атрибут, соответствующий имени
    user_role = current_user_data.role  # Или соответствующий атрибут роли
    total_users = User.query.count() #всего пользователей
    total_students = User.query.filter_by(role='student').count() #всего студентов
    total_teachers = User.query.filter_by(role='teacher').count() #всего учителей
    active_users = User.query.filter(User.last_login >= datetime.now() - timedelta(days=1)).count() #активные юзеры за последние 24 часа
    active_courses = Course.query.filter_by(status='active').count() #активные курсы колво

    #самый популярный курс
    popular_course_query = db.session.query(
        Course,
        db.func.count(course_student.c.student_id).label('student_count')
    ).join(course_student, Course.id == course_student.c.course_id).group_by(Course.id).order_by(
        db.func.count(course_student.c.student_id).desc()
    ).first()
    popular_course = popular_course_query[0].name if popular_course_query else "No courses yet"

    avg_lesson_rating = Feedback.query.with_entities(func.avg(Feedback.mark)).scalar() #средняя оценка по фидбекам
    teacher_feedback_query = Feedback.query.join(Course, Feedback.course_id == Course.id).filter(
        Course.tutor_id == current_user.id
    ).with_entities(func.avg(Feedback.mark)).scalar()
    teacher_rating = round(teacher_feedback_query, 2) if teacher_feedback_query else "N/A"

    return render_template(
        'dashboard.html',
        user_name=current_user_data.full_name,
        user_role = current_user_data.role,
        total_users=total_users,
        total_students=total_students,
        total_teachers=total_teachers,
        active_users=active_users,
        active_courses=active_courses,
        popular_course=popular_course,
        avg_lesson_rating=round(avg_lesson_rating, 2) if avg_lesson_rating else "N/A",
        teacher_rating=teacher_rating
    )

@teacher.route('/help', methods=['GET'])
def help_page():
    return render_template('help.html')

@teacher.route('/tips', methods=['GET'])
def tips_page():
    return render_template('tips.html')

@teacher.route('/notifications')
def notifications():
    return render_template('teacher/notifications.html')

@teacher.route('/teacher/profile')
@login_required
def profile():
    from app.models import User
    user = User.query.filter_by(id=current_user.id).first()
    return render_template('teacher/profile.html', user=user)

'''Courses'''
@teacher.route('/courses', methods=['GET'])
def courses():
    teacher_id = current_user.id
    courses = Course.query.filter_by(tutor_id=teacher_id).all()
    return render_template('teacher/courses.html', courses=courses)

@teacher.route('/courses/<int:course_id>')
def course_details(course_id):
    teacher_id = current_user.id
    course = Course.query.filter_by(id=course_id, tutor_id=teacher_id).first_or_404()
    return f"Details for course: {course.name}"

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
        teacher_id = current_user.id

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

'''Lessons'''
@teacher.route('/courses/<int:course_id>/lessons', methods=['GET'])
def lessons(course_id):
    teacher_id = current_user.id
    return f"Lessons for course ID: {course_id}"

@teacher.route('/add_lesson', methods=['GET', 'POST'])
@login_required
def add_lesson():
    if request.method == 'POST':
        # Получаем данные из формы
        lesson_title = request.form.get('topic')
        lesson_date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()  # Преобразуем строку в дату
        start_time = datetime.strptime(request.form.get('start_time'), '%H:%M').time()  # Время начала
        end_time = datetime.strptime(request.form.get('end_time'), '%H:%M').time() if request.form.get('end_time') else None  # Время окончания (если есть)
        location = request.form.get('location')
        course_id = request.form.get('course_id')

        # Создаем новый объект Lesson
        new_lesson = Lesson(
            course_id=course_id,
            date=lesson_date,
            topic=lesson_title,
            start_time=start_time,
            end_time=end_time,
            location=location
        )

        # Добавляем в базу данных
        db.session.add(new_lesson)
        db.session.commit()

        # Перенаправляем обратно на страницу курса или на страницу с уроками
        return redirect(url_for('teacher.dashboard'))

    # Для GET-запроса, выводим форму
    courses = Course.query.all()  # Получаем список всех курсов из базы данных
    return render_template('teacher/add_lesson.html', courses=courses)

@teacher.route('/courses/<int:course_id>/students', methods=['GET'])
def view_students(course_id):
    teacher_id = current_user.id
    course = Course.query.filter_by(id=course_id, tutor_id=teacher_id).first()
    if not course:
        flash('Course not found!', category='error')
        return redirect(url_for('teacher.courses'))
    students = course.students
    return render_template('teacher/view_students.html', course=course, students=students)

@teacher.route('/courses/<int:course_id>/feedback', methods=['GET'])
def analyze_feedback(course_id):
    teacher_id = current_user.id  # Заглушка для текущего учителя
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

'''Attendance'''
# @teacher.route('/attendance', methods=['GET', 'POST'])
# @login_required
# def attendance():
#     from app.models import User
#     teacher_id = current_user.id
#     # Получение всех курсов, связанных с учителем
#     courses = Course.query.filter_by(tutor_id=teacher_id).all()
#
#     # Получение всех уроков, связанных с курсами этого учителя
#     records = db.session.query(Attendance).join(Lesson).join(Course).join(User).all()
#
#     # Получение фильтров из запроса
#     course_filter = request.args.getlist('course')  # Список курсов
#     date_filter = request.args.getlist('date')  # Список дат
#     status_filter = request.args.getlist('status')  # Статус (присутствие/отсутствие)
#
#     query = Lesson.query
#
#     if course_filter:
#         query = query.join(Course).filter(Course.id.in_(course_filter))
#
#     if date_filter:
#         query = query.filter(Lesson.date.in_(date_filter))
#
#     if status_filter:
#         query = query.join(Attendance).filter(Attendance.status.in_(status_filter))
#
#     lessons = query.all()
#
#     # Возврат в шаблон с фильтрами и уроками
#     return render_template('teacher/attendance.html', courses=courses, lessons=lessons,
#                            course_filter=course_filter, date_filter=date_filter, status_filter=status_filter)
#
# @teacher.route('/attendance/<int:lesson_id>', methods=['GET', 'POST'])
# @login_required
# def manage_attendance(lesson_id):
#     from app.models import User
#     # Получаем урок
#     lesson = Lesson.query.get(lesson_id)
#     if not lesson:
#         flash('Lesson not found!', category='error')
#         return redirect(url_for('teacher.attendance'))
#
#     # Получаем курс, связанный с уроком
#     course = Course.query.get(lesson.course_id)
#     if not course:
#         flash('Course not found!', category='error')
#         return redirect(url_for('teacher.attendance'))
#
#     # Получаем студентов и их посещаемость
#     attendance_records = Attendance.query.filter_by(lesson_id=lesson_id).all()
#
#     if request.method == 'POST':
#         # Обработка изменения статуса студентов
#         for record in attendance_records:
#             status = request.form.get(f'status_{record.id}')
#             comment = request.form.get(f'comment_{record.id}')
#             reason = request.form.get(f'reason_{record.id}')
#             record.status = status
#             record.comments = comment
#             record.reason_of_excuse = reason
#         db.session.commit()
#         flash('Attendance updated successfully!', category='success')
#         return redirect(url_for('teacher.manage_attendance', lesson_id=lesson_id))
#
#     return render_template('teacher/manage_attendance.html', lesson=lesson, course=course,
#                            attendance_records=attendance_records)

@teacher.route('/attendance', methods=['GET'])
def attendance():
    # Получаем все курсы и уроки для фильтрации
    courses = Course.query.all()
    lessons = Lesson.query.all()

    # Чтение параметров фильтра из запроса
    course_filter = request.args.getlist('course')
    date_filter = request.args.getlist('date')
    status_filter = request.args.getlist('status')

    # Начинаем базовый запрос для посещаемости
    query = Attendance.query

    if course_filter and course_filter != ['']:
        query = query.join(Lesson).filter(Lesson.course_id.in_(course_filter))
    if date_filter and date_filter != ['']:
        query = query.filter(Attendance.lesson.has(Lesson.date.in_(date_filter)))
    if status_filter and status_filter != ['']:
        query = query.filter(Attendance.status.in_(status_filter))

    # Получаем записи посещаемости
    attendance_records = query.all()

    return render_template('teacher/attendance.html', courses=courses, lessons=lessons, attendance_records=attendance_records,
                           course_filter=course_filter, date_filter=date_filter, status_filter=status_filter)

@teacher.route('/get_lessons_for_course/<int:course_id>', methods=['GET'])
def get_lessons_for_course(course_id):
    lessons = Lesson.query.filter_by(course_id=course_id).all()
    print(f"Lessons for course {course_id}: {lessons}")  # Добавьте для отладки
    lessons_data = [{"date": lesson.date} for lesson in lessons]
    return jsonify({"lessons": lessons_data})

'''Feedback'''
@teacher.route('/feedback', methods=['GET'])
def feedback():
    teacher_id = current_user.id
    courses = Course.query.filter_by(tutor_id=teacher_id).all()

    # Получение параметров фильтрации
    selected_course_id = request.args.get('course_id', type=int)
    specific_date = request.args.get('specific_date')
    sort_by = request.args.get('sort_by', 'date')
    sort_order = request.args.get('sort_order', 'asc')

    # Базовый запрос
    query = Feedback.query.join(Lesson).join(Course).filter(Course.tutor_id == teacher_id)

    # Фильтрация по курсу
    if selected_course_id:
        query = query.filter(Course.id == selected_course_id)

    if specific_date:
        query = query.filter(Lesson.date == specific_date)

    # Сортировка
    if sort_by == 'mark':
        query = query.order_by(Feedback.mark.desc() if sort_order == 'desc' else Feedback.mark.asc())
    else:
        query = query.order_by(Lesson.date.desc() if sort_order == 'desc' else Lesson.date.asc())

    feedback_records = query.all()

    return render_template(
        'teacher/feedback.html',
        courses=courses,
        feedback_records=feedback_records,
        selected_course_id=selected_course_id,
        specific_date=specific_date,
        sort_by=sort_by,
        sort_order=sort_order
    )

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

'''Export'''
@teacher.route('/export/csv', methods=['GET'])
def export_csv():
    teacher_id = current_user.id
    courses = Course.query.filter_by(tutor_id=teacher_id).all()

    # Получаем параметры фильтрации
    course_filter = request.args.get('course', None)
    date_filter = request.args.get('date', None)
    student_filter = request.args.get('student', None)

    query = Feedback.query

    if course_filter:
        query = query.filter_by(course_id=course_filter)
    if date_filter:
        query = query.filter(Feedback.exact_time >= date_filter)
    if student_filter:
        query = query.filter_by(student_id=student_filter)

    filtered_feedbacks = query.all()

    # Подготовка данных для CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['Course', 'Student', 'Mark', 'Comment'])
    for feedback in filtered_feedbacks:
        writer.writerow([feedback.course.name, feedback.student.full_name, feedback.mark, feedback.comment])

    output = si.getvalue()
    response = Response(output, mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=feedback_export.csv'
    return response

@teacher.route('/export', methods=['GET', 'POST'])
def export():
    # if group or student = None ==> all groups or students
    if request.method == 'POST':
        # Получаем параметры фильтрации из формы
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        data_type = request.form.get('data_type', 'attendance')  # По умолчанию экспорт посещаемости
        course_filter = request.form.get('course')
        #make a temporary filter for students like online fil
        group_filter = request.form.get('group')
        student_filter = request.form.get('student')

        # Преобразуем start_date и end_date в формат datetime.date
        start_date = None
        end_date = None
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            except ValueError:
                start_date = None  # Если дата некорректная, игнорируем фильтрацию по дате
        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            except ValueError:
                end_date = None  # Если дата некорректная, игнорируем фильтрацию по дате

        # Получаем курсы, которые доступны для учителя
        teacher_id = current_user.id  # Для теста можно использовать статическое значение
        courses = Course.query.filter_by(tutor_id=teacher_id).all()

        if data_type == 'attendance':
            attendance_records = []
            for course in courses:
                if course_filter and str(course.id) != course_filter:
                    continue  # Пропустить курс, если фильтр не совпадает
                lessons = Lesson.query.filter_by(course_id=course.id).all()
                for lesson in lessons:
                    attendance_records.extend(Attendance.query.filter_by(lesson_id=lesson.id).all())

            # Фильтрация по датам
            if start_date:
                attendance_records = [a for a in attendance_records if a.lesson.date >= start_date]
            if end_date:
                attendance_records = [a for a in attendance_records if a.lesson.date <= end_date]

            # Фильтрация по студенту
            if student_filter:
                attendance_records = [a for a in attendance_records if student_filter.lower() in a.student.full_name.lower()]

            # Фильтрация по группе
            if group_filter:
                attendance_records = [a for a in attendance_records if group_filter.lower() in a.student.group.lower()]

            # Экспорт в Excel
            wb = Workbook()
            ws = wb.active
            ws.append(["Student Name", "Course Name", "Lesson Date", "Status", "Comments", "Reason of Excuse"])

            for record in attendance_records:
                student_name = record.student.full_name
                course_name = record.lesson.course.name
                lesson_date = record.lesson.date
                status = record.status
                comments = record.comments
                reason_of_excuse = record.reason_of_excuse
                ws.append([student_name, course_name, lesson_date, status, comments, reason_of_excuse])

            # Сохранение в буфер
            output = BytesIO()
            wb.save(output)
            output.seek(0)

            # Отправка файла пользователю
            return send_file(output, as_attachment=True, download_name="attendance_export.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    else:
        # Для GET-запроса показываем форму с выбором
        teacher_id = current_user.id  # Для теста можно использовать статическое значение
        courses = Course.query.filter_by(tutor_id=teacher_id).all()

        return render_template('teacher/export.html', courses=courses)


