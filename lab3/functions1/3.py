def solve(numheads, numlegs):
    y = (numlegs- 2*numheads) / 2
    x = numheads - y

    return x, y


'''
x = numheads - y
2*(numheads - y) + 4y = numlegs

2*numheads - 2y + 4y = 94
  y = (numlegs- 2numheads) / 2
  x = numheads - y
'''


heads = int(input())
legs = int(input())
a, b = solve(heads, legs)
print(int(a), int(b))