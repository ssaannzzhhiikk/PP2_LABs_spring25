import re

def replace_SpCoDo_col(text):
    return re.sub("[ ,.]", ":", text)

with open("row.txt", 'r', encoding="utf-8") as file:
    for txt in file:
        txt = txt.strip()
        print(replace_SpCoDo_col(txt))

print(40*"-")
print(replace_SpCoDo_col("Lorem Ipsum. Heavy,Rain"))