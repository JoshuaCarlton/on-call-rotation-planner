import os
import tkinter as tk
from tkinter import ttk

from my_calendar import my_calendar


def initialize_calendar_tab(parrent):
    calendar_tab = ttk.Frame(master=parrent)
    user_picker = UserPicker(calendar_tab)
    calendar = my_calendar(calendar_tab, user_picker)
    calendar.generate()
    calendar_tab.pack()
    return calendar_tab, user_picker, calendar




class UserPicker:
    def __init__(self, parrent) -> None:
        self.parrent = parrent
        self.user_selected = tk.StringVar()
        self.user_selected.set("none")
        self.user_list = []
        self.combo_box = ttk.Combobox(
            master=self.parrent, textvariable=self.user_selected, state="readonly"
        )
        self.combo_box["values"] = self.user_list
        self.combo_box.bind("<<ComboboxSelected>>", self.on_select)
        self.combo_box.pack()

    def list_users(self):
        abs_users = os.path.abspath("storage/users.txt")
        with open(abs_users, "r") as f:
            users = f.read().splitlines()
        self.user_list = []
        for user in users:
            name, _, _ = user.split()
            self.user_list.append(name.replace("_", " "))
        self.combo_box['values'] = self.user_list

    def on_select(self, event):
        event.widget.after_idle(event.widget.selection_clear)
