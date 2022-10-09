#!/bin/python3
# User input
# Meistsec 10/2022
# Notes

test = input()
print(test)

test = input("Enter the IP:")
print(test)

# Create a infinite loop
while True:
	test = input("Enter the IP: ")
	print(">>> {}".format(test))
	if test == "exit":
		break
	else:
		print("exploiting...")
