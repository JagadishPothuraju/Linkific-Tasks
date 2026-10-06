# Simple Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("===== Simple Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    choice = int(input("Choose an operation (1-4): "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        result = add(a, b)
    elif choice == 2:
        result = subtract(a, b)
    elif choice == 3:
        result = multiply(a, b)
    elif choice == 4:
        result = divide(a, b)
    else:
        result = "Invalid choice."

    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
