# RegEx in Python

import re

txt = "The rain in Spain"
# Functions for RegEx in Python =============================================================
# Check if the string starts with "The" and ends with "Spain"
x = re.search("^The.*Spain$", txt) # Output: <re.Match object; span=(0, 17), match='The rain in Spain'>

# Returns as a list all occurrences of "ai" 
y = re.findall("ai", txt) # Output: ['ai', 'ai']

# Split the string at each match character
z = re.split("\s", txt) #Output: ['The', 'rain', 'in', 'Spain']

# Replaces one or many matches with a string
w = re.sub("\s", "9", txt) #Output: The9rain9in9Spain




# Metacharacters in Python Regex =============================================================

# . - Any character (except newline character)
example1 = re.search("r.n", txt) # Output: <re.Match object; span=(4, 7), match='rai'>

# ^ - Starts with
example2 = re.search("^The", txt) # Output: <re.Match object; span=(0, 3), match='The'>

# $ - Ends with
example3 = re.search("Spain$", txt) # Output: <re.Match object; span=(12, 17), match='Spain'>

# * - Zero or more occurrences
example4 = re.search("aix*", txt) # Output: None

# + - One or more occurrences
example5 = re.search("aix+", txt) # Output: None

# ? - Zero or one occurrences
example6 = re.search("rai?", txt) # Output: <re.Match object; span=(4, 7), match='rai'>

# {} - Exactly the specified number of occurrences
example7 = re.search("a{2}", txt) # Output: None

# | - Either or
example8 = re.search("rain|Spain", txt) # Output: <re.Match object; span=(4, 8), match='rain'>

# () - Capture and group
example9 = re.search("(rain|Spain)", txt) # Output: <re.Match object; span=(4, 8), match='rain'>

# \ - Special sequence (or escape special characters)
example10 = re.search("\\bS\\w+", txt) # Output: <re.Match object; span=(12, 17), match='Spain'>




# Special Sequences =============================================================

# \A - Returns a match if the specified characters are at the beginning of the string
example11 = re.search("\AThe", txt) # Output: <re.Match object; span=(0, 3), match='The'>

# \b - Returns a match where the specified characters are at the beginning or end of a word
example12 = re.search(r"\bS\w+", txt) # Output: <re.Match object; span=(12, 17), match='Spain'>

# \B - Returns a match where the specified characters are present, but NOT at the beginning (or end) of a word
example13 = re.search(r"\Bai", txt) # Output: <re.Match object; span=(5, 7), match='ai'>

# \d - Returns a match where the string contains digits (numbers from 0-9)
example14 = re.search("\d", "The year is 2025") # Output: <re.Match object; span=(12, 13), match='2'>

# \D - Returns a match where the string DOES NOT contain digits
example15 = re.search("\D", "2025") # Output: <re.Match object; span=(0, 1), match='2'>

# \s - Returns a match where the string contains a white space character
example16 = re.search("\s", txt) # Output: <re.Match object; span=(3, 4), match=' '>

# \S - Returns a match where the string DOES NOT contain a white space character
example17 = re.search("\S", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# \w - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
example18 = re.search("\w", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# \W - Returns a match where the string DOES NOT contain any word characters
example19 = re.search("\W", txt) # Output: <re.Match object; span=(3, 4), match=' '>

# \Z - Returns a match if the specified characters are at the end of the string
example20 = re.search("Spain\Z", txt) # Output: <re.Match object; span=(12, 17), match='Spain'>




# Sets in Python Regex =============================================================

# [abc] - Returns a match where one of the specified characters (a, b, or c) is present
example21 = re.search("[abc]", txt) # Output: <re.Match object; span=(5, 6), match='a'>

# [a-z] - Returns a match for any lowercase character, alphabetically between a and z
example22 = re.search("[a-z]", txt) # Output: <re.Match object; span=(1, 2), match='h'>

# [A-Z] - Returns a match for any uppercase character, alphabetically between A and Z
example23 = re.search("[A-Z]", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# [0-9] - Returns a match for any digit between 0 and 9
example24 = re.search("[0-9]", "The year is 2025") # Output: <re.Match object; span=(12, 13), match='2'>

# [^abc] - Returns a match for any character EXCEPT a, b, and c
example25 = re.search("[^abc]", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# [a-zA-Z] - Returns a match for any character alphabetically between a and z, lower or upper case
example26 = re.search("[a-zA-Z]", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# [0-9a-zA-Z] - Returns a match for any digit or character alphabetically between a and z, lower or upper case
example27 = re.search("[0-9a-zA-Z]", txt) # Output: <re.Match object; span=(0, 1), match='T'>

# [^0-9] - Returns a match for any character EXCEPT digits
example28 = re.search("[^0-9]", "2025") # Output: None

