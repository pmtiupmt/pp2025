import os
import pickle
import gzip


DATA_FILE = "students.dat"


def save_data(manager):
    """
    Compress and save all persistent data before program exits.
    Data saved:
        - students
        - courses
    """
    data = {
        "students": manager.students,
        "courses": manager.courses
    }

    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)


def load_data(manager):
    """
    Load and decompress data when program starts.
    Return True if data loaded successfully, False otherwise.
    """
    if not os.path.exists(DATA_FILE):
        return False

    try:
        with gzip.open(DATA_FILE, "rb") as f:
            data = pickle.load(f)

        manager.students = data.get("students", [])
        manager.courses = data.get("courses", [])
        return True

    except Exception:
        # File corrupted or incompatible
        return False
