# ---------------- IMPORTS ----------------

import customtkinter as ctk
from tkinter import messagebox
import csv
import os
import random

# ---------------- EXTRAS ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Revision Planner")
app.geometry("1100x640")
app.minsize(540, 295)

# ---------------- DATA ----------------

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

weeks = ["Week A", "Week B"]

periods_week_a = ["Period 1", "Period 2", "Break", "Period 3", "Period 4", "Lunch", "Period 6", "Period 7"]
periods_week_b = ["Period 1", "Period 2", "Break", "Period 3", "Period 4", "Lunch", "Period 6", "Period 7"]

period_times_week_a = {
    "Period 1": "08:35 - 09:25",
    "Period 2": "09:25 - 10:15",
    "Break": "10:15 - 10:55",
    "Period 3": "10:55 - 11:45",
    "Period 4": "11:45 - 12:35",
    "Lunch": "12:35 - 01:25",
    "Period 6": "01:25 - 02:15",
    "Period 7": "02:15 - 03:10"
}

period_times_week_b = {
    "Period 1": "08:35 - 09:25",
    "Period 2": "09:25 - 10:15",
    "Break": "10:15 - 10:55",
    "Period 3": "10:55 - 11:45",
    "Period 4": "11:45 - 12:35",
    "Lunch": "12:35 - 01:25",
    "Period 6": "01:25 - 02:15",
    "Period 7": "02:15 - 03:10"
}

CSV_FILE_WEEK_A = "weeka.csv"
CSV_FILE_WEEK_B = "weekb.csv"

excluded_subjects = ["house", "academic", "lunch"]

# ---------------- TIMETABLE ----------------
timetable_week_a = {}
for period in periods_week_a:
    timetable_week_a[period] = {}
    for day in days:
        timetable_week_a[period][day] = ""

timetable_week_b = {}
for period in periods_week_b:
    timetable_week_b[period] = {}
    for day in days:
        timetable_week_b[period][day] = ""

# ---------------- FUNCTIONS ----------------

def get_csv_file():
    if week_var.get() == "Week A":
        return CSV_FILE_WEEK_A
    else:
        return CSV_FILE_WEEK_B

def get_periods():
    if week_var.get() == "Week A":
        return periods_week_a
    else:
        return periods_week_b

def get_period_times():
    if week_var.get() == "Week A":
        return period_times_week_a
    else:
        return period_times_week_b

def get_timetable():
    if week_var.get() == "Week A":
        return timetable_week_a
    else:
        return timetable_week_b

def get_next_slot_number():
    active_periods = get_periods()
    highest_number = 0

    for period in active_periods:
        if period.startswith("Slot "):
            number_part = period[5:]

            if number_part.isdigit():
                number = int(number_part)
                if number > highest_number:
                    highest_number = number

    return highest_number + 1

def get_all_subjects():
    subjects = []

    for timetable in [timetable_week_a, timetable_week_b]:
        for period in timetable:
            for day in days:
                subject = timetable[period][day].strip()

                if subject and not subject.startswith("Revision:"):
                    if subject.lower() not in excluded_subjects:
                        if subject not in subjects:
                            subjects.append(subject)

    return subjects

def randomise_revision():
    subjects = get_all_subjects()

    if not subjects:
        messagebox.showerror("Error", "Add some subjects first.")
        return

    timetable = get_timetable()

    for period in get_periods():
        for day in days:

            if timetable[period][day] == "":
                timetable[period][day] = "Revision: " + random.choice(subjects)

            elif timetable[period][day].startswith("Revision:"):
                timetable[period][day] = "Revision: " + random.choice(subjects)

    save_csv()
    refresh_grid()

def refresh_grid():
    for widget in grid_frame.winfo_children():
        widget.destroy()

    active_periods = get_periods()
    active_period_times = get_period_times()
    active_timetable = get_timetable()

    header_time = ctk.CTkLabel(
        grid_frame, text="Time", fg_color="#1f6aa5",
        text_color="white", font=("Arial", 14, "bold"),
        width=220, height=40, corner_radius=0
    )
    header_time.grid(row=0, column=0, sticky="nsew", padx=(0, 1), pady=(0, 1))

    day_column = 1
    for day in days:
        header_day = ctk.CTkLabel(
            grid_frame, text=day, fg_color="#1f6aa5",
            text_color="white", font=("Arial", 14, "bold"),
            width=180, height=40, corner_radius=0
        )
        header_day.grid(row=0, column=day_column, sticky="nsew", padx=(0, 1), pady=(0, 1))
        day_column = day_column + 1

    row_number = 1
    for period in active_periods:
        time = active_period_times.get(period, "")

        if time:
            time_text = f"{period} ({time})"
        else:
            time_text = period

        time_cell = ctk.CTkLabel(
            grid_frame, text=time_text, fg_color="#1e1e1e",
            text_color="white", font=("Arial", 13, "bold"),
            width=220, height=40, corner_radius=0, anchor="w", padx=10
        )
        time_cell.grid(row=row_number, column=0, sticky="nsew", padx=(0, 1), pady=(0, 1))

        day_column = 1
        for day in days:
            subject = active_timetable[period][day]

            if subject.startswith("Revision:"):
                text_color = "red"
            else:
                text_color = "white"

            subject_cell = ctk.CTkLabel(
                grid_frame, text=subject, fg_color="#1e1e1e",
                text_color=text_color, font=("Arial", 13, "bold"),
                width=180, height=40, corner_radius=0
            )
            subject_cell.grid(row=row_number, column=day_column, sticky="nsew", padx=(0, 1), pady=(0, 1))
            day_column = day_column + 1

        row_number = row_number + 1

def refresh_time_dropdown():

    active_periods = get_periods()

    time_menu.configure(values=active_periods)

    if time_var.get() not in active_periods and len(active_periods) > 0:
        time_var.set(active_periods[0])

def save_csv():
    csv_file = get_csv_file()
    active_periods = get_periods()
    active_period_times = get_period_times()
    active_timetable = get_timetable()

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)

        header = ["Period", "Time"]
        for day in days:
            header.append(day)
        writer.writerow(header)

        for period in active_periods:
            row = [period, active_period_times.get(period, "")]
            for day in days:
                row.append(active_timetable[period][day])
            writer.writerow(row)

def load_csv_for_week(week_name):
    if week_name == "Week A":
        csv_file = CSV_FILE_WEEK_A
        active_periods = periods_week_a
        active_period_times = period_times_week_a
        active_timetable = timetable_week_a
    else:
        csv_file = CSV_FILE_WEEK_B
        active_periods = periods_week_b
        active_period_times = period_times_week_b
        active_timetable = timetable_week_b

    if not os.path.exists(csv_file):
        return

    with open(csv_file, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if len(row) < len(days) + 2:
                continue

            period = row[0]
            time_value = row[1]

            if period not in active_timetable:
                active_periods.append(period)
                active_timetable[period] = {}
                for day in days:
                    active_timetable[period][day] = ""

            if time_value:
                active_period_times[period] = time_value

            day_index = 0
            for day in days:
                active_timetable[period][day] = row[day_index + 2]
                day_index = day_index + 1

def save_entry():
    day = day_var.get()
    period = time_var.get()
    subject = subject_entry.get().strip()

    if not subject:
        messagebox.showerror("Error", "Enter a subject")
        return

    active_timetable = get_timetable()
    active_timetable[period][day] = subject

    save_csv()
    refresh_grid()

    subject_entry.delete(0, "end")

def delete_entry():
    day = day_var.get()
    period = time_var.get()

    active_timetable = get_timetable()
    active_timetable[period][day] = ""

    save_csv()
    refresh_grid()

def change_week(choice):
    refresh_grid()
    refresh_time_dropdown()

def add_new_time_row():
    entered_time = time_slot_entry.get().strip()

    if not entered_time:
        messagebox.showerror("Error", "Enter a time slot")
        return

    active_periods = get_periods()
    active_period_times = get_period_times()
    active_timetable = get_timetable()

    new_period = "Slot " + str(get_next_slot_number())

    active_periods.append(new_period)
    active_period_times[new_period] = entered_time

    active_timetable[new_period] = {}
    for day in days:
        active_timetable[new_period][day] = ""

    refresh_grid()
    refresh_time_dropdown()

    save_csv()

    time_slot_entry.delete(0, "end")

def delete_time_row():
    period = time_var.get()

    active_periods = get_periods()
    active_period_times = get_period_times()
    active_timetable = get_timetable()

    if period not in active_periods:
        messagebox.showerror("Error", "No row selected to delete")
        return

    confirmed = messagebox.askyesno(
        "Delete Row",
        "Delete '" + period + "' from " + week_var.get() + "?\n"
        "This will remove all subjects entered for this row.\n\n"
        "This cannot be undone."
    )

    if not confirmed:
        return

    active_periods.remove(period)

    if period in active_period_times:
        del active_period_times[period]

    if period in active_timetable:
        del active_timetable[period]

    refresh_grid()
    refresh_time_dropdown()

    save_csv()

# ---------------- INPUTS ----------------

controls = ctk.CTkFrame(app)
controls.pack(fill="x", padx=20, pady=10)
controls.grid_columnconfigure(4, weight=1)

ctk.CTkLabel(controls, text="Week").grid(row=0, column=0, padx=5)
week_var = ctk.StringVar(value=weeks[0])
ctk.CTkOptionMenu(controls, values=weeks, variable=week_var, command=change_week).grid(row=1, column=0, padx=5)

ctk.CTkLabel(controls, text="Day").grid(row=0, column=1, padx=5)
day_var = ctk.StringVar(value=days[0])
ctk.CTkOptionMenu(controls, values=days, variable=day_var).grid(row=1, column=1, padx=5)

ctk.CTkLabel(controls, text="Time Slot").grid(row=0, column=2, padx=5)
time_var = ctk.StringVar(value=periods_week_a[0])
time_menu = ctk.CTkOptionMenu(controls, values=periods_week_a, variable=time_var)
time_menu.grid(row=1, column=2, padx=5)

ctk.CTkLabel(controls, text="Subject").grid(row=0, column=3, padx=5)
subject_entry = ctk.CTkEntry(controls, width=180)
subject_entry.grid(row=1, column=3, padx=5)

ctk.CTkButton(controls, text="Add", command=save_entry).grid(row=1, column=4, padx=10, sticky="e")

# ---------------- TABLE ----------------

frame = ctk.CTkFrame(app)
frame.pack(fill="x", expand=False, pady=20)

grid_frame = ctk.CTkFrame(frame, fg_color="#1e1e1e")
grid_frame.pack(fill="both", expand=True, padx=1, pady=1)

# ---------------- BUTTONS ----------------

bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(fill="x", padx=20, pady=10)

bottom_frame.grid_columnconfigure(0, weight=1)

inner = ctk.CTkFrame(bottom_frame)
inner.grid(row=0, column=0, pady=10)

inner.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(inner, text="Time Slot").grid(row=0, column=0, padx=10, pady=(0, 5))

time_slot_entry = ctk.CTkEntry(inner, width=200, placeholder_text="4:10 - 5:10")
time_slot_entry.grid(row=1, column=0, padx=10)

ctk.CTkButton(inner, text="Add a New Row", command=add_new_time_row).grid(row=1, column=1, padx=10)
ctk.CTkButton(inner, text="Delete Selected Row", fg_color="#a53d3d", hover_color="#7a2c2c", command=delete_time_row).grid(row=1, column=2, padx=10)

ctk.CTkButton(inner, text="Randomise Revision", command=randomise_revision).grid(row=1, column=3, padx=(30, 10), sticky="e")

# ---------------- MAIN ----------------

load_csv_for_week("Week A")
load_csv_for_week("Week B")

refresh_grid()
refresh_time_dropdown()

app.mainloop()