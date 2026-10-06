# Student Record Management System

FILE_NAME = "students.txt"

def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    marks = input("Enter marks: ").strip()

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{student_id}|{name}|{age}|{course}|{marks}\n")
    print("Student record added successfully.")

def view_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No student records found.")
        return

    if not records:
        print("No student records found.")
        return

    print("\n===== Student Records =====")
    for record in records:
        data = record.strip().split("|")
        if len(data) == 5:
            print(f"ID: {data[0]} | Name: {data[1]} | Age: {data[2]} | Course: {data[3]} | Marks: {data[4]}")

def search_student():
    search_id = input("Enter student ID to search: ").strip()
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No student records found.")
        return

    for record in records:
        data = record.strip().split("|")
        if len(data) == 5 and data[0] == search_id:
            print("\nStudent found:")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Course:", data[3])
            print("Marks:", data[4])
            return
    print("Student not found.")

def delete_student():
    delete_id = input("Enter student ID to delete: ").strip()
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No student records found.")
        return

    new_records = []
    deleted = False
    for record in records:
        data = record.strip().split("|")
        if len(data) == 5 and data[0] == delete_id:
            deleted = True
        else:
            new_records.append(record)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.writelines(new_records)

    print("Student record deleted successfully." if deleted else "Student not found.")

def main():
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
