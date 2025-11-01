class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rect1 = Rectangle(15, 3)
rect2 = Rectangle(4, 23)

area1 = rect1.calculate_area()
print(f"{rect1.width}x{rect1.height}: {area1}")
area2 = rect2.calculate_area()
print(f"{rect2.width}x{rect2.height}: {area2}")
