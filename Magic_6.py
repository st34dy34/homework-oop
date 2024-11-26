import math 

class Shape():
    def __init__(self):
        pass
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"I am rectangle, my calculated area: {self.area()}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return f"I am Circle, my calculated area: {self.area()}"
    

class RightTriangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"I am Right Triangle, my calculated area: {self.area()}"
    

class Trapezoid(Shape):
    def __init__(self,base1, base2,height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
    def __str__(self):
        return f"I am Trapezoid, my calculated area: {self.area()}"
    

shapes = [
        Rectangle(5, 10),
        Circle(7),
        RightTriangle(6, 8),
        Trapezoid(5, 7, 4)
    ]

print("""
      Rectangle(5, 10),
        Circle(7),
        RightTriangle(6, 8),
        Trapezoid(5, 7, 4)
      """)
print()

for shape in shapes:
    print(shape)