from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

shapes = [Rectangle(10, 20), Circle(5)]
calculator = AreaCalculator(shapes)
print(f"Total area: {calculator.total_area():.2f}")
