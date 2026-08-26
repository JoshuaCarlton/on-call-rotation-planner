import os
import tkinter as tk
from tkinter import ttk


class Users:
    def __init__(self, parrent: ttk.Frame, user_picker, calendar) -> None:
        self.parrent = parrent
        self.frame = ttk.Frame(parrent)
        self.user_picker = user_picker
        self.calendar = calendar
        self.frame.pack()

    def generate(self):
        self.user_picker.list_users()
        self.frame.pack_forget()
        self.frame = ttk.Frame(self.parrent)
        abs_users = os.path.abspath("storage/users.txt")
        with open(abs_users, "r") as f:
            content = f.read()
        lines = content.splitlines()
        for line in lines:
            name, phone, initials = line.split()
            self.pack_user(name, phone, initials)
        self.frame.pack()

    def delete_user(self, name, phone, initials):
        name = name.replace(" ", "_")
        abs_users = os.path.abspath("storage/users.txt")
        with open(abs_users, "r") as f:
            content = f.read()
        content = content.replace(f"{name} {phone} {initials}\n", "")
        with open(abs_users, "w") as f:
            f.write(content)
        delete_turns(name)
        self.generate()
        self.calendar.generate()

    def pack_user(self, name_str, phone_str, initials_str):
        user = ttk.Frame(self.frame, relief=tk.GROOVE)
        name = ttk.Label(master=user, text=name_str.replace("_", " "))
        phone = ttk.Label(master=user, text=phone_str)
        initials = ttk.Label(master=user, text=initials_str)
        name.pack(side="left", padx=10)
        phone.pack(side="left", padx=10)
        initials.pack(side="left", padx=10)
        delete_user = ttk.Button(
            master=user,
            text="delete user",
            command=lambda: self.delete_user(name_str, phone_str, initials_str),
        )
        delete_user.pack()
        user.pack(pady=10)


def delete_turns(name):
    abs_turns = os.path.abspath("storage/turns.txt")
    with open(abs_turns, "r") as f:
        turns = f.read().splitlines()
    content = ""
    for turn in turns:
        current_name, _, _, _ = turn.split()
        if name != current_name:
            content = content + f"{turn}\n"
    with open(abs_turns, "w") as f:
        f.write(content)
