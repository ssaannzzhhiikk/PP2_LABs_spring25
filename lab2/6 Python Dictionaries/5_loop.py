thisdict = []

#1 Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)


#2 Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])


#3 You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)


#4 Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)