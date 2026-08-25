import os
from tkinter import ttk


class Users:
    def __init__(self, parrent: ttk.Frame) -> None:
        self.parrent = parrent
        self.frame = ttk.Frame(parrent)
        self.frame.pack()

    def generate(self):
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
        self.generate()

    def pack_user(self, name_str, phone_str, initials_str):
        user = ttk.Frame(self.frame)
        name = ttk.Label(master=user, text = name_str.replace("_", " "))
        phone = ttk.Label(master=user, text = phone_str)
        initials = ttk.Label(master=user, text = initials_str)
        name.pack(side = "left", padx=10)
        phone.pack(side = "left", padx=10)
        initials.pack(side = "left", padx=10)
        delete_user = ttk.Button(
            master=user,
            text="delete user",
            command=lambda: self.delete_user(name_str, phone_str, initials_str),
        )
        delete_user.pack()
        user.pack(pady = 10)
