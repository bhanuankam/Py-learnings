"""
#tuples packing
Simple definition:
A tuple is an ordered collection of items that cannot be changed (immutable).
Example:
my_tuple = (1, 2, 3)
Items are in a fixed order
You cannot modify them after creation
It can store different types of data (numbers, text, etc.)
Packing / Unpacking
a = (1, 2, 3) # packing
x, y, z = a # unpacking
"""
a = (0, 1, 2, 3, 4, 5) # packing
x, y, *z = a # unpacking
print(a)
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))


#tuples are faster since they are readonly
