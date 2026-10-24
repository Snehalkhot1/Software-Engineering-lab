
# Common Student Data for HCI Experiment

students = {}


def add_student(student_id, name, marks):
    student_id = student_id.strip()
    name = name.strip()

    if not student_id or not name:
        return "Student ID and name are required"

    if student_id in students:
        return "Student ID already exists"

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"

    students[student_id] = {
        "name": name,
        "marks": marks
    }
    return "Student added successfully"


def search_student(student_id):
    return students.get(student_id.strip())


def update_student(student_id, name, marks):
    student_id = student_id.strip()
    name = name.strip()

    if student_id not in students:
        return "Student not found"

    if not name:
        return "Student name is required"

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"

    students[student_id] = {
        "name": name,
        "marks": marks
    }
    return "Student updated successfully"


def delete_student(student_id):
    student_id = student_id.strip()

    if student_id not in students:
        return "Student not found"

    del students[student_id]
    return "Student deleted successfully"
