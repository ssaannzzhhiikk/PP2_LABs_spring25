class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght
    
    def area(self):
        return self.lenght**2
    
shape = Shape()
print("Area of shape:", shape.area())

square = Square(4)
print("Area of square:", square.area())  # Output: 16
    
        