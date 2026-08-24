from tkinter import ttk


def new_create_user_tab(parrent: ttk.Notebook)-> ttk.Frame:
    create_user_tab = ttk.Frame(parrent)
    fields = ttk.Frame(create_user_tab)

    name_frame = ttk.Frame(fields)
    name_label = ttk.Label(master = name_frame, text = "name")
    name_label.pack()
    name_entry = ttk.Entry(master = name_frame)
    name_entry.pack()
    name_frame.pack(side = "left", padx = 10)

    phone_frame = ttk.Frame(fields)
    phone_label = ttk.Label(master = phone_frame, text = "phone number")
    phone_label.pack()
    phone_entry = ttk.Entry(master = phone_frame)
    phone_entry.pack()
    phone_frame.pack(side = "left", padx = 10)

    initials_frame = ttk.Frame(fields)
    initials_label = ttk.Label(master = initials_frame, text = "initials")
    initials_label.pack()
    initials_entry = ttk.Entry(master = initials_frame)
    initials_entry.pack()
    initials_frame.pack(side = "left", padx = 10)

    fields.pack(pady = 20)

    create_user_button = ttk.Button(master = create_user_tab, text = "save new user")
    create_user_button.pack(pady = 10)

    return create_user_tab
