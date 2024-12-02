from flask import Blueprint,render_template
from app.utils.models import Course

courses_blueprint=Blueprint('courses',__name__,)

@courses_blueprint.route('/courses/<int:id>')
def course(id):
    course=Course.query.get(id)
    return render_template('cousre.html')


