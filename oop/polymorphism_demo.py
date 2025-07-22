from math import pi


class Shape:
    def area(self):
        raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)