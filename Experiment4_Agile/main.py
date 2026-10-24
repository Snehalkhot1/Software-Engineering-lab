
"""
Experiment 4: Agile Development Methodologies
Student Management System
"""

students = {}
users = {}


def register(username, password):
    if not username.strip() or not password:
        return "Username and password are required"

    if username in users:
        return "Username already exists"

    users[username] = password
    return "Registration successful"


def login(username, password):
    if username in users and users[username] == password:
        return "Valid Login"
    return "Invalid Login"


def add_student(student_id, name, marks):
    if student_id in students:
        return "Student ID already exists"

    students[student_id] = {
        "name": name,
        "marks": marks
    }
    return "Student added successfully"


def update_student(student_id, name, marks):
    if student_id not in students:
        return "Student not found"

    students[student_id] = {
        "name": name,
        "marks": marks
    }
    return "Student updated successfully"


def delete_student(student_id):
    if student_id not in students:
        return "Student not found"

    del students[student_id]
    return "Student deleted successfully"


def search_student(student_id):
    return students.get(student_id, "Student not found")


def display_students():
    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print(
            "ID:", student_id,
            "| Name:", details["name"],
            "| Marks:", details["marks"]
        )


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Student Registration")
        print("2. Login")
        print("3. Add Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Display All Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Create username: ")
            password = input("Create password: ")
            print(register(username, password))

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login(username, password))

        elif choice == "3":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            try:
                marks = float(input("Enter marks: "))
                print(add_student(student_id, name, marks))
            except ValueError:
                print("Marks must be a number.")

        elif choice == "4":
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name: ")
            try:
                marks = float(input("Enter new marks: "))
                print(update_student(student_id, name, marks))
            except ValueError:
                print("Marks must be a number.")

        elif choice == "5":
            student_id = input("Enter student ID to delete: ")
            print(delete_student(student_id))

        elif choice == "6":
            student_id = input("Enter student ID to search: ")
            print(search_student(student_id))

        elif choice == "7":
            display_students()

        elif choice == "8":
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
