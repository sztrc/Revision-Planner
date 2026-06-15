import tkinter as tk
import customtkinter as ctk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Sidebar
        self.sidebar = tk.Frame(self, bg="#030005", width=75)
        self.sidebar.pack(side="left", fill="y")

        self.divider = tk.Frame(self, bg="#1D1D1D", width=2)
        self.divider.pack(side="left", fill="y")

        # Keep sidebar width fixed
        self.sidebar.pack_propagate(False)

# ----------------------------------------------------------------------------------------------------------------------

        # Sidebar title
        tk.Label(
            self.sidebar,
            text="☰",
            bg="#030005",
            fg="#E6E6E6",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=20)

        #Sidebar Buttons
        button = ctk.CTkButton(
            self.sidebar,
            text="📊",
            font=("Segoe UI Emoji", 20),
            width=50,
            height=50,
            corner_radius=12,
            fg_color="#1A1A1A",
            hover_color="#35205E"
        ).pack(pady=5)

        button = ctk.CTkButton(
            self.sidebar,
            text="📅",
            font=("Segoe UI Emoji", 20),
            width=50,
            height=50,
            corner_radius=12,
            fg_color="#1A1A1A",
            hover_color = "#35205E"
        ).pack(pady=5)

        button = ctk.CTkButton(
            self.sidebar,
            text="📈",
            font=("Segoe UI Emoji", 20),
            width=50,
            height=50,
            corner_radius=12,
            fg_color="#1A1A1A",
            hover_color = "#35205E"
        ).pack(pady=5)

        button = ctk.CTkButton(
            self.sidebar,
            text="🎯",
            font=("Segoe UI Emoji", 20),
            width=50,
            height=50,
            corner_radius=12,
            fg_color="#1A1A1A",
            hover_color = "#35205E"
        ).pack(pady=5)

        button = ctk.CTkButton(
            self.sidebar,
            text="⚙",
            font=("Segoe UI Emoji", 20),
            width=50,
            height=50,
            corner_radius=12,
            fg_color="#1A1A1A",
            hover_color = "#35205E"
        ).pack(pady=5)

# ----------------------------------------------------------------------------------------------------------------------

        self.main = tk.Canvas(
            self,
            bg="#05000A",
            highlightthickness=0,
            bd=0
        )
        self.main.pack(side="left", fill="both", expand=True)

        container = tk.Frame(self.main, bg="#05000A", bd=0, highlightthickness=0)

        self.main.create_window(
            915, 535,
            window=container
        )

        row = ctk.CTkFrame(container, fg_color="transparent")
        row.pack()

        # First Box
        self.first_box = ctk.CTkFrame(
            row,
            width=425,
            height=325,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.first_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.first_box,
            text="Today's Progress",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25,y=20)

        # Second Box
        self.second_box = ctk.CTkFrame(
            row,
            width=425,
            height=325,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.second_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.second_box,
            text="Study Time",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25, y=20)

        # Third Box
        self.third_box = ctk.CTkFrame(
            row,
            width=425,
            height=325,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.third_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.third_box,
            text="Tasks Completed",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25, y=20)

        # Fourth Box
        self.fourth_box = ctk.CTkFrame(
            row,
            width=425,
            height=325,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.fourth_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.fourth_box,
            text="Upcoming",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25, y=20)

        row2 = ctk.CTkFrame(container, fg_color="transparent")
        row2.pack()

        # Fifth Box
        self.fifth_box = ctk.CTkFrame(
            row2,
            width=750,
            height=540,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.fifth_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.fifth_box,
            text="Today's Schedule",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25, y=20)

        self.dropdown = ctk.CTkOptionMenu(
            self.fifth_box,
            fg_color="#0D0021",
            dropdown_fg_color="#0D0021",
            dropdown_hover_color="#12002E",
            button_color="#0D0021",
            font=("Arial", 15, "bold"),
            dropdown_font=("Arial", 15, "bold"),
            corner_radius=10,
            values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        )
        self.dropdown.place(x=25, y=65)

        # Sixth Box
        self.sixth_box = ctk.CTkFrame(
            row2,
            width=1010,
            height=540,
            corner_radius=20,
            fg_color="#06000F",
            border_width=2,
            border_color="#0F0F0F"
        )
        self.sixth_box.pack(side="left", padx=15, pady=15, anchor="w")

        title = ctk.CTkLabel(
            self.sixth_box,
            text="Subjects Overview",
            font=("Arial", 25, "bold"),
            text_color="white"
        )
        title.place(x=25, y=20)

        container = tk.Frame(self.main, bg="#05000A", bd=0, highlightthickness=0)

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Revision Tracker")
    root.state("zoomed")
    root.geometry("1920x1080")
    root.minsize(960, 540)
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
