
"""
Automated tests for Experiment 11.
Black-box and white-box tests for the login module.
"""

from login import validate_login, add_student, students


# Black-box functional test cases

def test_valid_login():
    assert validate_login("admin", "admin123") == "Valid Login"


def test_valid_student_login():
    assert validate_login("student", "stud@1") == "Valid Login"


def test_wrong_password():
    assert validate_login("admin", "wrong12") == "Invalid Login"


def test_unknown_username():
    assert validate_login("unknown", "abcdef") == "Invalid Login"


def test_empty_username():
    assert validate_login("", "admin123") == "Error: Username required"


def test_whitespace_username():
    assert validate_login("   ", "admin123") == "Error: Username required"


# Boundary Value Analysis: password length

def test_password_length_five():
    assert validate_login("admin", "abcde") == "Error: Password too short"


def test_password_length_six():
    assert validate_login("admin", "abcdef") == "Invalid Login"


def test_password_length_twelve():
    assert validate_login("admin", "abcdefghijkl") == "Invalid Login"


def test_password_length_thirteen():
    assert validate_login("admin", "abcdefghijklm") == "Error: Password too long"


# White-box tests for different branches

def test_password_not_a_string():
    assert validate_login("admin", None) == "Error: Invalid password"


def test_valid_student_path():
    result = validate_login("student", "stud@1")
    assert result == "Valid Login"


# Supporting Student Management System tests

def test_add_student():
    students.clear()
    assert add_student(1, "Asha", 85) is True
    assert (1, "Asha", 85) in students


def test_add_student_invalid_id():
    assert add_student(0, "Asha", 85) is False


def test_add_student_invalid_name():
    assert add_student(2, "   ", 85) is False


def test_add_student_invalid_marks():
    assert add_student(3, "Ravi", 120) is False
