#sets
"""
A set in Python is a collection of unique elements that is unordered and mutable.
Key points:
Written using curly braces → { }
Stores only unique values (duplicates are automatically removed)
Elements are not ordered (no indexing like lists/tuples)
Example:
s = {1, 2, 3, 3}
print(s)  # Output: {1, 2, 3}
Why use sets?
To remove duplicates
Fast membership testing (in)
Useful for mathematical operations like union, intersection

"mutable" means they can be changable

"""
#z = (1, 2, 3, 3, 2, 1, 4, 5) #tuples
s = {1, 2, 3, 3, 2, 1, 4, 5} #set
#print(s[0])
#s.add(6)
#print(s)
s.remove(5)
print(s)
