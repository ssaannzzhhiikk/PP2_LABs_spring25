import re

def up_lwr(text):
    return re.findall("[A-Z]{1}[a-z]+", text)

with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(txt)
        print(up_lwr(txt))

print(40*"-")
print(up_lwr("Asasa dj khaled Drake"))