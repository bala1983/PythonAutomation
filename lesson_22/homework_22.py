# Створення моделі даних: Створіть просту модель даних для системи управління студентами.
# Модель може містити таблиці для студентів, курсів та їх відношень.
# Кожен студент може бути зареєстрований на декілька курсів.
# Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
# Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
# Переконайтеся, що ці зміни коректно відображаються у базі даних.
# Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
# Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
# Можна використовувати будь яку ORM на Ваш вібир

import random
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = "student_course"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

    student = relationship("Student", back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    student_courses = relationship("StudentCourse", back_populates="student")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    student_courses = relationship("StudentCourse", back_populates="course")

engine = create_engine("sqlite:///students.db", echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

course_names = ["Math", "Physics", "Biology", "History", "Programming"]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()

for i in range(1, 21):
    student = Student(name=f"Student {i}")
    session.add(student)
    session.commit()
    for course in random.sample(courses, random.randint(1, 3)):
        session.add(StudentCourse(student_id=student.id, course_id=course.id))
session.commit()

new_student = Student(name="New Student")
session.add(new_student)
session.commit()
session.add(StudentCourse(student_id=new_student.id, course_id=courses[0].id))
session.commit()

math_course = session.query(Course).filter_by(name="Math").first()
print("\nСтуденти на курсі Math:")
for sc in math_course.student_courses:
    print(sc.student.name)  # виводимо тільки ім'я

student1 = session.query(Student).filter_by(id=1).first()
print(f"\nКурси студента {student1.name}: {[sc.course.name for sc in student1.student_courses]}")

student1.name = "Updated Student 1"
session.commit()

student2 = session.query(Student).filter_by(id=2).first()
session.delete(student2)
session.commit()