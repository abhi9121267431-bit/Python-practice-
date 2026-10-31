
import json
import os

FILE_NAME = "students.json"
PASS_MARK = 35


# Load existing student records
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
        if not isinstance(students, list):
            students = []
    except (json.JSONDecodeError, OSError):
        students = []
else:
    students = []


# Save student records
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# Display student details
def display_student(student):
    marks = student["marks"]
    print("\nName:", student["name"])
    print("Roll No:", student["roll_no"])
    print("Marks:", marks)
    print("Grade:", calculate_grade(marks))
    print("Result:", "Pass" if marks >= PASS_MARK else "Fail")


# Main program
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    # Add Student
    if choice == "1":
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()

        if not name or not roll_no:
            print("Name and roll number cannot be empty.")
            continue

        if any(s["roll_no"] == roll_no for s in students):
            print("Roll number already exists.")
            continue

        try:
            marks = float(input("Enter marks (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue
        except ValueError:
            print("Enter valid numeric marks.")
            continue

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks
        }

        students.append(student)
        save_students()

        print("Student added successfully!")
        display_student(student)

    # View Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for student in students:
                display_student(student)

    # Search Student
    elif choice == "3":
        search_roll = input("Enter roll number: ").strip()
        found = False

        for student in students:
            if student["roll_no"] == search_roll:
                display_student(student)
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
                display_student(student)

                new_name = input(
                    "Enter new name (Enter to keep current): "
                ).strip()

                new_marks = input(
                    "Enter new marks (Enter to keep current): "
                ).strip()

                # Validate marks before updating
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

                if new_name:
                    student["name"] = new_name

                if new_marks:
                    student["marks"] = marks

                save_students()
                print("Student updated successfully!")
                display_student(student)

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
                display_student(student)

                confirm = input(
                    "Confirm deletion? (yes/no): "
                ).strip().lower()

                found = True

                if confirm == "yes":
                    students.remove(student)
                    save_students()
                    print("Student deleted successfully!")
                else:
                    print("Deletion cancelled.")

                break

        if not found:
            print("Student not found.")

    # Class Summary Report
    elif choice == "6":
        if not students:
            print("No students found.")
        else:
            total_students = len(students)
            total_marks = sum(s["marks"] for s in students)
            average_marks = total_marks / total_students

            topper = max(students, key=lambda s: s["marks"])
            passed = sum(
                1 for s in students if s["marks"] >= PASS_MARK
            )
            failed = total_students - passed

            print("\n--- CLASS SUMMARY REPORT ---")
            print("Total Students:", total_students)
            print("Average Marks:", round(average_marks, 2))
            print("Class Topper:", topper["name"])
            print("Topper Roll No:", topper["roll_no"])
            print("Topper Marks:", topper["marks"])
            print("Topper Grade:", calculate_grade(topper["marks"]))
            print("Passed Students:", passed)
            print("Failed Students:", failed)

    # Exit
    elif choice == "7":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")


