
"""
Software Maintenance and Evolution
Student Management System
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """Load student records from the JSON file."""
    if not DATA_FILE.exists():
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {}

        return data

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data.")
        return {}


def save_students(students):
    """Save student records to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students, student_id, name, marks):
    """Add a student after validating the input."""
    student_id = str(student_id).strip()
    name = name.strip()

    if not student_id or not name:
        return "Student ID and name are required"

    if student_id in students:
        return "Student ID already exists"

    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        return "Marks must be numeric"

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    return "Student added successfully"


def update_student(students, student_id, name, marks):
    """Update an existing student's details."""
    student_id = str(student_id).strip()
    name = name.strip()

    if student_id not in students:
        return "Student not found"

    if not name:
        return "Student name is required"

    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        return "Marks must be numeric"

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    return "Student updated successfully"


def delete_student(students, student_id):
    """Delete a student if the ID exists."""
    student_id = str(student_id).strip()

    if student_id not in students:
        return "Student not found"

    del students[student_id]
    return "Student deleted successfully"


def search_student(students, search_name):
    """Find students by name, ignoring letter case."""
    search_name = search_name.strip().casefold()

    if not search_name:
        return []

    return [
        (student_id, details)
        for student_id, details in students.items()
        if search_name in details["name"].casefold()
    ]


def display_students(students):
    """Display all students in ID order."""
    if not students:
        print("No student records found.")
        return

    for student_id in sorted(students):
        details = students[student_id]
        print(
            f"ID: {student_id} | "
            f"Name: {details['name']} | "
            f"Marks: {details['marks']}"
        )


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Student name: ")

            try:
                marks = float(input("Marks (0-100): "))
                result = add_student(students, student_id, name, marks)
                print(result)

                if result == "Student added successfully":
                    save_students(students)

            except ValueError:
                print("Marks must be a number.")

        elif choice == "2":
            student_id = input("Student ID to update: ")
            name = input("New name: ")

            try:
                marks = float(input("New marks (0-100): "))
                result = update_student(students, student_id, name, marks)
                print(result)

                if result == "Student updated successfully":
                    save_students(students)

            except ValueError:
                print("Marks must be a number.")

        elif choice == "3":
            student_id = input("Student ID to delete: ")
            result = delete_student(students, student_id)
            print(result)

            if result == "Student deleted successfully":
                save_students(students)

        elif choice == "4":
            name = input("Enter name to search: ")
            results = search_student(students, name)

            if results:
                for student_id, details in results:
                    print(student_id, details)
            else:
                print("No matching students found.")

        elif choice == "5":
            display_students(students)

        elif choice == "6":
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
