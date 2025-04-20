import tkinter as tk, strings, custom_ui
from utils import preferences, shortcut
from tkinter import ttk

def show():
    window = custom_ui.Toplevel()
    window.title(strings.lang.pin_separator)
    window.configure(padx = preferences.get_scaled_value(14), pady = preferences.get_scaled_value(8))

    separator_type = tk.StringVar(value = "vertical")

    ttk.Label(window, text = strings.lang.pin_separator, font = ("Segoe UI Semibold", 17)).pack(anchor = "w")
    ttk.Label(window, text = strings.lang.choose_a_separator_type).pack(anchor = "w", pady = preferences.get_scaled_value(8))

    separator_types = ttk.Frame(window)
    separator_types.pack(pady = preferences.get_scaled_value(8))

    separator_vertical = tk.PhotoImage(file = preferences.internal + "separators/preview/separator_vertical.png")
    separator_horizontal = tk.PhotoImage(file = preferences.internal + "separators/preview/separator_horizontal.png")
    transparent = tk.PhotoImage(file = preferences.internal + "separators/preview/transparent.png")

    def create_vertical_separator_shortcut(): window.destroy(); shortcut.create_separator_shortcut("vertical")
    def create_horizontal_separator_shortcut(): window.destroy(); shortcut.create_separator_shortcut("horizontal")
    def create_transparent_separator_shortcut(): window.destroy(); shortcut.create_separator_shortcut("transparent")

    vertical = custom_ui.Button(separator_types, width = preferences.get_scaled_value(100), image = separator_vertical, compound = "top",
                          text = strings.lang.vertical_line, command = create_vertical_separator_shortcut)
    vertical.pack(side = "left")
    vertical.image = separator_vertical
    vertical.configure(pady = preferences.get_scaled_value(8))

    horizontal = custom_ui.Button(separator_types, width = preferences.get_scaled_value(100), image = separator_horizontal, compound = "top",
                            text = strings.lang.horizontal_line, command = create_horizontal_separator_shortcut)
    horizontal.pack(side = "left", padx = (preferences.get_scaled_value(8), 0))
    horizontal.image = separator_horizontal
    horizontal.configure(pady = preferences.get_scaled_value(8))

    transparent_b = custom_ui.Button(separator_types, width = preferences.get_scaled_value(100), image = transparent, compound = "top",
                               text = strings.lang.transparent, command = create_transparent_separator_shortcut)
    transparent_b.pack(side = "left", padx = (preferences.get_scaled_value(8), 0))
    transparent_b.image = transparent
    transparent_b.configure(pady = preferences.get_scaled_value(8))

    window.focus_set()
    window.resizable(False, False)