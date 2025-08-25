from abc import abstractmethod

class Figura:
    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Triangle(Figura):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_square(self):
        square = (self.__side_a + self.__side_b)/2
        return square

    def get_perimeter(self):
        perimeter = self.__side_a + self.__side_b + self.__side_c
        return perimeter

    def __str__(self):
        return f"Наш трикутник має строну А: {self.__side_a}, сторону Б: {self.__side_b}, сторону С: {self.__side_c}"

    def get_sides(self):
        list_sides = [self.__side_a, self.__side_b, self.__side_c]
        return list_sides

class Quadrat(Figura):
    def __init__(self, side_a):
        self.__side_a = side_a

    def get_square(self):
        square = self.__side_a ** 2
        return square

    def get_perimeter(self):
        perimeter = self.__side_a * 4
        return perimeter

    def __str__(self):
        return f"Наш квадрат має сторону А: {self.__side_a}"

    def get_sides(self):
        return self.__side_a

t = Triangle(5, 10, 15)
q = Quadrat(10)
t.get_perimeter()
t.get_sides()
q.get_sides()
print(t.get_sides())
print(t.get_square())
print(q.get_perimeter())
print(t)
print(q)