#!/bin/python3
# Tuples
# Meistsec 10/2022

tuple_items = ("item1", "item2", "item3")
#A tuple is a good item to use when your data is fixed and is not going to change
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

tupel_repeat = ('Combine!',) * 4
print(tupel_repeat)
print(type(tupel_repeat))

mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

tuple_combine = tuple_items +tuple_numbers
print(tuple_combine)
print(type(tuple_combine))

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index("item2"))

tuple_items = ("item1", "item2", "item3")
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print(len(tuple_items))

print(tuple_items[-1])
print(tuple_items[-2])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])

string1 = "I am a string"
print(string1[0:4])
print(string1[:-1])

