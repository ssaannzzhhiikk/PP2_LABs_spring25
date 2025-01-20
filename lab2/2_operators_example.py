#1
print(10 + 5)

"""
Python divides the operators in the following groups:
Arithmetic operators   +, -, *, /, %, **, //
Assignment operators  =, +=, &=, |=, >>= 
Comparison operators   ==, !=, >=
Logical operators   and, or, not
Identity operators  is, is not
Membership operators    in, not in
Bitwise operators  &, |, ^, <<
"""


#2 Operator Precedence
print((6 + 3) - (6 + 3))

#3
print(100 + 5 * 3)

#4 If two operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3)

''' highest precedence at the top:

()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR

'''