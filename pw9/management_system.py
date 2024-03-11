from domains.Student import Student
from domains.Course import Course
from input import integer_input, float_input, write_marks, write_course_info, write_student_info
from output import print_info
import numpy as np
import math
import zipfile
import os
import pickle
import threading
import tkinter as tk
from tkinter import messagebox
def create_students(num_students):
    students = []
    for _ in range(num_students):
        print_info(f"\nStudent Information (Student {len(students) + 1}):")
        student_id = integer_input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student = Student(student_id, student_name, student_dob)
        students.append(student)
    return students


def create_courses(num_courses):
    courses = {}
    for _ in range(num_courses):
        print_info(f"\nCourse Information (Course {len(courses) + 1}):")
        course_id = integer_input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_credit = float_input("Enter course credit: ")  # Use float_input() instead of integer_input()
        course = Course(course_id, course_name, course_credit)
        courses[course_id] = course
    return courses


def show_marks(students):
    print_info("\nStudent's Marks:")
    for student in students:
        print_info(f"\nStudent ID: {student._id}")
        marks = student.show_marks()
        if marks is None:
            print_info("No marks available for the student.")
        else:
            for course_id, marks_info in marks.items():
                print_info(f"Course ID: {course_id}")
                print_info(f"Attendance: {marks_info['attendance']}")
                print_info(f"Midterm: {marks_info['midterm']}")
                print_info(f"Final: {marks_info['final']}")


def show_courses(courses):
    print_info("\nCourse Information:")
    for course_id, course in courses.items():
        print_info(f"Course ID: {course_id}")
        print_info(f"Course Name: {course._name}")
        print_info(f"Credit: {course._credit}")


def sort_gpa(students, courses):
    print_info("\nStudents Sorted by GPA:")
    sorted_students = sorted(students, key=lambda student: student.calculate_gpa(courses)[0], reverse=True)
    for student in sorted_students:
        gpa, weighted_sum = student.calculate_gpa(courses)
        print_info(f"\nStudent ID: {student._id}")
        print_info(f"Student Name: {student._name}")
        print_info(f"GPA: {gpa}")


def compress_files():
    filenames = ["students.txt", "courses.txt", "marks.txt"]
    with zipfile.ZipFile("data.zip","w",compression=zipfile.ZIP_DEFLATED) as zf:
        with open("students.dat", "wb") as pf:
            pickle.dump(filenames, pf)
            for filename in filenames:
                with open(filename, "rb") as data_file:
                    data = data_file.read()
                    zf.writestr(filename, data)

def backgroundThread():
    compress_files()
def check_and_decompress():
    if os.path.exists("students.dat"):
        choice = input("Do you want to decompress the files? (y/n): ")
        if choice.lower() == "y":
            try:
                with open("students.dat", "rb") as file:
                    filenames = pickle.load(file)
                    for filename in filenames:
                        with open(filename, "wb") as data_file:
                            try:
                                data = pickle.load(file)
                                data_file.write(data)
                            except EOFError:
                                print_info(f"Error: Invalid data in {filename}.")
            except EOFError:
                print_info("Error: Invalid data in students.dat.")
    else:
        print_info("Error: students.dat file not found.")
def main():
    check_and_decompress()

    def create():
        num_students = entry_students.get()
        num_courses = entry_courses.get()

        if not num_students.isdigit() or not num_courses.isdigit():
            messagebox.showerror("Error", "Please enter valid numbers for the number of students and courses.")
            return

        num_students = int(num_students)
        num_courses = int(num_courses)

        students = create_students(num_students)
        courses = create_courses(num_courses)

        write_student_info(students)
        write_course_info(courses)

        messagebox.showinfo("Information", "Student and course information created successfully.")

        for student in students:
            marks_window = tk.Toplevel(window)
            marks_window.title(f"Enter Marks for Student ID: {student._id}")

            for course_id in courses:
                tk_labelAttendance = tk.Label(marks_window, text=f"Attendance mark for Course ID {course_id}:")
                tk_labelAttendance.grid(column=0, row=0, padx=10, pady=10)
                entry_attendance = tk.Entry(marks_window)
                entry_attendance.grid(column=1, row=0, padx=10, pady=10)

                tk_labelMidterm = tk.Label(marks_window, text=f"Midterm mark for Course ID {course_id}:")
                tk_labelMidterm.grid(column=0, row=1, padx=10, pady=10)
                entry_midterm = tk.Entry(marks_window)
                entry_midterm.grid(column=1, row=1, padx=10, pady=10)

                tk_labelFinal = tk.Label(marks_window, text=f"Final mark for Course ID {course_id}:")
                tk_labelFinal.grid(column=0, row=2, padx=10, pady=10)
                entry_final = tk.Entry(marks_window)
                entry_final.grid(column=1, row=2, padx=10, pady=10)

                def save_marks():
                    attendance = entry_attendance.get()
                    midterm = entry_midterm.get()
                    final = entry_final.get()

                    if not attendance.isdigit() or not midterm.isdigit() or not final.isdigit():
                        messagebox.showerror("Error", "Please enter valid numbers for the marks.")
                        return

                    attendance = float(attendance)
                    midterm = float(midterm)
                    final = float(final)

                    student.add_attendance(course_id, attendance)
                    student.add_midterm(course_id, midterm)
                    student.add_final(course_id, final)

                    messagebox.showinfo("Information", "Marks saved successfully.")

                    marks_window.destroy()

                button_save = tk.Button(marks_window, text="Save", command=save_marks)
                button_save.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

            marks_window.mainloop()

        write_marks(students)
        show_courses(courses)
        sort_gpa(students, courses)
        show_marks(students)

        compress_files()

    window = tk.Tk()
    window.title("Student Management System")

    tk_labelStudent = tk.Label(window, text="Number of students:")
    tk_labelStudent.grid(column=0, row=0, padx=10, pady=10)
    entry_students = tk.Entry(window)
    entry_students.grid(column=1, row=0, padx=10, pady=10)

    tk_labelCourse = tk.Label(window, text="Number of courses:")
    tk_labelCourse.grid(column=0, row=1, padx=10, pady=10)
    entry_courses = tk.Entry(window)
    entry_courses.grid(column=1, row=1, padx=10, pady=10)

    button_create = tk.Button(window, text="Create", command=create)
    button_create.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    window.mainloop()

if __name__ == '__main__':
    main()