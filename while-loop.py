"""
while Loop
Used when the number of iterations is not fixed and depends on a condition.
🔹 Example:
i = 0
while i < 5:
    print(i)
    i += 1
🔹 Theory:
Loop runs as long as condition is True
i += 1 increases value to avoid infinite loop
If condition never becomes False → infinite loop
👉 Used for condition-based repetition
"""
i = 123987456938456734560123987456938456734560123987456938456734560
for i in range(100,1000000000,100):
    print(i)
    i = i + 1
#    0 = 0 + 1 = 1

#important point
i = 5 #(start like in range)
while i < 105: #(end like in range)
    print(i)
    i = i+5 #(step like in range)
