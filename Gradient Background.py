import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Sidebar
        self.sidebar = tk.Frame(self, bg="#030005", width=100)
        self.sidebar.pack(side="left", fill="y")

        self.separator = tk.Frame(self, bg="#1D1D1D", width=2)
        self.separator.pack(side="left", fill="y")

        # Keep sidebar width fixed
        self.sidebar.pack_propagate(False)

        # Sidebar title
        tk.Label(
            self.sidebar,
            text="Menu",
            bg="#111111",
            fg="#E6E6E6",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=20)

        # Example buttons
        tk.Button(
            self.sidebar,
            text="Dashboard",
            bg="#1A1A1A",
            fg="white",
            relief="flat"
        ).pack(fill="x", padx=15, pady=5)

        tk.Button(
            self.sidebar,
            text="Subjects",
            bg="#1A1A1A",
            fg="white",
            relief="flat"
        ).pack(fill="x", padx=15, pady=5)

        tk.Button(
            self.sidebar,
            text="Settings",
            bg="#1A1A1A",
            fg="white",
            relief="flat"
        ).pack(fill="x", padx=15, pady=5)

        # Main content area
        self.main = GradientFrame(self, borderwidth=0, highlightthickness=0)
        self.main.pack(side="left", fill="both", expand=True)




class GradientFrame(tk.Canvas):
    # A gradient frame which uses a canvas to draw the background
    def __init__(self, parent, color1="#05000A", color2="#010003", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        self.delete("gradient")
        self.delete("text")

        width = self.winfo_width()
        height = self.winfo_height()
        limit = height

        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)

        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))

            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)

            self.create_line(0, i, width, i, fill=color, tags=("gradient",))

        self.lower("gradient")

        self.create_text(
            width // 7.5,
            height // 20,
            text="Revision Planner",
            fill="#D6CCFF",
            font=("Arial", 40, "bold"),
            tags=("text",)
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Revision Tracker")
    root.state("zoomed")
    root.geometry("1920x1080")
    root.minsize(960, 540)
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
