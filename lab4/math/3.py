import math

s = int(input("Enter number of sides: "))
l = int(input("Enter the length of a side: "))
A = int((s * l**2) / (4 * math.tan(math.pi / s)))

print("The area of the polygon is: ", A)
