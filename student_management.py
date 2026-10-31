
import json
import os

FILE_NAME = "students.json"

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

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks
        }

        students.append(student)
        
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])

    elif choice == "3":
        search_roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll_no"] == search_roll:
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")
