#Iterartors, Generators, Scope, Modules, Dates, Math, JSON

import datetime
import math
import json


# Python Iterators ===============================================================
print("Python Iterators")

class MyNumbers:
    def __iter__(self): #to make the object iterable
        self.a = 1
        return self

    def __next__(self): #to make the object an iterator
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))  # Output: 1
print(next(myiter))  # Output: 2
print(next(myiter))  # Output: 3
print(next(myiter))  # Output: 4
print(next(myiter))  # Output: 5



# Python Generators ==============================================================
print("\nPython Generators")
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3



# Python Scope ===================================================================
print("\nPython Scope")
def my_function():
    x = 10  # Local scope
    print(x)  # Output: 10

x = 20  # Global scope
my_function()
print(x)  # Output: 20

# Python Modules
print("\nPython Modules")
print(math.sqrt(16))  # Output: 4.0




# Python Dates ==================================================================
print("\nPython Dates")
now = datetime.datetime.now()
print("Current date and time:", now)  # Output: Current date and time

# Getting specific parts of the date and time
print("Year:", now.year)  # Output: Current year
print("Month:", now.month)  # Output: Current month
print("Day:", now.day)  # Output: Current day
print("Hour:", now.hour)  # Output: Current hour
print("Minute:", now.minute)  # Output: Current minute
print("Second:", now.second)  # Output: Current second

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") #"%A-day of week(monday..), %d %B-month, %Y"
print("Formatted date:", formatted_date)  # Output: Formatted date in YYYY-MM-DD HH:MM:SS format

# Creating a specific date
specific_date = datetime.datetime(2023, 10, 5, 14, 30, 0)
print("Specific date:", specific_date)  # Output: 2023-10-05 14:30:00




# Python Math ===================================================================
print("\nPython Math")
print(math.pi)  # Output: 3.141592653589793
print(math.factorial(5))  # Output: 120
print(math.radians(12))


# Python JSON ====================================================================
print("\nPython JSON")
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data) #py -> json

print(json_data)  # Output: {"name": "John", "age": 30, "city": "New York"}


#to open the json file:
with open("sample-data.json", "r") as file:
    data = json.load(file)