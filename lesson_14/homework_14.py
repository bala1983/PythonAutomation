# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об('єкт цього класу, представляючи студента. '
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.)
import self


class Student:

    def __init__(self, name, surname, age):
        self.name = name
        self.surmane = surname
        self.age = age
        self.average_score = 0

    def set_avarage_score(self, value):
        self.average_score = value
        print(f"Студент на ім'я {self.name} та прізвище {self.surmane} віком {self.age} років, "
              f"має середній бал {self.average_score}")

student = Student(name='Oleg', surname='Mishko', age=25)
student.set_avarage_score(99.8)