def scan_conflicts(lecture_grid):

    clash_log = []
    room_hits = 0
    teacher_hits = 0

    for echo_slot in range(len(lecture_grid)):
        for ripple_slot in range(echo_slot + 1, len(lecture_grid)):

            alpha = lecture_grid[echo_slot]
            beta = lecture_grid[ripple_slot]

            if alpha["day"] == beta["day"] and alpha["time"] == beta["time"]:

                if alpha["room"] == beta["room"]:
                    room_hits += 1
                    clash_log.append(f"ROOM: {alpha['subject']} & {beta['subject']} -> {alpha['room']}")

                if alpha["teacher"] == beta["teacher"]:
                    teacher_hits += 1
                    clash_log.append(f"TEACHER: {alpha['subject']} & {beta['subject']} -> {alpha['teacher']}")

    return clash_log, room_hits, teacher_hits
