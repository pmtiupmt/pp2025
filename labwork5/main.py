import persistence

manager = MarkManager()

loaded = persistence.load_data(manager)

if not loaded:
    input_students(manager)
    input_courses(manager)
    input_marks(manager)

# chạy chương trình bình thường

persistence.save_data(manager)
