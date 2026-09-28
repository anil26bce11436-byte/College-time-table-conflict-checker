# College Timetable Conflict Checker

A Python-based console application that detects timetable scheduling
conflicts in a college. The system identifies room and teacher
conflicts, checks free time slots, and displays the complete timetable.

# Project Overview

Managing a college timetable manually can lead to scheduling errors,
such as assigning the same classroom or the same teacher to multiple
classes at the same time. This project automatically scans the timetable
and reports such conflicts, making timetable verification faster and
more reliable.


## Features

-   Detects **Room Conflicts**
-   Detects **Teacher Conflicts**
-   Displays a **Conflict Summary**
-   Checks whether a selected time slot is **Free or Occupied**
-   Displays the **Complete Timetable**

## Project Structure

``` text
College-Timetable-Conflict-Checker/
-main.py
-timetable_data.py
-conflict_scanner.py
-free_slot.py
-timetable_view.py
-README.md
-statement.md


## Functional Modules

### 1. Conflict Scanner

-   Compares classes scheduled on the same day and time.
-   Detects room conflicts.
-   Detects teacher conflicts.

### 2. Free Slot Checker

-   Accepts day and time as input.
-   Shows whether the slot is free.
-   Displays class details if occupied.

### 3. Timetable Viewer

-   Displays the complete timetable.
-   Shows day, time, subject, and room.

## Technologies Used

-   Python 3
-   Lists
-   Dictionaries
-   Functions
-   Nested Loops
-   Conditional Statements

## How to Run

### Requirements

-   Python 3 installed

### Steps

1.  Download or clone the project.
2.  Open the project folder.
3.  Run:

bash
python main.py


## Sample Output

``` text
===== TIMETABLE AUDIT REPORT =====

⚠ ROOM: Python & English -> Room 101

--- Summary ---
Room Conflicts   : 1
Teacher Conflicts: 0
Total Conflicts  : 1

