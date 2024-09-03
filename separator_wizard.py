import tkinter as tk, util
from tkinter import ttk

def show():
    window = tk.Toplevel()
    window.title("Pin separator")
    window.resizable(False, False)
    window.iconbitmap("icon.ico")
    window.configure(padx = 14, pady = 8)

    separator_type = tk.StringVar(value = "vertical")

    ttk.Label(window, text = "Pin separator", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")
    ttk.Label(window, text = "Choose a separator type:").pack(anchor = "w", pady = 8)

    ttk.Radiobutton(window, text = "Vertical line (great for horizontal taskbars)", variable = separator_type, value = "vertical").pack(anchor = "w")
    ttk.Radiobutton(window, text = "Horizontal line (great for vertical taskbars)", variable = separator_type, value = "horizontal").pack(anchor = "w")
    ttk.Radiobutton(window, text = "Transparent", variable = separator_type, value = "transparent").pack(anchor = "w")

    pin_separator_btn = ttk.Button(window, text = "Create the shortcut", default = "active", command = lambda: util.create_separator_shortcut(separator_type.get()))
    pin_separator_btn.pack(fill = "x", pady = (8, 4))

    window.focus_set()