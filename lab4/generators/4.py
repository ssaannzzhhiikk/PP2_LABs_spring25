def squares(a, b):
    for i in range(a, b+1):
        yield i*i

m = int(input())
n = int(input())

gen = squares(m, n)

for i in gen:
    print(i)