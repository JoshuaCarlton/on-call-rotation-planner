import tkinter as tk
from tkinter import ttk

from save_user import save_user
from users import Users


def initialize_users_tab(parrent: ttk.Notebook, user_picker, calendar) -> ttk.Frame:
    user_tab = ttk.Frame(parrent)
    fields = ttk.Frame(user_tab)

    name_frame = ttk.Frame(fields)
    name_string = tk.StringVar()
    name_label = ttk.Label(master=name_frame, text="name")
    name_label.pack()
    name_entry = ttk.Entry(master=name_frame, textvariable=name_string)
    name_entry.pack()
    name_frame.pack(side="left", padx=10)

    phone_frame = ttk.Frame(fields)
    phone_string = tk.StringVar()
    phone_label = ttk.Label(master=phone_frame, text="phone number")
    phone_label.pack()
    phone_entry = ttk.Entry(master=phone_frame, textvariable=phone_string)
    phone_entry.pack()
    phone_frame.pack(side="left", padx=10)

    initials_frame = ttk.Frame(fields)
    initials_string = tk.StringVar()
    initials_label = ttk.Label(master=initials_frame, text="initials")
    initials_label.pack()
    initials_entry = ttk.Entry(master=initials_frame, textvariable=initials_string)
    initials_entry.pack()
    initials_frame.pack(side="left", padx=10)

    fields.pack(pady=10)

    users = Users(user_tab, user_picker, calendar)

    create_user_button = ttk.Button(
        master=user_tab,
        text="save new user",
        command=lambda: save_user(name_string, phone_string, initials_string, output_string, users),
    )
    create_user_button.pack(pady=10)

    output_string = tk.StringVar()
    output = ttk.Label(master=user_tab, textvariable=output_string)
    output.pack(pady=10)


    users.generate()

    return user_tab
