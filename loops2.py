"""
#Loops are used to repeat a block of code multiple times until a condition is met.
for Loop + range()
The for loop is used when you know how many times to repeat.
🔹 Example:
for i in range(1,21):
    print(i)
🔹 Theory:
range(5) generates numbers → 0, 1, 2, 3, 4
Loop runs 5 times
i takes each value one by one
👉 Used for count-controlled loops
"""
for i in range(10,2):
    print(i)
#for i in range(10, -1, -1):
#    print(i)
for i in range(10,2,-1):
    print(i)
# here -1 is very important because start > stop so -1 is used since using 1 will bump 10 to 11...
