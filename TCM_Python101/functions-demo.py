#!/bin/python3
# Functions and Code Reuse
# Meistsec 10/2022
# Notes

def function1():
		print("hello from function!")

function1()	
function1()

def function2():
	return "Hello from function2!"

return_from_function2 = function2()
print(return_from_function2)

def function3(s):
	print("\t{}".format(s))

function3("parameter")
function3("parameter2")

def function4(s1, s2):
	print("{}{}".format(s1,s2))

function4("any","thing")
function4(s1="thing", s2="any")
function4(s2="any", s1="thing")