# Day 2 - Python Fundamentals

name = "Jagadish"
age = 21
percentage = 85.5
is_student = True

print(name, age, percentage, is_student)

# Data types
print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"name": "Jagadish"}))

# Conditional statement
marks = 75
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")

# For loop
for i in range(1, 6):
    print(i)

# While loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

print(greet("Jagadish"))
print("Sum:", add_numbers(10, 20))
