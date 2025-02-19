import re

def _abb(text):
    if re.search("ab{2}", text) and re.search("ab{3}", text):
        return True
    return False


with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(txt)
        print(_abb(txt))

print(40*"-")

print(_abb("Lorem Ipsum ab abb abbb"))
