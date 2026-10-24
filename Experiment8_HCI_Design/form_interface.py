
# HCI Design 2: Form-Based Graphical Interface

import tkinter as tk
from tkinter import messagebox
import student_data as data


def get_inputs():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()

    try:
        marks = float(marks_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Marks must be a number.")
        return None

    if not student_id or not name:
        messagebox.showerror(
            "Missing Information",
            "Please enter student ID and name."
        )
        return None

    if not 0 <= marks <= 100:
        messagebox.showerror(
            "Invalid Marks",
            "Marks must be between 0 and 100."
        )
        return None

    return student_id, name, marks


def add():
    values = get_inputs()
    if values:
        result = data.add_student(*values)
        messagebox.showinfo("Add Student", result)
        refresh_list()


def search():
    student_id = id_entry.get().strip()
    student = data.search_student(student_id)

    if student:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, student["name"])
        marks_entry.delete(0, tk.END)
        marks_entry.insert(0, str(student["marks"]))
        messagebox.showinfo("Search", "Student found.")
    else:
        messagebox.showwarning("Search", "Student not found.")


def update():
    values = get_inputs()
    if values:
        result = data.update_student(*values)
        messagebox.showinfo("Update Student", result)
        refresh_list()


def delete():
    student_id = id_entry.get().strip()
    result = data.delete_student(student_id)
    messagebox.showinfo("Delete Student", result)
    refresh_list()


def clear():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


def refresh_list():
    student_list.delete(0, tk.END)

    for student_id, student in data.students.items():
        student_list.insert(
            tk.END,
            f"{student_id} | {student['name']} | {student['marks']}"
        )


root = tk.Tk()
root.title("Student Management - Form Design")
root.geometry("600x500")
root.configure(bg="#F2F5F9")

tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18, "bold"),
    bg="#F2F5F9"
).pack(pady=15)

form = tk.Frame(root, bg="#F2F5F9")
form.pack(pady=5)

tk.Label(form, text="Student ID:", bg="#F2F5F9").grid(
    row=0, column=0, sticky="w", padx=8, pady=6
)
id_entry = tk.Entry(form, width=30)
id_entry.grid(row=0, column=1, padx=8, pady=6)

tk.Label(form, text="Student Name:", bg="#F2F5F9").grid(
    row=1, column=0, sticky="w", padx=8, pady=6
)
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=1, column=1, padx=8, pady=6)

tk.Label(form, text="Marks:", bg="#F2F5F9").grid(
    row=2, column=0, sticky="w", padx=8, pady=6
)
marks_entry = tk.Entry(form, width=30)
marks_entry.grid(row=2, column=1, padx=8, pady=6)

buttons = tk.Frame(root, bg="#F2F5F9")
buttons.pack(pady=10)

tk.Button(buttons, text="Add", width=10, command=add).grid(
    row=0, column=0, padx=4, pady=4
)
tk.Button(buttons, text="Search", width=10, command=search).grid(
    row=0, column=1, padx=4, pady=4
)
tk.Button(buttons, text="Update", width=10, command=update).grid(
    row=0, column=2, padx=4, pady=4
)
tk.Button(buttons, text="Delete", width=10, command=delete).grid(
    row=0, column=3, padx=4, pady=4
)
tk.Button(buttons, text="Clear", width=10, command=clear).grid(
    row=1, column=0, padx=4, pady=4
)
tk.Button(
    buttons, text="Refresh List", width=12, command=refresh_list
).grid(row=1, column=1, padx=4, pady=4)

tk.Label(
    root, text="Student Records", font=("Arial", 12, "bold"),
    bg="#F2F5F9"
).pack(pady=5)

student_list = tk.Listbox(root, width=65, height=10)
student_list.pack(padx=10, pady=5)

root.mainloop()
