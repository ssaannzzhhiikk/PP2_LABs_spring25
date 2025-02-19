import re

def _ab(text):
    return bool(re.search("^a.*b$", text))

with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(txt)
        print(_ab(txt))

print(40*"-")

print(_ab("abracadabrab"))
print(_ab("ab"))
print(_ab("bed"))