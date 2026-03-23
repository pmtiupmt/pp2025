import os
import pickle
import gzip
import threading

DATA_FILE = "students.dat"


def _save_task(data):
    """
    Background thread task to save data
    """
    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)


def save_pickled_data_async(manager):
    """
    Save system data in background thread
    """
    data = {
        "students": manager.students,
        "courses": manager.courses
    }

    thread = threading.Thread(
        target=_save_task,
        args=(data,),
        daemon=True
    )
    thread.start()


def load_pickled_data(manager):
    """
    Load pickled data synchronously on startup
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
