#!/bin/python3
# Dictionaries
# Meistsec 10/2022
# Dictionaries are used to store data values in key value pairs and can't have duplicate keys
# Dictionaries use curly brakets and a key colon brackets for each value

dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"])
# This is accessing a value in the dictionary
print(dict1.get("a"))
# same thing, dif syntax

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["a"] = 1
print(dict1)

dict1["d"] = 4
print(dict1)

dict1["a"] = 0
print(dict1)
# you cant add another key value of a but you can change it

dict1.update({"a": 1})
print(dict1)
# This does the same as above dif syntax

dict1.pop("d")
print(dict1)
# pop removes key values from the dictionary

del dict1['c']
print(dict1)
# same as above

dict1['c'] = {"a":1, "b":2}
print(dict1)

dict2 = {}
print(dict2)

dict3 = dict()
print(dict3)

# the two above are useful when you want to have a data structure
# but do not know yet what that data will contain




