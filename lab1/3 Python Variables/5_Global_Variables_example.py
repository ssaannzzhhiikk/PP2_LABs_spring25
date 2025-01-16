#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#3 Global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#4 GLobal scope to change inside of func
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

