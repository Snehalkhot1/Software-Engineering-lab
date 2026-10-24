
# Business Logic Layer

import data_access


def add_student(student_id, name, marks):
    if not student_id.strip() or not name.strip():
        return "ID and name are required"

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"

    success = data_access.add_student(student_id, name, marks)

    if success:
        return "Student added successfully"

    return "Student ID already exists"


def search_student(student_id):
    student = data_access.get_student(student_id)

    if student is None:
        return "Student not found"

    return student


def list_students():
    return data_access.get_all_students()
