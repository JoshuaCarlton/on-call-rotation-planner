import tkinter as tk
from tkinter import ttk

from my_calendar import my_calendar


def initialize_calendar_tab(parrent):
    calendar_tab = ttk.Frame(master=parrent)
    calendar = my_calendar(calendar_tab)
    calendar.generate()
    calendar_tab.pack()
    return calendar_tab
