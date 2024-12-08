from flask import Blueprint, request
from app.models import Course, User, CourseStudent ,Lesson
from datetime import date
from app import db
student_courses=Blueprint('student_courses',__name__)

@student_courses.route('/student/<int:id>/courses')
def student_courses(id):
    student=User.query.get(id)
    att_c=CourseStudent.query.filter_by(student_id=student.id).all()
    att_courses={}
    for i in range(len(att_c)):
        att_courses.update({f"att_course_{i}":{"id": str(att_c[i].course_id),
                                       "name":str(att_c[i].course.name),
                                       'count': str(len(CourseStudent.query.filter_by(course_id=att_c[i].course_id).all())),
                                       'start_date':str(att_c[i].course.start_date),
                                       'end_date': str(att_c[i].course.end_date),
                                       "status": str(att_c[i].course.status),
                                       }})

    att_c_id=[cour.course_id for cour in att_c] #id всех посещаемых курсов
    aff_c_id=[cour.id for cour in Course.query.all() if cour.id not in att_c_id]
    #id всех доступных курсов
    aff_courses={}
    for i in range(len(aff_c_id)):
        course=Course.query.filter_by(id=aff_c_id[i]).first()
        aff_courses.update({f"aff_course_{i}":{"id": str(course.id),
                                       "name":str(course.name),
                                       'count': str(len(CourseStudent.query.filter_by(course_id=course.id).all())),
                                       'start_date':str(course.start_date),
                                       'end_date': str(course.end_date),
                                       "status": str(course.status),
                                       }})
    return {'att_courses':att_courses,'aff_courses':aff_courses}

#кнопка записаться на курс будет в подробнее каждого курса
@student_courses.route('/student/<int:id>/courses/<int:course_id>',methods=['GET','POST'])
def student_all_inf_about_course(id,course_id):
    if request.method=='POST':
        new_course_entry=CourseStudent(course_id=course_id,student_id=id)
        try:
            db.session.add(new_course_entry)
            db.session.commit()
            return 'Вы записались на курс'
        except:
            return 'При записи на курс произошла ошибка'
    else:
        course=Course.query.filter_by(id=course_id).first()
        current_date=date.today()
        lessons=Lesson.query.filter_by(course_id=course_id).all()
        count=len([1 for i in lessons if i.date<current_date])
        inf={'course_id':course.id,
             'course_name':course.name,
             'amount_of_finish_lessons': str(count),
             'amount_of_lessons': str(len(lessons)),
             'amount_of_finish_lessons_in_perсentages': str(count/len(lessons)*100)+'%'
             }
        if course.link==None:
            inf.update({'link':'Ссылка на гугл диск пока не добавлена'})
        else:
            inf.update({'link': str(course.link)})
        for i in range(len(lessons)):
            inf.update({f'lesson_{i}': {'lesson_name':str(lessons[i].topic),
                                       'location':str(lessons[i].location),
                                       'date':str(lessons[i].date)
                                      }})
        return inf