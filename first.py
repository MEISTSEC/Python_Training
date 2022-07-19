#!/bin/python3

#Strings
#Print String
print("Hello, World!")
print('Hello, World!')
print("""This string runs
multiple lines!""") #triple quote for multi-line
print("This string is "+"awesome!") #We can also concatenate
print('\n') #new line
print('Test that new line out.')

#MATH
print(50 + 50) #add
print(50 -50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #divsion with remainder (or a float)
print(50 // 6) #no remainder

print('\n')
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lower
print(quote.title()) #title
print(len(quote)) #counts characters

name = "JohnBoy"
age = 40 #int
gpa = 3.8 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No.

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)


print('\n')
#FUNCTIONS (Mini Programs)

def who_am_i(): #this is a function without parameters
	name = "JohnBoy" #local variable
	age = 41
	print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))