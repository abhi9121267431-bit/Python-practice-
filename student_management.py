
import json
import os

FILE_NAME = "students.json"

# Load student records
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
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()

        try:
            marks = float(input("Enter marks: "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue
        except ValueError:
            print("Enter valid numeric marks.")
            continue

        if any(s["roll_no"] == roll_no for s in students):
            print("Roll number already exists.")
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
        if not students:
            print("No students found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])

    # Search Student
    elif choice == "3":
        search_roll = input("Enter roll number: ").strip()
        found = False

        for student in students:
            if student["roll_no"] == search_roll:
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        search_roll = input("Enter roll number to update: ").strip()
        found = False

        for student in students:
            if student["roll_no"] == search_roll:
                new_name = input(
                    "Enter new name (Enter to keep current): "
                ).strip()

                new_marks = input(
                    "Enter new marks (Enter to keep current): "
                ).strip()

                if new_marks:
                    try:
                        marks = float(new_marks)
                        if not 0 <= marks <= 100:
                            print("Marks must be between 0 and 100.")
                            found = True
                            break
                    except ValueError:
                        print("Invalid marks.")
                        found = True
                        break

                    student["marks"] = marks

                if new_name:
                    student["name"] = new_name

                with open(FILE_NAME, "w") as file:
                    json.dump(students, file, indent=4)

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        delete_roll = input("Enter roll number to delete: ").strip()
        found = False

        for student in students:
            if student["roll_no"] == delete_roll:
                print("Student found:", student["name"])
                confirm = input("Confirm deletion? (yes/no): ")

                found = True

                if confirm.strip().lower() == "yes":
                    students.remove(student)

                    with open(FILE_NAME, "w") as file:
                        json.dump(students, file, indent=4)

                    print("Student deleted successfully!")
                else:
                    print("Deletion cancelled.")

                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")
