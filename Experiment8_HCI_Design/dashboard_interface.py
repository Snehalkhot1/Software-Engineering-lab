
# HCI Design 3: Dashboard-Based Graphical Interface

import tkinter as tk
from tkinter import messagebox
import student_data as data


def refresh():
    records.delete(0, tk.END)
    total_label.config(text=f"Total Students: {len(data.students)}")

    if data.students:
        average = sum(
            student["marks"] for student in data.students.values()
        ) / len(data.students)
    else:
        average = 0

    average_label.config(text=f"Average Marks: {average:.1f}")

    for student_id, student in data.students.items():
        records.insert(
            tk.END,
            f"ID: {student_id}  |  "
            f"{student['name']}  |  Marks: {student['marks']}"
        )


def add_student():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()

    try:
        marks = float(marks_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Enter numeric marks.")
        return

    if not student_id or not name:
        messagebox.showerror(
            "Input Error", "Enter both ID and name."
        )
        return

    result = data.add_student(student_id, name, marks)
    messagebox.showinfo("Student Management", result)
    refresh()


def search_student():
    student_id = id_entry.get().strip()
    student = data.search_student(student_id)

    if student:
        messagebox.showinfo(
            "Student Found",
            f"Name: {student['name']}\nMarks: {student['marks']}"
        )
    else:
        messagebox.showwarning("Search", "Student not found.")


def delete_student():
    student_id = id_entry.get().strip()
    result = data.delete_student(student_id)
    messagebox.showinfo("Student Management", result)
    refresh()


root = tk.Tk()
root.title("Student Management Dashboard")
root.geometry("700x550")
root.configure(bg="#EEF2F7")

header = tk.Frame(root, bg="#1E3A5F", height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="Student Management Dashboard",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1E3A5F"
).pack(pady=18)

summary = tk.Frame(root, bg="#EEF2F7")
summary.pack(fill="x", padx=15, pady=12)

total_label = tk.Label(
    summary, text="Total Students: 0",
    font=("Arial", 12, "bold"), bg="white", padx=15, pady=12
)
total_label.pack(side="left", expand=True, fill="x", padx=5)

average_label = tk.Label(
    summary, text="Average Marks: 0.0",
    font=("Arial", 12, "bold"), bg="white", padx=15, pady=12
)
average_label.pack(side="left", expand=True, fill="x", padx=5)

form = tk.Frame(root, bg="#EEF2F7")
form.pack(pady=5)

tk.Label(form, text="Student ID:", bg="#EEF2F7").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
id_entry = tk.Entry(form, width=25)
id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form, text="Name:", bg="#EEF2F7").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
name_entry = tk.Entry(form, width=25)
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form, text="Marks:", bg="#EEF2F7").grid(
    row=2, column=0, padx=5, pady=5, sticky="w"
)
marks_entry = tk.Entry(form, width=25)
marks_entry.grid(row=2, column=1, padx=5, pady=5)

actions = tk.Frame(root, bg="#EEF2F7")
actions.pack(pady=8)

tk.Button(
    actions, text="Add Student", width=14, command=add_student
).grid(row=0, column=0, padx=5)

tk.Button(
    actions, text="Search Student", width=14, command=search_student
).grid(row=0, column=1, padx=5)

tk.Button(
    actions, text="Delete Student", width=14, command=delete_student
).grid(row=0, column=2, padx=5)

tk.Button(
    actions, text="Refresh Dashboard", width=18, command=refresh
).grid(row=0, column=3, padx=5)

tk.Label(
    root, text="Student Records",
    font=("Arial", 13, "bold"), bg="#EEF2F7"
).pack(pady=5)

records = tk.Listbox(root, width=85, height=12)
records.pack(padx=15, pady=5, fill="both", expand=True)

refresh()
root.mainloop()
