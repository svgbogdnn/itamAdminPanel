'''from flask import Blueprint,request,redirect
from app.models import Attendance,User,Feedback,Lesson
from app import db

student_feedback=Blueprint('student_feedback',__name__)

@student_feedback.route('/student/<int:id>/feedback',methods=['POST','GET'])
def student_feedback(id):
    attendance = Attendance.query.filter_by(student_id=id).all()
    if request.method=='GET':
        inf={}
        for i in range(len(attendance)):
            feedback={'lesson_id':str(attendance[i].lesson_id),
                          'course_name':str(attendance[i].lesson.course.name),
                                   'tutor_fullname':str(User.query.filter_by(id=attendance[
                                       i].lesson.course.tutor_id).first().full_name),
                                    'date':str(attendance[i].lesson.date)
                                    }
            if not(Feedback.query.filter_by(student_id=id,lesson_id=attendance[i].lesson.id).first())==None:
                add_feedback={'mark':str(Feedback.query.filter_by(student_id=id,lesson_id=attendance[i].lesson.id).first().mark),
                          'comment':str(Feedback.query.filter_by(student_id=id,lesson_id=attendance[i].lesson.id).first().comment)
                          }
            else:
                add_feedback={'mark':'','comment':''}
            feedback.update(add_feedback)
            inf.update({f'{i}':feedback})
        sorted_inf=dict(
            sorted(inf.items(), key=lambda item: item[1]['date']) #кортеж пары, сортировка по ключу второй элемент
            # кортежа ключ-date
            )
        return sorted_inf
    else:
        mark=request.form['mark']
        comment=request.form['comment']
        lesson_id = request.form['lesson_id'] #как нибудь это передать скрыто
        new_feedback=Feedback(lesson_id=lesson_id,student_id=id,
                              course_id=Lesson.query.filter_by(id=lesson_id).first().course_id,
                              mark=mark, comment=comment)
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(f'/student/{id}/feedback')
'''