from itertools import permutations 

def p(s):
    new = permutations(s)
    return new


a = input()
s = p(a)
for i in s:
    print(*i)
