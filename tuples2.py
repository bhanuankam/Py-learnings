#HW3
numbers = [i for i in range(10)]
print(numbers)

#2
numbers = [i for i in range(1,20) if i % 2 == 1]
print(numbers)

#3
numbers = [i for i in reversed(range(1,11))]
print(numbers)

### 4️⃣ Calculate the sum of the first 20 natural numbers
#Sum = 1 + 2 + ... + 20 = 210
#4
"""
lst_num = [i for i in range(1,21)]
total=0
for num in lst_num:
    total=total+num
print(total)


total=0
for num in range(1,21):
    total=total+num
print(total)

"""

"""
number=int(input("Enter number :"))
for i in range(1,11):
    print(i,"x",number, "=", number * i)


"""