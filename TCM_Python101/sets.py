#!/bin/python3
# Sets
# Meistsec 10/2022
# Sets can store multiple values in one variable
# Sets can not be ordered and don't allow duplicate values

set1 = {"a", "b", "c"}
# looks similar to a dictionary. However, there is no key value defined.
print(set1)
print(type(set1))

set2 = {"a", "a", "a"}
print(set2)
print(len(set2))
# can't have a duplicate value. Hence it returns 1 in the output.

set3 = {"a", 0, True}
print(set3)
print(type(set3))

set4 = set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3)


list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set5 = {4, 5, 6}
set6 = set4.union(set4)
print(set6)

set4.remove(4)
print(set4)

set4.discard(4)
print(set4)

# since sets are unordered, using pop can give unexpected results

print(set1)
set1.pop()
print(set1)
# This is going to give you different results each time it is run because there is no order


