import curses

def show_students(stdscr, students):
    curses.curs_set(0)
    stdscr.clear()

    stdscr.addstr(1, 2, "STUDENT GPA LIST (DESCENDING)")
    row = 3
    for s in students:
        stdscr.addstr(row, 2, str(s))
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()
