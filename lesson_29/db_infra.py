import random
from sqlalchemy import create_engine
from courses import Course
from declarative_base import Base
from sqlalchemy.orm import sessionmaker
from students import Student

def init_db():
    engine = create_engine("postgresql://test_user:test_password@localhost:5432/test_db")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

Session = init_db()

def default_values():
    session = Session()
    course_names = ["Math", "Physics", "Biology", "History", "Programming"]
    courses = [Course(name=name) for name in course_names]
    session.add_all(courses)
    for i in range(1, 21):
        student = Student(name=f"Student {i}")
        session.add(student)
        session.commit()
        for course in random.sample(courses, random.randint(1, 5)):
            session.add(Student(id=student.id, course_id=course.id))
    session.commit()
    session.close()

def show_student_by_name(name):
    session = Session()
    student = session.query(Student).filter_by(name=name).first()
    info_about_student = f"Інфо про студента {student.name}: {student.id}"
    session.commit()
    session.close()
    return info_about_student
