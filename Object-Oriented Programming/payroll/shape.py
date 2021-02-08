from abc import ABC, abstractmethod
import math


class Shape(ABC):
    id = 0

    def __init__(self):
        Shape.id += 1
        self.id = Shape.id

    @abstractmethod
    def area(self):
        pass  # No body

    @abstractmethod
    def perimeter(self):
        pass  # No body


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius

    def area(self):
        print("Calling Circle.area")
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length, self.width = length, width

    def area(self):
        print("Calling Rectangle.area")
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        Shape.__init__(self)
        self.side1, self.side2, self.side3 = side1, side2, side3

    def area(self):
        print("Calling Triangle.area")
        # Heron's Formula:
        s1, s2, s3 = self.side1, self.side2, self.side3
        p = (s1 + s2 + s3) / 2
        return math.sqrt(p * (p - s1) * (p - s2) * (p - s3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def main():
    c = Circle(3)
    r = Rectangle(12, 35)
    t = Triangle(3, 4, 5)
    shapes = [c, r, t]
    for shape in shapes:
        print(shape.id, shape.area(), shape.perimeter())


if __name__ == "__main__":
    main()

""" Output:
Calling Circle.area
28.274333882308138
Calling Rectangle.area
420
Calling Triangle.area
6.0
"""
