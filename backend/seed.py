from app import create_app, db
from app.models import users, courses

app = create_app()

# Создание тестовых данных
with app.app_context():
    # Создание пользователя
    if not users.query.filter_by(email="test@example.com").first():
        test_user = users(
            name="Test User",
            email="test@example.com",
            password="hashed_password",
            role="student"
        )
        db.session.add(test_user)

    # Создание курса
    if not courses.query.filter_by(course_code="MATH101").first():
        test_course = courses(
            name="Introduction to Math",
            description="Basic math course",
            tutor_id=1,  # Замените на ID существующего преподавателя
            course_code="MATH101"
        )
        db.session.add(test_course)

    db.session.commit()
    print("Test data seeded!")
