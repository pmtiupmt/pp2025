import math
from domains.student import Student
from domains.course import Course

def input_students(manager):
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"\nStudent {i + 1}")
        s = Student()
        s._id = input("ID: ")
        s._name = input("Name: ")
        s._dob = input("DOB: ")
        manager.students.append(s)

def input_courses(manager):
    n = int(input("\nNumber of courses: "))
    for i in range(n):
        print(f"\nCourse {i + 1}")
        c = Course()
        c._id = input("Course ID: ")
        c._name = input("Course name: ")
        c._credit = int(input("Credit: "))
        manager.courses.append(c)

def input_marks(manager):
    for c in manager.courses:
        print(f"\nEnter marks for {c.get_id()}")
        for s in manager.students:
            raw = float(input(f"{s.get_name()}: "))
            mark = math.floor(raw * 10) / 10
            s.add_mark(c.get_id(), mark, c.get_credit())
