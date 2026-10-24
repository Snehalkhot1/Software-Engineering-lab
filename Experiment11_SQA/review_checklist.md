
# Experiment No. 11: Software Quality Assurance

## 1. Project Details

- **Project Name:** Student Management System
- **Module:** Login Module
- **Experiment:** Compare and Contrast Different Software Quality Assurance Techniques
- **IDE:** Visual Studio Code
- **Programming Language:** Python

## 2. Aim

To study, apply, and compare different Software Quality Assurance (SQA) techniques, including Technical Reviews/Inspections, Static Analysis, Black-Box Testing, and White-Box Testing.

## 3. Technical Review / Formal Inspection

### Inspection Roles

| Role | Student | Responsibility |
|---|---|---|
| Moderator | Student A | Plans and leads the inspection meeting |
| Author | Student B | Develops the Login module and answers questions |
| Reader | Student C | Reads and explains the code |
| Recorder | Student D | Records defects in the defect log |
| Inspector | Student E | Checks the code against the checklist |

### Inspection Checklist

| No. | Checklist Item | Result | Remarks |
|---|---|---|---|
| 1 | Does the code follow naming conventions? | Yes | Descriptive function and variable names are used |
| 2 | Are all inputs validated? | Yes | Empty username and password length are checked |
| 3 | Are passwords stored securely? | No | Demonstration uses hard-coded plain-text passwords |
| 4 | Is error handling implemented? | Partial | Input validation exists; no logging is implemented |
| 5 | Are comments and documentation adequate? | Yes | Module and function docstrings are provided |
| 6 | Is hard-coded data avoided? | No | Fixed credentials are required for this experiment |
| 7 | Are all variables defined before use? | Yes | Required variables are defined |

## 4. Defect Log

| ID | Defect Description | Location | Severity | Status |
|---|---|---|---|---|
| R1 | Passwords stored in plain text | Original login code | High | Open for production |
| R2 | No validation for empty username | Original login code | Medium | Fixed |
| R3 | Hard-coded user credentials | Login module | Medium | Retained for lab |
| R4 | Student list was undefined | Original add_student function | High | Fixed |
| R5 | Missing comments and documentation | Original source code | Low | Fixed |

## 5. Static Analysis

### Tools Used

- Pylint
- Flake8

### Commands

```powershell
python -m pylint login.py
python -m flake8 login.py
```

### Purpose

Static analysis examines the source code without executing it. It helps identify coding-standard violations, undefined variables, naming problems, and other potential issues.

Record the actual warnings and results displayed by the tools when you execute these commands.

## 6. Black-Box Testing

Black-box testing checks the functionality of the Login module using inputs and expected outputs without depending on the internal code structure.

### Functional Test Cases

| Test ID | Username | Password | Expected Output |
|---|---|---|---|
| T1 | admin | admin123 | Valid Login |
| T2 | admin | wrong12 | Invalid Login |
| T3 | Empty | admin123 | Error: Username required |
| T4 | unknown | abcdef | Invalid Login |
| T5 | admin | abcde | Error: Password too short |
| T6 | admin | abcdefghijklm | Error: Password too long |

### Boundary Value Analysis

The valid password length is between 6 and 12 characters.

| Test ID | Password Length | Expected Result |
|---|---:|---|
| B1 | 5 | Rejected |
| B2 | 6 | Length accepted |
| B3 | 12 | Length accepted |
| B4 | 13 | Rejected |

## 7. White-Box Testing

White-box testing examines the internal logic, conditions, and execution paths of the Login module.

### Test Paths

| Path | Condition | Input | Expected Output |
|---|---|---|---|
| P1 | Empty username | Empty / admin123 | Error: Username required |
| P2 | Password too short | admin / abcde | Error: Password too short |
| P3 | Password too long | admin / abcdefghijklm | Error: Password too long |
| P4 | Unknown username | unknown / abcdef | Invalid Login |
| P5 | Incorrect password | admin / wrong12 | Invalid Login |
| P6 | Correct credentials | admin / admin123 | Valid Login |

### Testing Commands

```powershell
python -m pytest -v
python -m coverage run --branch -m pytest
python -m coverage report -m login.py
```

Record the actual test results and coverage percentage after execution.

## 8. Comparison of SQA Techniques

| Parameter | Technical Review | Static Analysis | Black-Box Testing | White-Box Testing |
|---|---|---|---|---|
| Type | Manual inspection | Automated analysis | Dynamic testing | Dynamic testing |
| Code execution | Not required | Not required | Required | Required |
| Main purpose | Find defects early | Identify code quality issues | Verify functionality | Verify internal logic |
| Main advantage | Detects design and security issues | Fast and repeatable | Tests user requirements | Examines branches and paths |
| Limitation | Time-consuming | Cannot find every runtime defect | May miss internal paths | May miss missing requirements |

## 9. Observations

1. Technical reviews help identify design, documentation, and security problems.
2. Static analysis identifies coding-standard violations and potential programming errors.
3. Black-box testing verifies whether the program produces the expected output for different inputs.
4. White-box testing examines the internal logic and execution paths.
5. Combining different SQA techniques improves defect detection and overall software quality.

## 10. Conclusion

Software Quality Assurance techniques were studied and applied to the Login module of the Student Management System. Technical reviews, static analysis, black-box testing, and white-box testing provide different ways to identify defects. The experiment demonstrates that combining these techniques helps improve software reliability, maintainability, and quality.
