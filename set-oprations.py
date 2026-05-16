#set operations
a = {1,2,3}
b = {2,3,4}
print(a | b) # union
print(a & b) # intersection
print(b - a) # difference


#subset
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True
print(B.issubset(A))   # True

#symmetric difference
l1 = [1,2,3]
l2 = [3,4,5]
set1 = set(l1)
set2 = set(l2)
print(set1 ^ set2) #symmetric difference
