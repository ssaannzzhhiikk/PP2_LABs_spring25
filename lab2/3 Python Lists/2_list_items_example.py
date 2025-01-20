#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #-> banana

#2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  #-> cherry

#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  #-> ['cherry', 'orange', 'kiwi']

#4  same as [0:4]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #->  ['apple', 'banana', 'cherry', 'orange']

#5  same as [2 : maxindex-1]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  #->  ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  #->  ['orange', 'kiwi', 'melon']

#7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")