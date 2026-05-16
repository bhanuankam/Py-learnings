'''for i in range(5):
 if i == 3:
     break # stop
 print(i)

for i in range(5):
    if i == 3:
        continue # skip
    print(i)

for i in range(3):
    pass

for i in range(3):
    for j in range(2):
        print(i, j)
'''
#Basic List
nums = [1,2,3]
sq = [x*x for x in nums]
print(sq)