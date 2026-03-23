import os
import pickle
import gzip

DATA_FILE = "students.dat"


def save_pickled_data(manager):
    """
    Serialize and compress system data using pickle.
    """
    data = {
        "students": manager.students,
        "courses": manager.courses
    }

    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)


def load_pickled_data(manager):
    """
    Load and decompress pickled system data.
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
        return False
