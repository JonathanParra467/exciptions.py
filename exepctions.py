"""
Enhance a basic Python program by implementing try and except statements
to handle errors in user input, focusing on data type errors.
"""


def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")
    try:
        result = 10 / 5
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Division successful!")
    finally:
        print("Execution completed.")
square_number()