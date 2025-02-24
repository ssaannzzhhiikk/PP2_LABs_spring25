from functools import reduce

def multiply_list(lst):
    return reduce(lambda a, b: a * b, lst)

n = [1, 2, 3, 4, 5, 6]
print(multiply_list(n))