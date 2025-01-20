#1 Packing a tuple:
fruits = ("apple", "banana", "cherry")

#2 Unpacking a tuple:
fruits = ("apple", "anana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

