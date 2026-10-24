
# Presentation Layer

import business


def run_app():
    while True:
        print("\n--- Layered Student System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Student name: ")

            try:
                marks = float(input("Marks: "))
                print(business.add_student(student_id, name, marks))
            except ValueError:
                print("Marks must be a number.")

        elif choice == "2":
            student_id = input("Enter ID to search: ")
            print(business.search_student(student_id))

        elif choice == "3":
            print(business.list_students())

        elif choice == "4":
            break

        else:
            print("Invalid choice")
