def show_timetable(lecture_grid):
    print("\n===== COMPLETE TIMETABLE =====")
    for orbit in lecture_grid:
        print(f"{orbit['day']:9} | {orbit['time']:5} | "
            f"{orbit['subject']:12} | {orbit['room']}")
