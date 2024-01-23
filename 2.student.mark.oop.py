class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self._dob = dob
        self._mark = {}

    def add_mark(self, course_id, mark):
        self._mark[course_id] = mark

    def show_marks(self):
        if not self._mark:
            print("No marks available for the student.")
        else:
            print(f"Student ID: {self._id}")
            for course_id, mark in self._mark.items():
                print(f"Course ID: {course_id}, Mark: {mark}")


class Course:
    def __init__(self, course_id, name):
        self._id = course_id
        self._name = name


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
        course = Course(course_id, name)
        self._courses.append(course)

    def add_mark(self, student_id):
        course_id = input("Enter course ID:")
        mark = int(input(f"Enter the mark for student {student_id} in course {course_id}:"))
        student = self._find_student(student_id)
        if student:
            student.add_mark(course_id, mark)
        else:
            print("Student not found.")

    def list_students(self):
        if not self._students:
            print("There are no students.")
        else:
            for student in self._students:
                print(f"Student ID: {student._id}, Student Name: {student._name}")

    def list_courses(self):
        if not self._courses:
            print("There are no courses.")
        else:
            for course in self._courses:
                print(f"Course ID: {course._id}, Course Name: {course._name}")

    def show_marks(self, student_id):
        student = self._find_student(student_id)
        if student:
            student.show_marks()
        else:
            print("Student not found.")


    def manage(self):
        while True:
            print("\n1. Add student")
            print("2. Add course")
            print("3. Input student's marks")
            print("4. Show student's marks")
            print("5. List students")
            print('6. List courses')
            print("7. Exit")

            option = int(input("Your choice:"))

            if option == 1:
                student_id = input("ID: ")
                name = input("Student's name:")
                dob = input("Student's date of birth:")
                self.add_student(student_id, name, dob)
            elif option == 2:
                course_id = input("Course ID: ")
                name = input("Course name:")
                self.add_course(course_id, name)
            elif option == 3:
                student_id = input("Enter student ID: ")
                self.add_mark(student_id)
            elif option == 4:
                student_id = input("Enter student ID:")
                self.show_marks(student_id)
            elif option == 5:
                self.list_students()
            elif option == 6:
                self.list_courses()
            elif option == 7:
                break
            else:
                print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    my_mark_management_system = ManagementSystem()
    my_mark_management_system.manage()