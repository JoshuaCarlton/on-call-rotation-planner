import tkinter as tk
from tkinter import ttk

from create_user_tab import new_create_user_tab


def main():
    window = tk.Tk()
    window.title("on call rotation planner")
    window.geometry("900x600")

    # notebook
    notebook = ttk.Notebook(window)

    # calendar
    calendar_tab = ttk.Frame(notebook)

    # users
    users_tab = ttk.Frame(notebook)

    # create user
    create_user_tab = new_create_user_tab(notebook)

    notebook.add(calendar_tab, text="calendar")
    notebook.add(users_tab, text="users")
    notebook.add(create_user_tab, text="create user")
    notebook.pack()

    window.mainloop()


main()
