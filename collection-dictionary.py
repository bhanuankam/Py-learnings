"""
A dictionary is a data type used to store data in key–value pairs.
Think of it like a real dictionary:
word (key) → meaning (value)

my_dict = {
    "key1": value1,
    "key2": value2
}
"""
#Create Dictionary
d = {"name": "Ram", "age": 20}
#Access / Update
#print(d["name"])
#print(d["age"])
#print(type(d["age"]))
d["age"] = 21
d["name"] = "John"
d["address"] = "1, 2nd, banaglore"
print(d)

"""
students = {
    101: {
        "name": "Rahul",
        "age": 20,
        "course": "BCA",
        "marks": 85
    },
    102: {
        "name": "Priya",
        "age": 21,
        "course": "BBA",
        "marks": 90
    },
    103: {
        "name": "Amit",
        "age": 19,
        "course": "BSc",
        "marks": 78
    }
}
print(students[102])

"""