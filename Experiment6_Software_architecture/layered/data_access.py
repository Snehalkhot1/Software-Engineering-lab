
# Data Access Layer

students = {}


def add_student(student_id, name, marks):
    if student_id in students:
        return False

    students[student_id] = {
        "name": name,
        "marks": marks
    }
    return True


def get_student(student_id):
    return students.get(student_id)


def get_all_students():
    return students
