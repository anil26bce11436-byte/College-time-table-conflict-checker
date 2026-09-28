def check_free_slot(lecture_grid):

    print("\n===== FREE SLOT CHECKER =====")

    pick_day = input("Enter Day: ").title()
    pick_time = input("Enter Time (HH:MM): ")

    vacant = True

    for pulse in lecture_grid:

        if pulse["day"] == pick_day and pulse["time"] == pick_time:

            vacant = False

            print("\nClass Found")
            print("Subject :", pulse["subject"])
            print("Teacher :", pulse["teacher"])
            print("Room    :", pulse["room"])

    if vacant:
        print("\nNo class scheduled.")
        print("This slot is FREE!")
