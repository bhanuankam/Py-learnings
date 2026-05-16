#nums = int(input("Enter number:"))
nums = [1,2,3,4,5,6,7,8]
odd = [x for x in nums if x % 2 != 0]
even = [x for x in nums if x % 2 == 0]
print("these are odd numbers",odd)
print("these are even numbers",even)