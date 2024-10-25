import tkinter as tk, util, strings, custom_ui
from tkinter import ttk

strings.load_language(open(util.user_preferences + "\\language", "r").read())

def show():
    window = custom_ui.Toplevel()
    window.title(strings.lang.pin_separator)
    window.resizable(False, False)
    window.iconbitmap(util.internal + "icon.ico")
    window.configure(padx = 14, pady = 8)

    separator_type = tk.StringVar(value = "vertical")

    ttk.Label(window, text = strings.lang.pin_separator, font = ("Segoe UI Semibold", 17)).pack(anchor = "w")
    ttk.Label(window, text = strings.lang.choose_a_separator_type).pack(anchor = "w", pady = 8)

    ttk.Radiobutton(window, text = strings.lang.vertical_line, variable = separator_type, value = "vertical").pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.lang.horizontal_line, variable = separator_type, value = "horizontal").pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.lang.transparent, variable = separator_type, value = "transparent").pack(anchor = "w")

    pin_separator_btn = ttk.Button(window, text = strings.lang.create_the_shortcut, default = "active", command = lambda: util.create_separator_shortcut(separator_type.get()))
    pin_separator_btn.pack(fill = "x", pady = (12, 4))

    window.focus_set()