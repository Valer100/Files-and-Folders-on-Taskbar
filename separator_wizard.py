import tkinter as tk, util, strings, custom_ui, os
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

    separator_types = ttk.Frame(window)
    separator_types.pack(pady = 8)

    separator_vertical = tk.PhotoImage(file = util.internal + "separators/preview/separator_vertical.png")
    separator_horizontal = tk.PhotoImage(file = util.internal + "separators/preview/separator_horizontal.png")
    transparent = tk.PhotoImage(file = util.internal + "separators/preview/transparent.png")

    vertical = ttk.Button(separator_types, width = 100, image = separator_vertical, compound = "top",
                          text = strings.lang.vertical_line, command = lambda: util.create_separator_shortcut("vertical"))
    vertical.pack(side = "left")
    vertical.configure(pady = 8)

    horizontal = ttk.Button(separator_types, width = 100, image = separator_horizontal, compound = "top",
                            text = strings.lang.horizontal_line, command = lambda: util.create_separator_shortcut("horizontal"))
    horizontal.pack(side = "left", padx = (8, 0))
    horizontal.configure(pady = 8)

    transparent_b = ttk.Button(separator_types, width = 100, image = transparent, compound = "top",
                               text = strings.lang.transparent, command = lambda: util.create_separator_shortcut("transparent"))
    transparent_b.pack(side = "left", padx = (8, 0))
    transparent_b.configure(pady = 8)

    window.focus_set()
    window.mainloop()