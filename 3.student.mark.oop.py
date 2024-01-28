import math
import numpy as np
import curses


class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name


class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self._dob = dob
        self._attendance = {}
        self._midterm = {}
        self._final = {}

    def add_attendance(self, course_id, attendance):
        self._attendance[course_id] = attendance

    def add_midterm(self, course_id, midterm):
        self._midterm[course_id] = midterm

    def add_final(self, course_id, final):
        self._final[course_id] = final

    def show_marks(self):
        if not self._attendance or not self._midterm or not self._final:
            print("No marks available for the student.")
        else:
            print(f"Student ID: {self._id}")
            for course_id in self._attendance:
                if course_id in self._midterm and course_id in self._final:
                    attendance = self._attendance[course_id]
                    midterm = self._midterm[course_id]
                    final = self._final[course_id]
                    total_marks = attendance * 0.1 + midterm * 0.3 + final * 0.6
                    print(f"Course ID: {course_id}, Total Mark: {total_marks}")

    def calculate_gpa(self, courses):
        if not self._attendance or not self._midterm or not self._final:
            return 0

        total_credits = 0
        total_gpa = 0

        for course_id in self._attendance:
            if course_id in self._midterm and course_id in self._final:
                attendance = self._attendance[course_id]
                midterm = self._midterm[course_id]
                final = self._final[course_id]
                total_marks = attendance * 0.1 + midterm * 0.3 + final * 0.6

                for course in courses:
                    if course._id == course_id:
                        credit = course.get_credit()
                        total_credits += credit

                        if total_marks >= 18:
                            gpa = 4.0
                        elif total_marks >= 16:
                            gpa = 3.6
                        elif total_marks >= 14:
                            gpa = 3.2
                        elif total_marks >= 12:
                            gpa = 2.8
                        elif total_marks >= 10:
                            gpa = 2.4
                        elif total_marks >= 8:
                            gpa = 2.0
                        elif total_marks >= 6:
                            gpa = 1.6
                        elif total_marks >= 4:
                            gpa = 1.2
                        elif total_marks >= 2:
                            gpa = 0.8
                        else:
                            gpa = 0.4

                        total_gpa += gpa * credit

        if total_credits == 0:
            return 0

        weighted_sum = np.sum(np.array(list(self._final.values())) * np.array(list(courses.values())))
        average_gpa = total_gpa / total_credits

        return average_gpa, weighted_sum


class Course:
    def __init__(self, course_id, name, credit):
        self._id = course_id
        self._name = name
        self._credit = credit

    def get_credit(self):
        return self._credit


class ManagementSystem:
    def __init__(self):
        self._courses = []
        self._students = []

    def _find_student(self, student_id):
        for student in self._students:
            if student._id == student_id:
                return student
        return None

    def add_student(self, student_id, name, dob):
        student = Student(student_id, name, dob)
        self._students.append(student)

    def add_course(self, course_id, name):
        credit = int(input("Enter the credit for the course: "))
        course = Course(course_id, name, credit)
        self._courses.append(course)

    def add_mark(self, student_id, course_id, mark):
        student = self._find_student(student_id)
        if student:
            if 0 <= mark <= 20:
                if course_id not in student._attendance:
                    attendance = int(input("Enter attendance mark: "))
                    student.add_attendance(course_id, attendance)
                if course_id not in student._midterm:
                    midterm = int(input("Enter midterm mark: "))
                    student.add_midterm(course_id, midterm)
                student.add_final(course_id, math.floor(mark*10)/10)
                print("Mark added successfully.")
            else:
                print("Invalid mark. Mark should be between 0 and 20.")
        else:
            print("Student not found.")

    def list_students(self):
        if not self._students:
            print("No students in the system.")
        else:
            print(f"\nList of Students:")
            for student in self._students:
                print(f"Student ID: {student._id}, Name: {student._name}")

    def list_courses(self):
        if not self._courses:
            print("There are no courses.")
        else:
            for course in self._courses:
                print(f"\nCourse ID: {course._id}, CourseName: {course._name}")

    def show_marks(self, student_id):
        student = self._find_student(student_id)
        if student:
            student.show_marks()
        else:
            print("Student not found.")

    def sort_gpa(self):
        if not self._students:
            print("No students in the system.")
        else:
            sorted_students = sorted(self._students, key=lambda student: student.calculate_gpa(self._courses), reverse=True)
            print("Sorted Students by GPA:")
            for student in sorted_students:
                print(f"Student ID: {student._id}, Name: {student._name}, GPA: {student.calculate_gpa(self._courses)}")

    def run(self):
        while True:
            print(f"\nManagement System Menu:")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Add Mark")
            print("4. Show mark")
            print("5. List Students")
            print("6. List Courses")
            print("7. Calculate GPA")
            print("8. Sorted by GPA")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                dob = input("Enter student date of birth: ")
                self.add_student(student_id, name, dob)
                print("Student added successfully.")

            elif choice == "2":
                course_id = int(input("Enter course ID: "))
                name = input("Enter course name: ")
                self.add_course(course_id, name)
                print("Course added successfully.")

            elif choice == "3":
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                mark = int(input("Enter mark: "))
                self.add_mark(student_id, course_id, mark)
                print("Mark added successfully.")

            elif choice == "4":
                student_id = int(input("Enter student ID:"))
                self.show_marks(student_id)

            elif choice == "5":
                self.list_students()

            elif choice == "6":
                self.list_courses()

            elif choice == "7":
                student_id = int(input("Enter student ID: "))
                student = self._find_student(student_id)
                if student:
                    gpa = student.calculate_gpa(self._courses)
                    print(f"Student ID: {student._id}, GPA: {gpa}")
                else:
                    print("Student not found.")

            elif choice == "8":
                self.sort_gpa()
            elif choice == "0":
                break

            else:
                print("Invalid choice. Please try again.\n")


# Create an instance of the ManagementSystem
management_system = ManagementSystem()

# Run the management system
management_system.run()