from domains.manager import MarkManager
from input import input_students, input_courses, input_marks
from output import show_menu
import persistence


def main():
    manager = MarkManager()

    # Load saved data (synchronous)
    loaded = persistence.load_pickled_data(manager)

    if not loaded:
        input_students(manager)
        input_courses(manager)
        input_marks(manager)

    # Run main UI loop
    show_menu(manager)

    # Save data in background thread
    persistence.save_pickled_data_async(manager)


if __name__ == "__main__":
    main()
