import math
import numpy as np

class Student:
    def __init__(self, sid='', name='', dob=''):
        self._id = sid
        self._name = name
        self._dob = dob
        self.marks = {}  # {course_id: (mark, credit)}

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def add_mark(self, course_id, mark, credit):
        self.marks[course_id] = (mark, credit)

    def calculate_gpa(self):
        if not self.marks:
            return 0.0

        marks = np.array([m for m, c in self.marks.values()])
        credits = np.array([c for m, c in self.marks.values()])
        gpa = np.sum(marks * credits) / np.sum(credits)

        return math.floor(gpa * 10) / 10

    def __str__(self):
        return f"{self._id} - {self._name} | GPA: {self.calculate_gpa()}"
