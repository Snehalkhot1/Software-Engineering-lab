
# Software Maintenance Log

## Project
Student Management System

## 1. Corrective Maintenance
Purpose:
Fix errors discovered during testing or use.

Example:
- Reject marks outside the range 0 to 100.
- Display "Student not found" when an unknown ID is updated.
- Prevent duplicate student IDs.

Verification:
Run the automated unit tests.

## 2. Adaptive Maintenance
Purpose:
Modify software to work in a changed environment.

Example:
- Store records in a JSON file instead of keeping them only in memory.
- Load saved records when the application starts.

Verification:
Add a student, close the application, restart it, and check
whether the student record is still available.

## 3. Perfective Maintenance
Purpose:
Improve functionality, usability, or performance.

Example:
- Search names without considering uppercase or lowercase.
- Display student records in ID order.
- Provide clear messages for successful and unsuccessful operations.

Verification:
Search for "asha" when the stored name is "Asha Patil".

## 4. Preventive Maintenance
Purpose:
Reduce the likelihood of future faults and make the software
easier to maintain.

Example:
- Divide functionality into separate functions.
- Use meaningful function and variable names.
- Add docstrings and automated tests.
- Validate inputs before changing records.

Verification:
Run the test suite after code changes.

## Maintenance Record

| Technique | Change | Verification |
|---|---|---|
| Corrective | Input validation and missing-record handling | Unit tests |
| Adaptive | JSON-based persistent storage | Save and reload test |
| Perfective | Case-insensitive search and sorted display | Search and display tests |
| Preventive | Modular functions and regression tests | Full test suite |

## Result
The project demonstrates four software maintenance categories
and uses automated tests to check important behavior.
