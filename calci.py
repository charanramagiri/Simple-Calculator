import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return abs(a-b)

def multiply(a, b):
    return a*b

def divide(a, b):
    

    

def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    print(f"Values received: a = {a}, b = {b}")
    #1st function
    print(f"Addition of {a} and {b} is {add(a,b)}")
    #2nd function
    print(f"Multiplication of {a} and {b} is {multiply(a,b)}")
    #3rd function
    print(f"Subtraction of {a} and {b} is {subtract(a,b)}")
    #4th function
    print(f"Division of {a} and {b} is {divide(a,b)}")

if __name__ == "__main__":
    calculator()
