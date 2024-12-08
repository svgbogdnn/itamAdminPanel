from flask import Blueprint
from app.utils.models import Attendance,User


student_attendance_blueprint=Blueprint('student_attendance',__name__)

@student_attendance_blueprint.route('/student/<int:id>/attendance')
def student_attendance(id):
    attendance=Attendance.query.filter_by(student_id=id).all()
    attendance_inf={}
    for i in range(len(attendance)):
        tutor=User.query.filter_by(id=attendance[i].lesson.course.tutor_id).first()
        attendance_inf.update({f'entry_{i}':{
            'tutor_name': str(tutor.full_name),
            'course':str(attendance[i].lesson.course.name),
            'date':str(attendance[i].lesson.date),
            'status':str(attendance[i].status)
                                         }})

    return attendance_inf

