# Student Grade Calculator

print("===== Student Grade Calculator =====")
name = input("Enter student name: ")

try:
    subjects = int(input("Enter number of subjects: "))
    if subjects <= 0:
        print("Number of subjects must be greater than 0.")
    else:
        marks = []
        for i in range(subjects):
            while True:
                try:
                    mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    print("Enter marks between 0 and 100.")
                except ValueError:
                    print("Enter a valid number.")

        total = sum(marks)
        average = total / subjects

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        result = "Pass" if average >= 50 else "Fail"

        print("\n===== Result =====")
        print("Student:", name)
        print("Total:", total)
        print("Average:", round(average, 2))
        print("Grade:", grade)
        print("Result:", result)
except ValueError:
    print("Please enter valid input.")
