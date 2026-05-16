#List Comprehension
#squares = [x*x for x in range(5)]
#print(squares)


nums = [1,2,3,4]
even = [z+5 for z in nums if z % 2 == 0]
print(even)

"""
#creation of the list
List comprehension in Python is a concise way to create lists using a single line of code.
It combines a loop and optional condition into one expression.
Syntax: [expression for item in iterable if condition]
It is used to make code shorter and more readable.

In Python, for is not a “command” — it is a keyword.
It is used to create a loop (called a for loop)
It lets you iterate over items like lists, strings, or ranges
It repeats a block of code for each item in a sequence
"""