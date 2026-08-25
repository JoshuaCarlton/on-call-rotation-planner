import calendar
import datetime
import tkinter as tk
from tkinter import ttk


class my_calendar:
    def __init__(self, parrent) -> None:
        self.parrent = parrent
        today = datetime.date.today()  # noqa: DTZ011
        self.year = today.year
        self.month = today.month
        self.frame = ttk.Frame(master=self.parrent)
        self.frame.pack()
        self.parrent.pack()

    def generate(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(master=self.parrent, relief=tk.GROOVE)
        top_bar = ttk.Frame(master=self.frame, width=60*7, height=25)
        top_bar.pack_propagate(False)
        month_scroller = ttk.Frame(master=top_bar)

        month_down_button = ttk.Button(
            master=month_scroller, text="◀", command=self.month_down
        )
        current_month = ttk.Label(
            master=month_scroller, text=str(self.month)
        )

        month_up_button = ttk.Button(
            master=month_scroller, text="▶", command=self.month_up
        )

        current_year = ttk.Label(master=top_bar, text=str(self.year))
        month_down_button.pack(side="left")
        current_month.pack(side="left", padx=10)
        month_up_button.pack(side="left")
        month_scroller.pack(side="left")
        current_year.pack(side="right")
        top_bar.pack(pady=5, padx=5)

        calendar_table = ttk.Frame(master=self.frame)
        days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days_row = ttk.Frame(master=calendar_table)
        for day in days_of_the_week:
            box = ttk.Frame(master=days_row, width=60, height=25, relief=tk.GROOVE)
            box.pack_propagate(False)
            label = ttk.Label(master=box, text = day)
            label.pack()
            box.pack(side="left")
        days_row.pack()

        calendar_table.pack(pady = 10)

        self.frame.pack(pady = 20)

    def month_down(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.generate()

    def month_up(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.generate()
