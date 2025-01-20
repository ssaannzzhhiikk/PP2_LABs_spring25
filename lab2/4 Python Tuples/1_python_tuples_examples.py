#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2 Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#3 Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4 One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#5 String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#6 A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

