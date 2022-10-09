#!/bin/python3
# Loops
# Meistsec 10/2022
# Loops

a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)

# While loop
a = 1
while a < 5:
	a += 1 # This is the exit function for the loop
	print(a)

# making a space
print()

# For loop
for i in [0, 1, 2, 3, 4]:
	print(i+6)

print("---")

for i in range(5): # Same as above for the for loop
	print(i+6)

for i in range(3):
	for j in range(3):
		print(i,j)
print("---")

# Break, Continue, and Pass
for i in range(5):
	if i == 2:
		break
	print(i)

for i in range(5):
	if i == 2:
		continue
	print(i)

print("---")

for i in range(5):
	if i == 2:
		pass
	print(i)

for c in "string":
	print(c)

for key, value in {"a":1, "b":2, "c":3}.items():
	print(key, value)