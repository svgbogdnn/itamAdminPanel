from flask import Blueprint,request,redirect
import json
from flask import render_template
from app.utils.models import User, Attended_course,Course,Lesson

student_blueprint=Blueprint('student',__name__,)



@student_blueprint.route('/student/<int:id>', methods=['GET','POST'])#
def student(id):
    student=User.query.get(id)
    Attended_courses=Attended_course.query.filter_by(student_id=id).all()
    if request.method=='POST':
        student_id = request.form['student_id']
        if student_id:
            return redirect(f'/student/get_new_course/{student_id}')
        else:
            course_id=request.form['course_id']
            return redirect(f'/student/courses/{course_id}')
    return render_template('student.html',student=student,Attended_courses=Attended_courses)

@student_blueprint.route('/student/get_new_course/<int:id>')
def get_new_course(id):
    student=User.query.get(id)
    attended_courses=Attended_course.query.filter_by(student_id=student.id).all()
    courses=Course.query.all()
    attended_courses_id=([i.course_id for i in attended_courses])
    not_attended_courses_id=[]
    for i in range(1,Course.query.count()+1):
        if i not in attended_courses_id:
            not_attended_courses_id.append(i)
    not_attended_courses=([Course.query.filter_by(id=i).first() for i in not_attended_courses_id])
    pass


@student_blueprint.route('/student/courses/<int:course_id>',methods=['POST','GET'])
def cousre(course_id):
    course=Course.query.get(course_id)
    lessons=Lesson.query.filter_by(course_id=course_id).all()
    tutor=User.query.filter_by(id=course.tutor_id).first()
    if request.method=='POST':
        lesson_id = request.form['lesson_id']
        return redirect(f'/student/lessons/{lesson_id}')
    return render_template('course.html',course=course,lessons=lessons,tutor=tutor)

@student_blueprint.route('/student/lessons/<int:lesson_id>')
def lesson(lesson_id):
    lesson=Lesson.query.get(lesson_id)
    return render_template('lesson.html')


