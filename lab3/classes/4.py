import math

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def show(self):
        print(f"The coordinates are : X:{self.X}, Y:{self.Y}")

    def move(self, X, Y):
        self.X = X
        self.Y = Y

    def dist(self, other):
        return math.sqrt((self.X - other.X) ** 2 + (self.Y - other.Y) ** 2)
    

p1 = Point(1, 2)
p2 = Point(3, 4)

p1.show()
p2.show()

p1.move(3, 12)
p1.show() 

d = p1.dist(p2)
print("The distance between p1 and p2:", d)