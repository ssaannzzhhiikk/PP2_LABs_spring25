N = int(input())

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

generator = evens(N)

numbers = ",".join(str(x) for x in generator)

print(numbers)