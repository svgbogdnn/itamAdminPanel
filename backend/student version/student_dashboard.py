from flask import Blueprint,request,redirect
import json
from flask import render_template
from app.utils.models import User, Attended_course,Course,Lesson
from  datetime import date

student_dashboard_blueprint=Blueprint('student_dashboard',__name__,)



@student_dashboard_blueprint.route('/student/<int:id>', methods=['GET'])#
def student(id):
    student=User.query.get(id)
    '''notifications'''
    attended_courses=Attended_course.query.filter_by(student_id=id).all()
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
    '''notifications'''
    return {'notifications_of_nearest_lessons':notifications_of_nearest_lessons,
            'general_inf':{'name': student.full_name,'role':student.role},
            'notifications_of_feedback':notifications_of_feedback
            }







