import re

def sq_lowercase(text):
    return re.findall(r"\b[a-z]+_[a-z]+\b", text)

with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(txt)
        print(sq_lowercase(txt))

print(40*"-")

print(sq_lowercase("lorem_ipsum aaa a_b  Asd_sdA"))
