def all_true(tup):
    all(tup)


t1 = (True, True, True, True, True, True, True, True)
t2 = (True, True, False, True, True, True, True, True)
print(all(t1))
print(all(t2))
