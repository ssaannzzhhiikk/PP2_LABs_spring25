import re

def _ab(text):
    if re.search("ab*", text):
        return True
    return False

with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(txt)
        print(_ab(txt))

print(40*"-")
print(_ab("This text means ab nana abb"))