import math
import numpy as np


class Student:
    def __init__(self, sid='', name='', dob=''):
        self._id = sid
        self._name = name
        self._dob = dob
        self.marks = {}   # {course_id: (mark, credit)}

    def input(self):
        self._id = input("ID: ")
        self._name = input("Name: ")
        self._dob = input("Date of birth: ")
     
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


class Course:
    def __init__(self, cid='', name='', credit=0):
        self._id = cid
        self._name = name
        self._credit = credit

    def input(self):
        self._id = input("Course ID: ")
        self._name = input("Course name: ")
        self._credit = int(input("Credit: "))

    def get_id(self):
        return self._id

    def get_credit(self):
        return self._credit

    def __str__(self):
        return f"{self._id} - {self._name} ({self._credit} credits)"


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for i in range(n):
            print(f"\nStudent {i + 1}")
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        n = int(input("\nNumber of courses: "))
        for i in range(n):
            print(f"\nCourse {i + 1}")
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        for c in self.courses:
            print(f"\nEnter marks for course {c.get_id()}")
            for s in self.students:
                raw = float(input(f"{s.get_name()}: "))
                mark = math.floor(raw * 10) / 10   # round-down to 1 digit
                s.add_mark(c.get_id(), mark, c.get_credit())

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.calculate_gpa(), reverse=True)

    def show_students(self):
        for s in self.students:
            print(s)


def main():
    manager = MarkManager()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()
    manager.sort_students_by_gpa()


if __name__ == "__main__":
    main()