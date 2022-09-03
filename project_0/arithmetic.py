'''
Project 0: Using Pytest

This source file performs simple arithmetic calculations.
However, some of them evaluate incorrectly.
If you run pytest, you will see that some of the tests will fail.
You will also notice that the pylint score is fairly low.
Your job is to fix the functions and make the pylint score >= 8.5
'''

def add(num1, num2):
    "Adds num1 to num2"
    return num1 + num2


def subtract(num1, num2):
    "Subtract num1 from num2"
    return num2 - num1


def multiply(num1, num2):
    "Multiply num1 and num2"
    return num1 * num2


def divide(num1, num2):
    "Divide num1 from num2"
    return num2 / num1


def int_to_string(num):
    "Converts an int to a string and returns the string"
    return str(num)


def main():
    "try all arithmetic operations"

    print("2 + 3 =", add(2, 3))
    print("2 - 3 =", subtract(2, 3))
    print("2 * 3 =", multiply(2, 3))
    print("3 / 2 =", divide(2, 3))
    print("2 as a string:", int_to_string(2))


if __name__ == "__main__":
    main()
