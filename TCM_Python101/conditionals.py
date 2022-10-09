#!/bin/python3
# Conditionals
# Meistsec 10/2022
# Make different decisions by branching depending on the outcome of both comparisons.
# The outcome of the comaprisons with the values being either true or false
# Remember Conditionals are executed in a linear order

if True:
	print("True")

if False:
	print("False")

if not False:
	print("not false")
# This is the equivalent of true

if 1 < 1:
	print("1 < 1")
elif 1 <= 1:
	print("1 <= 1")
	print("here")
else:
	print("else 1")

if 1 < 1:
	print("1 < 1")
elif 1 <= 1:
	print("1 <= 1")
elif 2 <= 2:
	print("2 <= 2")
else:
	print("else reached")

if 1 > 0 and 0 < 1:
	print("1 > 0 and 0 < 1")

if 1 > 0 and 0 < 1:
	print("1 > 0 and 0 < 1")

if (1 < 0 or 0 < 1) or 1 == 1:
	print("1 < 0 or 0 < 1")

if 0 < 1: print("0 < 1")

# In python you can use an inline turnary. 
# A turnary is an operator which is used to return a result from a conditional expression
# e.g below

if 0 < 1: print("0 < 1")
print("1 >= 1") if 1 >= 1 else print("1 < 1")

if 1 >= 1:
	print("1 >= 1")
else:
	print("1 < 1")

if 0 > 1:
	print("1")
elif 0 < 1:
	print("2")
else:
	print("3")

# The above written as a turnary below
print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")

