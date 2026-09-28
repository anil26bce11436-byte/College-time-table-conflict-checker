from timetable_data import lecture_grid
from conflict_scanner import scan_conflicts
from free_slot import check_free_slot
from timetable_view import show_timetable

clash_log, room_hits, teacher_hits = scan_conflicts(lecture_grid)

print("\n===== TIMETABLE AUDIT REPORT =====\n")

if clash_log:
    for item in clash_log:
        print("⚠", item)
else:
    print("No conflicts found.")

print("\n--- Summary ---")
print("Room Conflicts   :", room_hits)
print("Teacher Conflicts:", teacher_hits)
print("Total Conflicts  :", len(clash_log))

check_free_slot(lecture_grid)

show_timetable(lecture_grid)

print("\nSystem Check Complete.")
