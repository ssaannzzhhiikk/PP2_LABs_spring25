""" Error, we cannot combine strings and numbers
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

#1 f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#2
price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  #-> The price is 59.00 dollars

#3
txt = f"The price is {20 * 59} dollars"
print(txt)