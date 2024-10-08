import strings.en_US
import strings.ro_RO
import tkinter as tk, util, strings
from tkinter import ttk

strings.load_language(open(util.user_preferences + "\\language", "r").read())
window = None

def show():
    global window

    window = tk.Toplevel()
    window.title(strings.lang.change_language)
    window.resizable(False, False)
    window.iconbitmap(util.internal + "icon.ico")
    window.configure(padx = 16, pady = 0)

    language = tk.StringVar(value = open(util.user_preferences + "\\language", "r").read())

    ttk.Label(window, text = strings.lang.change_language, font = ("Segoe UI Semibold", 17)).pack(anchor = "w", pady = 8, padx = (0, 128))

    ttk.Radiobutton(window, text = strings.lang.lang_system_default, value = "default", variable = language).pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.en_US.language, value = "en_US", variable = language).pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.ro_RO.language, value = "ro_RO", variable = language).pack(anchor = "w")

    buttons = ttk.Frame(window)
    buttons.pack(pady = (16, 10), anchor = "e")

    def apply_language():
        open(util.user_preferences + "\\language", "w").write(language.get())
        window.destroy()

    ok_btn = ttk.Button(buttons, text = strings.lang.ok, default = "active", command = apply_language).pack(side = "right", padx = (8, 0))
    cancel_btn = ttk.Button(buttons, text = strings.lang.cancel, command = window.destroy).pack(side = "right")

    window.focus_set()