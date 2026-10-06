# Day 3 - Python Data Structures & File Handling

# List
students = ["Ravi", "Anu", "Kiran"]
students.append("Jagadish")
print("List:", students)

# Tuple
subjects = ("Python", "AI", "Machine Learning")
print("Tuple:", subjects)

# Dictionary
student = {"id": "101", "name": "Jagadish", "course": "AI & ML"}
print("Dictionary:", student)

# Set
skills = {"Python", "SQL", "Python", "ML"}
print("Set:", skills)

# Write to a text file
with open("practice.txt", "w", encoding="utf-8") as file:
    file.write("Python File Handling Practice\n")
    file.write("This file was created using Python.\n")

# Read from a text file
with open("practice.txt", "r", encoding="utf-8") as file:
    print("File content:")
    print(file.read())
