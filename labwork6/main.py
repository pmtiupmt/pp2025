import persistence

manager = MarkManager()

loaded = persistence.load_pickled_data(manager)

if not loaded:
    input_students(manager)
    input_courses(manager)
    input_marks(manager)

# chương trình chạy bình thường

persistence.save_pickled_data(manager)
