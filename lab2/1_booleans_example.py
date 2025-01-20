#1
print(10 > 9) #T
print(10 == 9) #F
print(10 < 9) #F

#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") # -> b is not greater than a

#3
print(bool("Hello")) # -> T
print(bool(15)) #-> T


#4
x = "Hello"
y = 15

print(bool(x)) #-> T
print(bool(y)) #-> T

#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) #all of them returns T

#6 The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7 One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8
def myFunction() :
  return True

print(myFunction())  #-> True

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")  #-> YES!
else:
  print("NO!")

#10 var, type   
x = 200
print(isinstance(x, int))