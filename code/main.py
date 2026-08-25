import tkinter as tk
from tkinter import ttk

from create_user_tab import initialize_users_tab


def main():
    window = tk.Tk()
    window.title("on call rotation planner")
    window.geometry("900x600")

    # notebook
    notebook = ttk.Notebook(window)

    # calendar
    calendar_tab = ttk.Frame(notebook)

    # user
    users_tab = initialize_users_tab(notebook)

    notebook.add(calendar_tab, text="calendar")
    notebook.add(users_tab, text="users")
    notebook.pack()

    window.mainloop()


main()
