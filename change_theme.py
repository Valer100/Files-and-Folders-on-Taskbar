import strings.en_US, strings.ro_RO
import tkinter as tk, util, strings, custom_ui
from tkinter import ttk

strings.load_language(open(util.user_preferences + "\\language", "r").read())
window = None

def show():
    global window

    window = custom_ui.Toplevel()
    window.title(strings.lang.change_theme)
    window.resizable(False, False)
    window.configure(padx = 16, pady = 0)

    theme = tk.StringVar(value = util.theme)

    ttk.Label(window, width = 25, text = strings.lang.change_theme, font = ("Segoe UI Semibold", 17)).pack(anchor = "w", pady = 8)

    ttk.Radiobutton(window, text = strings.lang.lang_system_default, value = "default", variable = theme).pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.lang.light_theme, value = "light", variable = theme).pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.lang.dark_theme, value = "dark", variable = theme).pack(anchor = "w")

    buttons = ttk.Frame(window)
    buttons.pack(pady = 16, anchor = "e")

    def apply_theme():
        open(util.user_preferences + "\\theme", "w").write(theme.get())
        util.theme = theme.get()
        window.destroy()

    ok_btn = ttk.Button(buttons, text = strings.lang.ok, default = "active", command = apply_theme).pack(side = "right", padx = (8, 0))
    cancel_btn = ttk.Button(buttons, text = strings.lang.cancel, command = window.destroy).pack(side = "right")

    window.focus_set()