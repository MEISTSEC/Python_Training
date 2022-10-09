#!/bin/python3
# Exceptions and Error Handling
# Meistsec 10/2022
# Notes

print(1)
print(2)

try:
	f = open('asdfasdfasd')
except:
	print("the file does not exist!")

try:
	alskdfjlkasdjf
	f = open("aldksjflasdjf")
except FileNotFoundError:
	print("the file does not exist!")
except Exception as e:
	print(e)
finally:
	print("this message!")

n = 100
if n == 0:
	raise Exception("n can't be 0!")
if type(n) is not int:
	raise Exception("n must be an int!")

print(1/n)

# Similar example written as an assertion
n = 0
assert(n != 0)
print(1/n)