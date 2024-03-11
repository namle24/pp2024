class Course:
    def __init__(self, course_id, name, credit):
        self._id = course_id
        self._name = name
        self._credit = credit

    def get_credit(self):
        return self._credit