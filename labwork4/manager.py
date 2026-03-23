from domains.student import Student
from domains.course import Course
import math

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def sort_students_by_gpa(self):
        self.students.sort(
            key=lambda s: s.calculate_gpa(),
            reverse=True
        )
