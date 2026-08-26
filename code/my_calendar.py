import calendar
import datetime
import os
import tkinter as tk
from tkinter import ttk

from lookup_turns import after, lookup_turns


class my_calendar:
    def __init__(self, parrent, user_picker) -> None:
        self.parrent = parrent
        today = datetime.date.today()  # noqa: DTZ011
        self.year = today.year
        self.month = today.month
        self.frame = ttk.Frame(master=self.parrent)
        self.user_picker = user_picker
        self.frame.pack()
        self.parrent.pack()

    def generate(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(master=self.parrent, relief=tk.GROOVE)
        top_bar = ttk.Frame(master=self.frame, width=60 * 7, height=25)
        top_bar.pack_propagate(False)
        month_scroller = ttk.Frame(master=top_bar)

        month_down_button = ttk.Button(
            master=month_scroller, text="◀", command=self.month_down, width=2
        )
        current_month_holder = ttk.Frame(master=month_scroller, width=75, height=20)
        current_month_holder.pack_propagate(False)
        current_month = ttk.Label(
            master=current_month_holder, text=str(calendar.month_name[self.month])
        )

        month_up_button = ttk.Button(
            master=month_scroller, text="▶", command=self.month_up, width=2
        )

        current_year = ttk.Label(master=top_bar, text=str(self.year))
        month_down_button.pack(side="left")
        current_month.pack()
        current_month_holder.pack(side="left", padx=10)
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
            label = ttk.Label(master=box, text=day)
            label.pack(pady=2)
            box.pack(side="left")
        days_row.pack()

        cal = calendar.Calendar(firstweekday=0)
        weeks = cal.monthdayscalendar(self.year, self.month)
        users = lookup_turns(self.year, self.month)
        for week in weeks:
            week_row = ttk.Frame(master=calendar_table)
            for day in week:
                box = ttk.Frame(master=week_row, width=60, height=50, relief=tk.GROOVE)
                box.pack_propagate(False)
                if day != 0:
                    user = users[day - 1]
                    label = ttk.Label(master=box, text=day)
                    label.pack()
                    if user[2]:
                        set_turn = ttk.Button(
                            master=box,
                            text=f"({user[0]})",
                            width=4,
                            command=lambda x=user[1]: self.remove_turn(x),
                        )
                    else:
                        set_turn = ttk.Button(
                            master=box,
                            text=user[0],
                            width=4,
                            command=lambda x=int(day): self.save_turn(
                                (self.year, self.month, x)
                            ),
                        )
                    set_turn.pack()

                box.pack(side="left")
            week_row.pack()

        calendar_table.pack(pady=10)

        self.frame.pack(pady=20)

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

    def save_turn(self, date: tuple[int, int, int]):
        if self.user_picker.user_selected.get() == "none":
            return
        new_turn = f"{self.user_picker.user_selected.get().replace(' ', '_')} {date[0]} {date[1]} {date[2]}\n"
        abs_turns = os.path.abspath("storage/turns.txt")
        with open(abs_turns, "r") as f:
            turns = f.read().splitlines()
        content = ""
        placed = False
        for turn in turns:
            _, ny, nm, nd = turn.split()
            next_date = (int(ny), int(nm), int(nd))
            if placed == False and after(next_date, date):
                content = content + new_turn
                placed = True
            content = content + f"{turn}\n"
        if not placed:
            content = content + new_turn
        with open(abs_turns, "w") as f:
            f.write(content)
        self.generate()



    def remove_turn(self, full_turn):
        abs_turns = os.path.abspath("storage/turns.txt")
        with open(abs_turns, "r") as f:
            content = f.read()
        content = content.replace(full_turn, "")
        with open(abs_turns, "w") as f:
            f.write(content)
        self.generate()
