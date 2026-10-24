
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import student_system


class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.students = {}

    def test_add_student(self):
        result = student_system.add_student(
            self.students, "101", "Asha", 85
        )
        self.assertEqual(result, "Student added successfully")

    def test_duplicate_student_id(self):
        student_system.add_student(
            self.students, "101", "Asha", 85
        )
        result = student_system.add_student(
            self.students, "101", "Ravi", 90
        )
        self.assertEqual(result, "Student ID already exists")

    def test_invalid_marks(self):
        result = student_system.add_student(
            self.students, "101", "Asha", 120
        )
        self.assertEqual(result, "Marks must be between 0 and 100")

    def test_empty_name(self):
        result = student_system.add_student(
            self.students, "101", "   ", 85
        )
        self.assertEqual(result, "Student ID and name are required")

    def test_update_student(self):
        student_system.add_student(
            self.students, "101", "Asha", 85
        )
        result = student_system.update_student(
            self.students, "101", "Asha Patil", 90
        )
        self.assertEqual(result, "Student updated successfully")
        self.assertEqual(self.students["101"]["marks"], 90)

    def test_update_missing_student(self):
        result = student_system.update_student(
            self.students, "999", "Ravi", 75
        )
        self.assertEqual(result, "Student not found")

    def test_delete_student(self):
        student_system.add_student(
            self.students, "101", "Asha", 85
        )
        result = student_system.delete_student(self.students, "101")
        self.assertEqual(result, "Student deleted successfully")
        self.assertNotIn("101", self.students)

    def test_delete_missing_student(self):
        result = student_system.delete_student(self.students, "999")
        self.assertEqual(result, "Student not found")

    def test_case_insensitive_search(self):
        student_system.add_student(
            self.students, "101", "Asha Patil", 85
        )
        results = student_system.search_student(
            self.students, "asha"
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "101")

    def test_save_and_load_students(self):
        with tempfile.TemporaryDirectory() as folder:
            test_file = Path(folder) / "students.json"

            with patch.object(student_system, "DATA_FILE", test_file):
                student_system.save_students({
                    "101": {"name": "Asha", "marks": 85}
                })
                loaded = student_system.load_students()

            self.assertEqual(
                loaded["101"]["name"], "Asha"
            )
            self.assertEqual(
                loaded["101"]["marks"], 85
            )


if __name__ == "__main__":
    unittest.main()
