from .Person import Person
import numpy as np

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
            return None
        marks = {}
        for course_id in self._attendance:
            if course_id in self._midterm and course_id in self._final:
                attendance = self._attendance[course_id]
                midterm = self._midterm[course_id]
                final = self._final[course_id]
                marks[course_id] = {
                    'attendance': attendance,
                    'midterm': midterm,
                    'final': final
                }
        return marks

    import numpy as np

    def calculate_gpa(self, courses):
        if not self._attendance or not self._midterm or not self._final:
            return 0

        total_credits = 0
        total_gpa = 0
        weighted_sum = 0

        for course_id in self._attendance:
            if course_id in self._midterm and course_id in self._final:
                attendance = self._attendance[course_id]
                midterm = self._midterm[course_id]
                final = self._final[course_id]
                total_marks = attendance * 0.1 + midterm * 0.3 + final * 0.6

                for course_id, course in courses.items():
                    if course._id == course_id:
                        credit = course.get_credit()
                        total_credits += credit
                        weighted_sum += total_marks * credit

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

        average_gpa = weighted_sum / total_credits

        return average_gpa, weighted_sum
