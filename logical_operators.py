# Logical operators: combine or invert boolean conditions (and, or, not).

def show(expr: str, value: bool) -> None:
    print(f"{expr:20} -> {value}")


print("and: True only if both sides are True")
show("True and False", True and False)
show("False and True", False and True)
show("False and False", False and False)
show("True and True", True and True)

print()
print("or: True if at least one side is True")
show("True or False", True or False)
show("False or True", False or True)
show("True or True", True or True)
show("False or False", False or False)

print()
print("not: inverts True/False")
show("not True", not True)
show("not False", not False)
