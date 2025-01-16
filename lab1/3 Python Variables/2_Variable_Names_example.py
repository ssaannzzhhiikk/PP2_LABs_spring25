""" Rules for var:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#1 Legal var.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#2 Illegal
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#3 Camel Case
myVariableName = "John"

#4 Pascal case
MyVariableName = "John"

#5 Snake case
my_variable_name = "John"