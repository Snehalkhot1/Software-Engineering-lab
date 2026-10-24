
# HCI Design 1: Menu-Driven Interface

import student_data as data


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")

            try:
                marks = float(input("Enter marks: "))
                print(data.add_student(student_id, name, marks))
            except ValueError:
                print("Please enter numeric marks.")

        elif choice == "2":
            student_id = input("Enter student ID: ")
            student = data.search_student(student_id)

            if student:
                print("Student details:", student)
            else:
                print("Student not found")

        elif choice == "3":
            student_id = input("Enter student ID: ")
            name = input("Enter new name: ")

            try:
                marks = float(input("Enter new marks: "))
                print(data.update_student(student_id, name, marks))
            except ValueError:
                print("Please enter numeric marks.")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            print(data.delete_student(student_id))

        elif choice == "5":
            if not data.students:
                print("No student records available.")
            else:
                for student_id, student in data.students.items():
                    print(student_id, student)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
