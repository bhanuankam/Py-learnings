"""Homework-style conditionals — one function per exercise. Run the file and pick a number."""


def exercise_1_grade() -> None:
    """Letter grade from marks (0–100)."""
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Please enter a number.")
        return
    if not 0 <= marks <= 100:
        print("Marks should be between 0 and 100.")
        return
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")


def exercise_2_largest() -> None:
    """Largest of three numbers."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
    except ValueError:
        print("Please enter numbers only.")
        return
    if a >= b and a >= c:
        print("A is largest of three")
    elif b >= a and b >= c:
        print("B is largest of three")
    else:
        print("C is largest")


def exercise_3_leap_year() -> None:
    """Leap year (Gregorian rules)."""
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Please enter a whole year.")
        return
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if leap:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def exercise_4_discount() -> None:
    """10% discount if amount ≥ 1000."""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a number.")
        return
    if amount >= 1000:
        discount = amount * 0.10
        print("Discount is", discount)
        print("Discounted price is", amount - discount)
    else:
        print("No discount")


def exercise_5_discount_message() -> None:
    """Print discount rule only (no calculation)."""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a number.")
        return
    if amount >= 1000:
        print("10% discount")
    else:
        print("No discount")


def exercise_6_calculator() -> None:
    """Simple + - * / on two integers."""
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    except ValueError:
        print("Please enter whole numbers.")
        return
    operator = input("Enter operator (+, -, *, /): ").strip()
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(a / b)
    else:
        print("Unknown operator.")


def exercise_7_temperature() -> None:
    """Hot above 30; you can extend with warm/cold bands."""
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a number.")
        return
    if temp > 30:
        print("Hot")
    elif 20 < temp <= 30:
        print("Warm")
    elif temp < 20:
        print("Cold")
    else:
        print("Thanks")


def exercise_8_vowel() -> None:
    """Single letter vowel check."""
    ch = input("Enter a letter: ").strip().lower()
    if len(ch) != 1 or not ch.isalpha():
        print("Please enter one letter.")
        return
    if ch in "aeiou":
        print("Entered value is a vowel")
    else:
        print("Consonant")


def exercise_9_vowel_or_consonant() -> None:
    """Same idea as #8 with explicit consonant label."""
    ch = input("Enter a character: ").strip().lower()
    if len(ch) != 1 or not ch.isalpha():
        print("Please enter one letter.")
        return
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")


def exercise_10_weekday() -> None:
    """Map 1–7 to weekday name."""
    try:
        n = int(input("Enter number (1–7): "))
    except ValueError:
        print("Please enter a whole number.")
        return
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    if n in days:
        print(days[n])
    else:
        print("Enter between 1–7")


def exercise_11_three_digits() -> None:
    """True three-digit positive integer: 100–999."""
    try:
        n = int(input("Enter number: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if 100 <= n <= 999:
        print("Number is three digits:", n)
    else:
        print("Number is not three digits:", n)


EXERCISES = {
    "1": exercise_1_grade,
    "2": exercise_2_largest,
    "3": exercise_3_leap_year,
    "4": exercise_4_discount,
    "5": exercise_5_discount_message,
    "6": exercise_6_calculator,
    "7": exercise_7_temperature,
    "8": exercise_8_vowel,
    "9": exercise_9_vowel_or_consonant,
    "10": exercise_10_weekday,
    "11": exercise_11_three_digits,
}


def main() -> None:
    print("Homework exercises — enter 1–11, or blank for 1 (grade).")
    choice = input("Exercise: ").strip() or "1"
    fn = EXERCISES.get(choice)
    if fn is None:
        print("Unknown choice. Use 1–11.")
        return
    fn()


if __name__ == "__main__":
    main()
