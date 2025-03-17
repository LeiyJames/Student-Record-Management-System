import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Record Management System")             

# Title Label
title_label = tk.Label(win, text="Student Record Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE)             
title_label.pack(side=tk.TOP, fill=tk.X)     

# Enter Details Frame
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 15), padx=10, pady=10)
detail_frame.place(x=20, y=110, width=420, height=560)

# Labels and Entries for Student Information
name_label = tk.Label(detail_frame, text="Name:", font=("Arial", 12))
name_label.grid(row=0, column=0, pady=5, sticky="w")
name_entry = tk.Entry(detail_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, pady=5, padx=10)

age_label = tk.Label(detail_frame, text="Age:", font=("Arial", 12))
age_label.grid(row=1, column=0, pady=5, sticky="w")
age_entry = tk.Entry(detail_frame, font=("Arial", 12))
age_entry.grid(row=1, column=1, pady=5, padx=10)

gender_label = tk.Label(detail_frame, text="Gender:", font=("Arial", 12))
gender_label.grid(row=2, column=0, pady=5, sticky="w")
gender_combobox = ttk.Combobox(detail_frame, font=("Arial", 12), values=["Male", "Female",])
gender_combobox.grid(row=2, column=1, pady=5, padx=10)

address_label = tk.Label(detail_frame, text="Address:", font=("Arial", 12))
address_label.grid(row=3, column=0, pady=5, sticky="w")
address_entry = tk.Entry(detail_frame, font=("Arial", 12))
address_entry.grid(row=3, column=1, pady=5, padx=10)

# New Fields for Grades and Attendance
grade_label = tk.Label(detail_frame, text="Grade:", font=("Arial", 12))
grade_label.grid(row=4, column=0, pady=5, sticky="w")
grade_entry = tk.Entry(detail_frame, font=("Arial", 12))
grade_entry.grid(row=4, column=1, pady=5, padx=10)

attendance_label = tk.Label(detail_frame, text="Attendance:", font=("Arial", 12))
attendance_label.grid(row=5, column=0, pady=5, sticky="w")
attendance_entry = tk.Entry(detail_frame, font=("Arial", 12))
attendance_entry.grid(row=5, column=1, pady=5, padx=10)

# Function to Add a Student
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    address = address_entry.get()
    grade = grade_entry.get()
    attendance = attendance_entry.get()

    if name and age and gender and address and grade and attendance:
        student_list.insert("", "end", values=(name, age, gender, address, grade, attendance))
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

# Function to Clear Entry Fields
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combobox.set('')
    address_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    attendance_entry.delete(0, tk.END)

# Function to Update a Student's Details
def update_student():
    selected_item = student_list.selection()
    if selected_item:
        item = student_list.item(selected_item)
        values = item['values']

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_combobox.set('')
        address_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        attendance_entry.delete(0, tk.END)

        name_entry.insert(0, values[0])
        age_entry.insert(0, values[1])
        gender_combobox.set(values[2])
        address_entry.insert(0, values[3])
        grade_entry.insert(0, values[4])
        attendance_entry.insert(0, values[5])

        student_list.delete(selected_item)

# Function to Delete a Student Record
def delete_student():
    selected_item = student_list.selection()
    if selected_item:
        student_list.delete(selected_item)
    else:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")

# Function to Generate Reports (Export to Text File)
def generate_report():
    with open("student_report.txt", "w") as f:
        for record in student_list.get_children():
            record_values = student_list.item(record)['values']
            f.write(f"Name: {record_values[0]}, Age: {record_values[1]}, Gender: {record_values[2]}, Address: {record_values[3]}, Grade: {record_values[4]}, Attendance: {record_values[5]}\n")
    messagebox.showinfo("Report Generated", "Student report has been generated successfully.")

# Buttons to Add, Update, Delete, and Generate Report (Side by Side)
button_frame = tk.Frame(detail_frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=10)

add_button = tk.Button(button_frame, text="Add", font=("Arial", 12), width=10, command=add_student)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update", font=("Arial", 12), width=10, command=update_student)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 12), width=10, command=delete_student)
delete_button.grid(row=0, column=2, padx=5, pady=5)

generate_report_button = tk.Button(button_frame, text="Report", font=("Arial", 12), width=10, command=generate_report)
generate_report_button.grid(row=0, column=3, padx=5, pady=5)


# Student Records Display Area
records_frame = tk.Frame(win)
records_frame.place(x=470, y=110, width=860, height=560)

columns = ("Name", "Age", "Gender", "Address", "Grade", "Attendance")
student_list = ttk.Treeview(records_frame, columns=columns, show="headings", height=20)
for col in columns:
    student_list.heading(col, text=col)
    student_list.column(col, width=150)

student_list.pack(fill=tk.BOTH, expand=True)

win.mainloop()
