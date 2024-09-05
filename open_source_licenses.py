import tkinter as tk, util
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def show():
    window = tk.Toplevel()
    window.title("Open source licenses")
    window.resizable(False, False)
    window.iconbitmap(util.internal + "icon.ico")
    window.configure(padx = 16, pady = 0)

    ttk.Label(window, text = "Open source licenses", font = ("Segoe UI Semibold", 17)).pack(anchor = "w", pady = (8, 16))

    licenses_text = ScrolledText(window, width = "90", height = 30, wrap = "word")
    licenses_text.pack(pady = (0, 16))

    licenses_text.insert("1.0", open(util.internal + "OPEN_SOURCE_LICENSES.txt", "r", encoding = "utf8").read())
    licenses_text.configure(state = "disabled")

    window.focus_set()