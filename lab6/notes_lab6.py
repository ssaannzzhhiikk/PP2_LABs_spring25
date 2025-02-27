import os




# 1. Reading a File
# To read a file in Python, you can use the `open()` function with the mode 'r' 'a', 'w', 'x'.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 2. Writing to a File
# To write to a file, use the `open()` function with the mode 'w' (write).
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# 3. Appending to a File
# To append to a file, use the `open()` function with the mode 'a' (append).
with open('example.txt', 'a') as file:
    file.write('\nAppended text.')

# 4. Creating a File
# A new file is created when you open a file in write or append mode that does not exist.
with open('newfile.txt', 'w') as file:
    file.write('This is a new file.')

# 5. Deleting a File
# To delete a file, you can use the `os.remove()` function from the `os` module.
os.remove('newfile.txt')

#6. To read a single line from a file, you can use the `readline()` method.
with open('example.txt', 'r') as file:
    line = file.readline()
    print(line)




# Working with Directories ====================================================================================

# 1. Creating a Directory
# To create a directory, use the `os.mkdir()` function.
os.mkdir('new_directory')

# 2. Changing the Current Working Directory
# To change the current working directory, use the `os.chdir()` function.
os.chdir('new_directory')

# 3. Listing Files in a Directory
# To list all files and directories in the current directory, use the `os.listdir()` function.
files = os.listdir('.')
print(files)

# 4. Removing a Directory
# To remove a directory, use the `os.rmdir()` function.
os.chdir('..')  # Move up to the parent directory
os.rmdir('new_directory')

#5. Deleting file
# To delete a file, you can use the `os.remove()` function from the `os` module.
os.remove('example.txt')

#6. Listing directory
# To list all files and directories in the current directory, use the `os.listdir()` function.
files = os.listdir('path')
print(files) #gives list of files in the current directory




#--------------------------------------------------------------------------------------------------------------



# Builtin function of Python

from functools import reduce

#1. reduce() Function
# The reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

# Example: Using reduce to compute the sum of a list
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)  # Output: 15



# filter() Function
# The filter() function is used to construct an iterator from elements of an iterable for which a function returns true.

# Example: Using filter to get even numbers from a list
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]



# map() Function
# The map() function applies a given function to all items in an input list.

# Example: Using map to double each number in a list
def double(n):
    return n * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# Example: Using map with a lambda function to square each number in a list
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


t = (True, True, True)
print(all(t)) # Output: True