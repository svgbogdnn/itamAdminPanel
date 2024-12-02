from flask import Blueprint
import json
from flask import render_template
from app.utils.models import User, Attended_course,Course

student_blueprint=Blueprint('student',__name__,)



@student_blueprint.route('/student/<int:id>')#
def student(id):
    student=User.query.get(id)
    Attended_courses=Attended_course.query.filter_by(student_id=id).all()
    return render_template('student.html',student=student,Attended_courses=Attended_courses)
