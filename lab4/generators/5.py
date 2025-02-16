n = int(input())

gen = (x for x in range(n, -1, -1))

for i in gen:
    print(i)