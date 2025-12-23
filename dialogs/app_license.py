import tkinter as tk, strings, custom_ui
from tkinter import ttk
from utils import preferences

def show(window):
    window = custom_ui.Toplevel(master = window)
    window.title(strings.lang.license)
    window.configure(padx = preferences.get_scaled_value(16), pady = 0)

    header = ttk.Frame(window)
    header.pack(anchor = "w", pady = (preferences.get_scaled_value(8), preferences.get_scaled_value(16)))

    ttk.Label(header, text = "\ueb95 ", font = ("Segoe UI", 17), padding = (0, 5, 0, 0)).pack(side = "left")
    ttk.Label(header, width = 25, text = strings.lang.license, font = ("Segoe UI Semibold", 17)).pack(side = "left")

    license_text = custom_ui.ScrolledTextTtkScrollbar(window, width = 80, height = 22, wrap = "word", background = custom_ui.colors.entry_bg,
                                foreground = custom_ui.colors.fg, selectbackground = custom_ui.colors.entry_select,
                                selectforeground = "#ffffff", highlightthickness = 1, relief = "solid",
                                highlightbackground = custom_ui.colors.entry_bd, border = 0,
                                highlightcolor = custom_ui.colors.entry_bd, font = ("Consolas", 10))
    
    license_text.pack()
    license_text.insert("1.0", open(preferences.internal + "LICENSE").read())
    license_text.configure(state = "disabled")
    license_text.bind("<Button-3>", lambda event: custom_ui.show_readonly_text_context_menu(license_text))

    buttons = ttk.Frame(window)
    buttons.pack(pady = preferences.get_scaled_value(16), anchor = "e")

    custom_ui.Button(buttons, text = strings.lang.ok, default = "active", command = window.destroy).pack(side = "right")

    window.resizable(False, False)
    window.focus_set()