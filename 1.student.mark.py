def input_student_info():
    return {
        'id': input("ID: "),
        'name': input("Student's name: "),
        'marks': {}
    }

def input_course_info():
    return {
        'id': input("Course ID: "),
        'name': input("Course's name: ")
    }

def input_mark(student):
    course_id = input("Enter the course ID: ")
    mark = int(input(f"Enter the mark for student {student['id']} in course {course_id}: "))
    student['marks'][course_id] = mark

def list_students(students):
    if len(students) == 0:
        print("There are no students.")
    else:
        for student in students:
            print(f"Student ID: {student['id']}, Student Name: {student['name']}")

def list_courses(courses):
    if len(courses) == 0:
        print("There are no courses.")
    else:
        for course in courses:
            print(f"Course ID: {course['id']}, Course Name: {course['name']}")

def show_marks(students, student_id):
    for student in students:
        if student['id'] == student_id:
            marks = student['marks']
            if len(marks) == 0:
                print("No marks available for the student.")
            else:
                print(f"Student ID: {student['id']}, Marks:")
                for course_id, mark in marks.items():
                    print(f"Course ID: {course_id}, Mark: {mark}")
            return
    print("Student not found.")

def main():
    courses = []
    students = []

    while True:
        print("\n1. Add student")
        print("2. Add course")
        print("3. Input student's marks")
        print("4. Show student's marks")
        print("5. List students")
        print("6. List courses")
        print("7. Exit")

        option = int(input("Your choice: "))

        if option == 1:
            students.append(input_student_info())
        elif option == 2:
            courses.append(input_course_info())
        elif option == 3:
            student_id = input("Enter student ID: ")
            found = False
            for student in students:
                if student['id'] == student_id:
                    input_mark(student)
                    found = True
                    break
            if not found:
                print("Student not found.")
        elif option == 4:
            student_id = input("Enter student ID: ")
            show_marks(students, student_id)
        elif option == 5:
            list_students(students)
        elif option == 6:
            list_courses(courses)
        elif option == 7:
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
