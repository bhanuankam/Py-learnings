"""
#1. Create a list of numbers from 1 to 5 and print the third element.

nums = [i for i in range(1,6)]
#nums = [1,2,3,4,5]
print(nums)
print(nums[2])


"""
#2. Write a program to add an element `10` to a list and then sort it.
""" 
#2. Write a program to add an element `10` to a list and then sort it.

#nums = [i for i in range(6)]
nums = [5,2,8,1,6]
nums.append(100)
nums.sort()
print(nums)

"""
"""
#3. Given `a = [1,2,3,4,5]`, use slicing to print the last 3 elements.
a = [1,2,3,4,5]
print(a[2:5])

"""
"""
#4. Create a nested list and access the element `4` from `[[1,2],[3,4]]`.
a = [[1,2],[3,4],[5,6]]
print(a[1][1],a[2][0])

"""
#5. Using list comprehension, create a list of squares for numbers from 1 to 6.
squares = [i*i for i in range(1,7) if i % 2 == 0] 
squares = [i*i for i in range(1,7) if i % 2 != 0] #opposite of even
print(squares)

""" 
"