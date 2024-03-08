from domains.Student import Student
from domains.Course import Course
from input import integer_input, float_input, write_marks, write_course_info, write_student_info
from output import print_info
import numpy as np
import math
import zipfile
import os


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
    with zipfile.ZipFile("students.dat", "w") as zipf:
        for filename in filenames:
            zipf.write(filename)


def check_and_decompress():
    if os.path.exists("students.dat"):
        choice = input("Do you want to decompress the files? (y/n): ")
        if choice.lower() == "y":
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extractall()


def main():
    check_and_decompress()

    num_students = integer_input(f"\nEnter the number of students: ")
    students = create_students(num_students)

    num_courses = integer_input(f"\nEnter the number of courses: ")
    courses = create_courses(num_courses)

    write_student_info(students)
    write_course_info(courses)

    print_info("\n Information:")
    for student in students:
        print_info(f"\nStudent ID: {student._id}")
        for course_id in courses:
            attendance = float_input(f"Enter attendance mark for Course ID {course_id}: ")
            midterm = float_input(f"Enter midterm mark for Course ID {course_id}: ")
            final = float_input(f"Enter final mark for Course ID {course_id}: ")
            student.add_attendance(course_id, attendance)
            student.add_midterm(course_id, midterm)
            student.add_final(course_id, final)

    write_marks(students)
    show_courses(courses)
    sort_gpa(students, courses)
    show_marks(students)

    compress_files()


if __name__ == '__main__':
    main()