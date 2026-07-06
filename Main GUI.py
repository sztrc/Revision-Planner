# ---------------- IMPORTS ----------------

import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
import csv
import os

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

periods = [
    "Period 1",
    "Period 2",
    "Break",
    "Period 3",
    "Period 4",
    "Lunch",
    "Period 6",
    "Period 7"
]

period_times = {
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

# ---------------- FUNCTIONS ----------------
def get_csv_file():
    if week_var.get() == "Week A":
        return CSV_FILE_WEEK_A
    else:
        return CSV_FILE_WEEK_B

def refresh_grid():
    tree.delete(*tree.get_children())

    for period in periods:
        time_label = f"{period} ({period_times[period]})"
        row = [time_label] + [timetable[period][day] for day in days]
        tree.insert("", "end", values=row)

def save_csv():
    csv_file = get_csv_file()

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Time"] + days)

        for period in periods:
            writer.writerow(
                [period] +
                [timetable[period][day] for day in days]
            )

def load_csv():
    csv_file = get_csv_file()

    if not os.path.exists(csv_file):
        return

    with open(csv_file, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader, None)  # Skip header

        for row in reader:
            if len(row) < len(days) + 1:
                continue

            period = row[0]

            if period in timetable:
                for i, day in enumerate(days):
                    timetable[period][day] = row[i + 1]


def save_entry():
    day = day_var.get()
    period = time_var.get()
    subject = subject_entry.get().strip()

    if not subject:
        messagebox.showerror("Error", "Enter a subject")
        return

    timetable[period][day] = subject

    save_csv()
    refresh_grid()

    subject_entry.delete(0, "end")

def delete_entry():
    day = day_var.get()
    period = time_var.get()

    timetable[period][day] = ""

    save_csv()
    refresh_grid()

def change_week(choice):
    for period in periods:
        for day in days:
            timetable[period][day] = ""

    load_csv()
    refresh_grid()

# ---------------- INPUTS ----------------

controls = ctk.CTkFrame(app)
controls.pack(fill="x", padx=20, pady=10)
controls.grid_columnconfigure(4, weight=1)

ctk.CTkLabel(controls, text="Week").grid(row=0, column=0, padx=5)
week_var = ctk.StringVar(value=weeks[0])
ctk.CTkOptionMenu(
    controls,
    values=weeks,
    variable=week_var,
    command=change_week
).grid(row=1, column=0, padx=5)

ctk.CTkLabel(controls, text="Day").grid(row=0, column=1, padx=5)
day_var = ctk.StringVar(value=days[0])
ctk.CTkOptionMenu(controls, values=days, variable=day_var).grid(row=1, column=1, padx=5)

ctk.CTkLabel(controls, text="Time Slot").grid(row=0, column=2, padx=5)
time_var = ctk.StringVar(value=periods[0])
ctk.CTkOptionMenu(controls, values=periods, variable=time_var).grid(row=1, column=2, padx=5)

ctk.CTkLabel(controls, text="Subject").grid(row=0, column=3, padx=5)
subject_entry = ctk.CTkEntry(controls, width=180)
subject_entry.grid(row=1, column=3, padx=5)

ctk.CTkButton(controls, text="Add", command=save_entry).grid(row=1, column=4, padx=10, sticky="e")

# ---------------- GRID STORAGE ----------------
timetable = {t: {d: "" for d in days} for t in periods}

# ---------------- TABLE ----------------
frame = ctk.CTkFrame(app)
frame.pack(fill="x", expand=False, pady=20)

tree = ttk.Treeview(
    frame,
    columns=["Time"] + days,
    show="headings",
    height=len(periods)
)

tree.heading("Time", text="Time")
tree.column("Time", width=220, minwidth=235, anchor="w")

for d in days:
    tree.heading(d, text=d)
    tree.column(d, width=180, minwidth=195, anchor="center")

tree.pack(fill="both", expand=True)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#1e1e1e",
    foreground="white",
    fieldbackground="#1e1e1e",
    rowheight=40,
    borderwidth=0,
    font=("Arial", 13, "bold")
)

style.configure(
    "Treeview.Heading",
    background="#1f6aa5",
    font=("Arial", 14, "bold"),
    relief="flat",
)

style.map(
    "Treeview",
    background=[("selected", "#144870")],
    foreground=[("selected", "white")]
)

# ---------------- BUTTONS ----------------

ctk.CTkButton(
    app,
    text="Add to Timetable",
    command=save_entry
).pack(pady=10)

ctk.CTkButton(
    app,
    text="Save CSV",
    command=save_csv
).pack()

# ---------------- MAIN ----------------
load_csv()
refresh_grid()

app.mainloop()
