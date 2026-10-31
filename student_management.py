
import json
import os

FILE_NAME = "students.json"

# Load existing student records
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = []


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")

        try:
            marks = float(input("Enter marks: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue
        except ValueError:
            print("Please enter valid numeric marks.")
            continue

        # Check for duplicate roll numbers
        if any(s["roll_no"] == roll_no for s in students):
            print("This roll number already exists.")
            continue

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks
        }

        students.append(student)

        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])

    # Search Student
    elif choice == "3":
        search_roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll_no"] == search_roll:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")
