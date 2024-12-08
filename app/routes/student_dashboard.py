'''from flask import Blueprint,request,redirect
import json
from flask import render_template
from app.models import User, CourseStudent,Course,Lesson
from  datetime import date

student_dashboard = Blueprint('student_dashboard', __name__)

@student_dashboard.route('/student/<int:id>', methods=['GET'])#
def student(id):
    student=User.query.get(id)
    attended_courses=CourseStudent.query.filter_by(student_id=id).all()
    all_lessons=[]
    for i in attended_courses:
        course_lessons=Lesson.query.filter_by(course_id=i.course_id).all()
        all_lessons+=course_lessons
    all_lessons=sorted(all_lessons,key=lambda h: h.date)
    notifications_of_nearest_lessons={}
    count=0
    for i in all_lessons:
        if (0<=(i.date-date.today()).days<=7):
            notifications_of_nearest_lessons.update({f'{count}':{
                'name_of_lesson':str(i.topic),
                'date_of_lesson':str(i.date),
                'start_time':str(i.start_time),
                'location':str(i.location)
            }})
            count+=1
    notifications_of_feedback = {}
    count = 0
    for i in all_lessons:
        if (0 < (date.today()-i.date).days <= 7):
            notifications_of_feedback.update({f'{count}': {
                'name_of_lesson': str(i.topic),
                'date_of_lesson': str(i.date),
            }})
            count += 1
    return {'notifications_of_nearest_lessons':notifications_of_nearest_lessons,
            'general_inf':{'name': student.full_name,'role':student.role},
            'notifications_of_feedback':notifications_of_feedback
            }
'''
'''from flask import Blueprint, request, jsonify
from app.models import User, CourseStudent, Course, Lesson
from datetime import date

student_dashboard = Blueprint('student_dashboard', __name__)

@student_dashboard.route('/<int:id>', methods=['GET'])
def student(id):
    student = User.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    attended_courses = CourseStudent.query.filter_by(student_id=id).all()
    all_lessons = []

    for course in attended_courses:
        course_lessons = Lesson.query.filter_by(course_id=course.course_id).all()
        all_lessons += course_lessons

    all_lessons = sorted(all_lessons, key=lambda h: h.date)

    notifications_of_nearest_lessons = []
    for lesson in all_lessons:
        if 0 <= (lesson.date - date.today()).days <= 7:
            notifications_of_nearest_lessons.append({
                'name_of_lesson': str(lesson.topic),
                'date_of_lesson': str(lesson.date),
                'start_time': str(lesson.start_time),
                'location': str(lesson.location)
            })

    notifications_of_feedback = []
    for lesson in all_lessons:
        if 0 < (date.today() - lesson.date).days <= 7:
            notifications_of_feedback.append({
                'name_of_lesson': str(lesson.topic),
                'date_of_lesson': str(lesson.date),
            })

    return jsonify({
        'notifications_of_nearest_lessons': notifications_of_nearest_lessons,
        'general_inf': {'name': student.full_name, 'role': student.role},
        'notifications_of_feedback': notifications_of_feedback
    })
'''