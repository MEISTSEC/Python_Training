#!/bin/python3
# Booleans & operators
# Meistsec 10/2022

valid = True
not_valid = False

print(valid == True)
# The == is a comparison not an equal to
print(not_valid == True)

print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print(10 < 9 == True)
print((10 == 10) == True)

print((10 != 10) == True)
#!= means does not equal to. Thats the point of the exclamation point

print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 > 9) == True)

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

print(bool(0) == False)
print(bool(1) == True)

print(10 + 10)
print(10 - 10)
print(10 / 10)
print(10 // 10)

print(10 /3)
print(10 // 3)
print(10 % 3)

print(10 * 10)
print(10 ** 10)
print(10 % 10)

x = 10
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

x = 13
print(bin(x))
print(bin(x)[2:].rjust(4,"0"))

y = 5
print(bin(y)[2:].rjust(4,"0"))

print(bin(x & y)[2:].rjust(4,"0"))
print(x & y)


# & | those mean bitwise AND and OR



print(bin(x >> 1)[2:].rjust(4,"0"))
