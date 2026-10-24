
"""
Student Management System - Login Module
Experiment 11: Software Quality Assurance
"""

# Fixed credentials for this laboratory experiment.
# Do not use hard-coded passwords in a real application.
USERS = {
    "admin": "admin123",
    "student": "stud@1"
}

# Student records used by the sample Student Management System.
students = []


def validate_login(username, password):
    """Validate username, password length, and login credentials."""

    if not username or not username.strip():
        return "Error: Username required"

    if not isinstance(password, str):
        return "Error: Invalid password"

    if len(password) < 6:
        return "Error: Password too short"

    if len(password) > 12:
        return "Error: Password too long"

    if username in USERS and USERS[username] == password:
        return "Valid Login"

    return "Invalid Login"


def add_student(student_id, name, marks):
    """Add a student after checking the input values."""

    if not isinstance(student_id, int) or student_id <= 0:
        return False

    if not isinstance(name, str) or not name.strip():
        return False

    if not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
        return False

    students.append((student_id, name, marks))
    return True


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    print(validate_login(username, password))
