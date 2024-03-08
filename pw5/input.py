import numpy as np
import math
from domains import *
import zipfile


def integer_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def float_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def write_student_info(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"Student ID: {student._id}\n")
            file.write(f"Student Name: {student._name}\n")
            file.write(f"Date of Birth: {student._dob}\n\n")


def write_course_info(courses):
    with open("courses.txt", "w") as file:
        for course_id, course in courses.items():
            file.write(f"Course ID: {course_id}\n")
            file.write(f"Course Name: {course._name}\n")
            file.write(f"Credit: {course._credit}\n\n")


def write_marks(students):
    with open('marks.txt', 'w') as file:
        for student in students:
            file.write(f"Student ID: {student._id}\n")
            marks = student.show_marks()
            if marks is not None:
                for course_id, marks_info in marks.items():
                    file.write(f"Course ID: {course_id}\n")
                    file.write(f"Attendance: {marks_info['attendance']}\n")
                    file.write(f"Midterm: {marks_info['midterm']}\n")
                    file.write(f"Final: {marks_info['final']}\n")
                    total_mark = marks_info['attendance'] + marks_info['midterm'] + marks_info['final']
                    file.write(f"Total Mark: {total_mark}\n")
            else:
                file.write("No marks available for the student.\n")
            file.write("\n")