#!/bin/python3
# Reading and Writing Files
# Meistsec 10/2022
# Notes

f = open('top-100.txt')
print(f)

f = open('top-100.txt', 'rt')
print(f)
# mode is read/text

#print(f.read())

print("---")

print(f.readlines())
print(f.readlines())
# this wont work an will return nothing because you already read to the end of the file
# do this below with seek
f.seek(0)
print(f.readlines())

f.seek(0)
for line in f:
	print(line.strip())

f.close()

#f = open("test.txt", "w")

f = open("test.txt", "a")
f.write("test line two!")
f.close()	
# instead of w for write mode use a for append mode

print(f.name)
print(f.closed)
print(f.mode)

with open('rocky.txt', encoding='latin-1') as f:
	for line in f:
		pass