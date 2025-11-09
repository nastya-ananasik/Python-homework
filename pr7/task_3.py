from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

class Square(GeometricFigure):
    def __init__(self, side):
        self._side = side

    def set_side(self, side):
        self._side = side

    def get_area(self) -> float:
        return self._side ** 2

def print_area(figure: GeometricFigure):
    print(f"Area of the figure is: {figure.get_area()}")

rect = Rectangle(4, 5)
sq = Square(4)

print_area(rect)  # Area: 20
print_area(sq)    # Area: 16
