
"""
Experiment 4: XP Test-Driven Development
Tests for the Student Management System
"""

import unittest
import main


class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        # Start each test with empty records.
        main.students.clear()
        main.users.clear()

    def test_registration(self):
        result = main.register("asha", "pass123")
        self.assertEqual(result, "Registration successful")

    def test_duplicate_registration(self):
        main.register("asha", "pass123")
        result = main.register("asha", "pass456")
        self.assertEqual(result, "Username already exists")

    def test_valid_login(self):
        main.register("asha", "pass123")
        result = main.login("asha", "pass123")
        self.assertEqual(result, "Valid Login")

    def test_invalid_login(self):
        result = main.login("asha", "wrong123")
        self.assertEqual(result, "Invalid Login")

    def test_add_student(self):
        result = main.add_student("101", "Asha", 85)
        self.assertEqual(result, "Student added successfully")
        self.assertEqual(main.students["101"]["name"], "Asha")

    def test_update_student(self):
        main.add_student("101", "Asha", 85)
        result = main.update_student("101", "Asha Patil", 90)
        self.assertEqual(result, "Student updated successfully")
        self.assertEqual(main.students["101"]["marks"], 90)

    def test_delete_student(self):
        main.add_student("101", "Asha", 85)
        result = main.delete_student("101")
        self.assertEqual(result, "Student deleted successfully")
        self.assertNotIn("101", main.students)

    def test_search_student(self):
        main.add_student("101", "Asha", 85)
        result = main.search_student("101")
        self.assertEqual(result["name"], "Asha")

    def test_search_missing_student(self):
        result = main.search_student("999")
        self.assertEqual(result, "Student not found")


if __name__ == "__main__":
    unittest.main()
