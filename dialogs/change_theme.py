import strings.en_US, strings.ro_RO
import tkinter as tk, strings, custom_ui
from tkinter import ttk
from utils import preferences

window = None

def show():
    global window
    window = custom_ui.Toplevel()
    window.title(strings.lang.change_theme)
    window.configure(padx = preferences.get_scaled_value(16), pady = 0)

    themes = ["default", "light", "dark"]
    theme = tk.StringVar(value = preferences.theme if preferences.theme in themes else "default")

    header = ttk.Frame(window)
    header.pack(anchor = "w", pady = (preferences.get_scaled_value(4), preferences.get_scaled_value(8)))

    ttk.Label(header, text = "\ue771 ", font = ("Segoe UI", 17), padding = (0, 5, 0, 0)).pack(side = "left")
    ttk.Label(header, text = strings.lang.change_theme + " ", font = ("Segoe UI Semibold", 17)).pack(side = "left")

    custom_ui.Radiobutton(window, text = strings.lang.lang_system_default, value = "default", variable = theme).pack(anchor = "w")
    custom_ui.Radiobutton(window, text = strings.lang.light_theme, value = "light", variable = theme).pack(anchor = "w")
    custom_ui.Radiobutton(window, text = strings.lang.dark_theme, value = "dark", variable = theme).pack(anchor = "w")

    buttons = ttk.Frame(window)
    buttons.pack(pady = preferences.get_scaled_value(16), fill = "x")

    def apply_theme():
        preferences.theme = theme.get()
        preferences.save_settings()
        window.destroy()

    buttons.grid_columnconfigure(index = [0, 1], weight = 1)

    custom_ui.Button(buttons, text = strings.lang.cancel, command = window.destroy).grid(row = 0, column = 0, padx = (0, preferences.get_scaled_value(4)), sticky = "ew")
    custom_ui.Button(buttons, text = strings.lang.ok, default = "active", command = apply_theme).grid(row = 0, column = 1, padx = (preferences.get_scaled_value(4), 0), sticky = "ew")

    window.resizable(False, False)
    window.focus_set()