# By Raj Shekhar Aryal
# Simple Cli based Calculator made in python


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    # Quick guard against ZeroDivisionError
    if b == 0:
        return "Error (Cannot divide by zero)"
    return a / b


def exponent(a, b):
    return a**b


print("Welcome to Simple Calculator\n")

while True:

    print("#" * 25)
    print("Enter 'A' for addition")
    print("Enter 'B' for subtraction")
    print("Enter 'C' for multiplication")
    print("Enter 'D' for division")
    print("Enter 'E' for exponent")
    print("Enter 'Q' to quit")
    print("#" * 25)


    choice = input("Enter your choice: ").upper()


    if choice == "Q":
        print("Goodbye!")
        break


    if choice not in ["A", "B", "C", "D", "E"]:
        print("Please enter a valid option\n")
        continue


    print("#" * 25)
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    print("#" * 25)


    if choice == "A":
        print(f"Result: {a} + {b} = {addition(a, b)}\n")
    elif choice == "B":
        print(f"Result: {a} - {b} = {subtraction(a, b)}\n")
    elif choice == "C":
        print(f"Result: {a} * {b} = {multiplication(a, b)}\n")
    elif choice == "D":
        print(f"Result: {a} / {b} = {division(a, b)}\n")
    elif choice == "E":
        print(f"Result: {a} ^ {b} = {exponent(a, b)}\n")