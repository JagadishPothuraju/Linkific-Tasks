import numpy as np

print("=" * 45)
print("       STUDENT MARKS ANALYSIS")
print("=" * 45)

students = np.array(["Jagadish", "Rahul", "Anu", "Kiran", "Suresh"])
marks = np.array([85, 78, 95, 88, 76])

print("\nStudent Marks:")
for name, mark in zip(students, marks):
    status = "Pass" if mark >= 40 else "Fail"
    print(f"{name:<10} : {mark:>3} - {status}")

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

print("\nMARKS ANALYSIS")
print("-" * 45)
print(f"Total Marks   : {total}")
print(f"Average Marks : {average:.2f}")
print(f"Highest Marks : {highest} ({students[np.argmax(marks)]})")
print(f"Lowest Marks  : {lowest} ({students[np.argmin(marks)]})")
print("\nStudents above average:", students[marks > average])
print("Students below average:", students[marks < average])
print("\nAnalysis completed successfully!")
