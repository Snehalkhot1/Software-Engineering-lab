
# Experiment 6: Monolithic Architecture

students = {}


def add_student(student_id, name, marks):
    if student_id in students:
        return "Student ID already exists"

    students[student_id] = {"name": name, "marks": marks}
    return "Student added successfully"


def search_student(student_id):
    return students.get(student_id, "Student not found")


def main():
    while True:
        print("\n--- Monolithic Student System ---")
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
                print(add_student(student_id, name, marks))
            except ValueError:
                print("Marks must be a number.")

        elif choice == "2":
            student_id = input("Enter ID to search: ")
            print(search_student(student_id))

        elif choice == "3":
            print(students)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
