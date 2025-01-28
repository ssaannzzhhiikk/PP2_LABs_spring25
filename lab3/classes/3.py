class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.lenght = length
        self.width = width

    def area(self):
        return self.width * self.lenght

shape = Shape()
print("Area of shape:", shape.area())

rect = Rectangle(3, 4)
print("Area of Rectangle:", rect.area())
    
        