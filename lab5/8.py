import re

def split_up(a):
    x = re.split("[A-Z]", a)
    return x

print(split_up("qwertYuio"))