N = int(input())

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

generator = evens(N)

for x in generator:
    print(x)