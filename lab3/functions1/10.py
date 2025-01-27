def setik(a):
    unique = []
    for i in a:
        if i not in unique:
            unique.append(i)
    return unique

a = list(map(int, input().split()))

print(setik(a))