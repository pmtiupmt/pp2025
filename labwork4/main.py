import curses
from domains.manager import MarkManager
import input as input_module
import output as output_module

def main():
    manager = MarkManager()

    input_module.input_students(manager)
    input_module.input_courses(manager)
    input_module.input_marks(manager)

    manager.sort_students_by_gpa()

    curses.wrapper(output_module.show_students, manager.students)

if __name__ == "__main__":
    main()
