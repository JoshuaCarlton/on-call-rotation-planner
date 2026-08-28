import tkinter as tk
from tkinter import ttk

from create_calendar_tab import initialize_calendar_tab
from create_user_tab import initialize_users_tab
from update import update_phone_number


def main():
    window = tk.Tk()
    window.title("on call rotation planner")
    window.geometry("600x600")

    # notebook
    notebook = ttk.Notebook(window)

    # calendar
    calendar_tab, user_picker, calendar = initialize_calendar_tab(notebook)

    # user
    users_tab = initialize_users_tab(notebook, user_picker, calendar)

    notebook.add(calendar_tab, text="calendar")
    notebook.add(users_tab, text="users")
    notebook.pack()

    def on_closing():
        window.destroy()
        update_phone_number()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()


main()
