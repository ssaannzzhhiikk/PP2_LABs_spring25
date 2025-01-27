from math import pi as p

def volume_sphere(a):
    return 4/3 * p * a**3

radius = int(input())

print(volume_sphere(radius))