N = int(input())
generator = (x*x for x in range(N))

for i in generator:
    print(i)