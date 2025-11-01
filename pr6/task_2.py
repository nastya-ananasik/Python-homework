from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(13)
rectangle = Rectangle(5, 10)
triangle = Triangle(31, 10)

print(f"Площа кола: {circle.calculate_area():.2f}")
print(f"Площа прямокутника: {rectangle.calculate_area()}")
print(f"Площа трикутника: {triangle.calculate_area()}")
