import tkinter as tk, strings, custom_ui, webbrowser
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import strings._info
from utils import preferences
from dialogs import app_license

def show():
    global show_os_licenses, show_licenses
    show_os_licenses = False

    window = custom_ui.Toplevel()
    window.title(strings.lang.about_title)
    window.configure(padx = preferences.get_scaled_value(16), pady = 0)

    def show_hide_licenses():
        global arrow, show_os_licenses
        show_os_licenses = not show_os_licenses

        if show_os_licenses: licenses.pack(pady = preferences.get_scaled_value(16))
        else: licenses.forget()

        show_licenses.configure(image = custom_ui.icons.arrow_up if show_os_licenses else custom_ui.icons.arrow_down)

    app_info = ttk.Frame(window)
    app_info.pack(fill = "x")

    app_icon = tk.Canvas(app_info, width = preferences.get_scaled_value(63), height = preferences.get_scaled_value(40), highlightthickness = 0, background = custom_ui.colors.bg)
    app_icon.pack(side = "left", padx = (0, preferences.get_scaled_value(16)), pady = (preferences.get_scaled_value(16), 0))
    app_icon.create_image(preferences.get_scaled_value(63) // 2, preferences.get_scaled_value(40) // 2, image = custom_ui.icons.app_about, anchor = "center")

    app_name_and_version = ttk.Frame(app_info)
    app_name_and_version.pack(side = "left")

    ttk.Label(app_name_and_version, text = "Files and Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w", pady = (preferences.get_scaled_value(8), 0))
    ttk.Label(app_name_and_version, text = strings.lang.version + ((" " + strings.lang.last_commit) if strings._info.channel == "canary" else "")).pack(anchor = "w")
    
    if not strings.lang in [strings.en_US, strings.ro_RO]:
        ttk.Label(app_name_and_version, text = strings.lang.translation_made_by.replace("%a", strings.lang.author)).pack(anchor = "w")

    links = ttk.Frame(window)
    links.pack(fill = "x", pady = (preferences.get_scaled_value(16), 0))

    custom_ui.Toolbutton(links, text = "GitHub", link = True, command = lambda: webbrowser.open("https:\\\\github.com\\Valer100\\Volume-Labeler")).pack(side = "left")
    custom_ui.Toolbutton(links, text = strings.lang.issues, link = True, command = lambda: webbrowser.open("https:\\\\github.com\\Valer100\\Volume-Labeler\\issues")).pack(side = "left", padx = (4, 0))
    custom_ui.Toolbutton(links, text = strings.lang.latest_version, link = True, command = lambda: webbrowser.open("https:\\\\github.com\\Valer100\\Volume-Labeler\\releases\\latest")).pack(side = "left", padx = (4, 0))
    custom_ui.Toolbutton(links, text = strings.lang.license, link = True, command = lambda: app_license.show(window)).pack(side = "left", padx = (preferences.get_scaled_value(4), 0))

    buttons = ttk.Frame(window)
    buttons.pack(fill = "x", pady = preferences.get_scaled_value(16))

    show_licenses = custom_ui.Button(buttons, text = strings.lang.open_source_licenses, command = show_hide_licenses, compound = "left", image = custom_ui.icons.arrow_down)
    show_licenses.pack(anchor = "w", side = "left", fill = "y")
    show_licenses.configure(padx = preferences.get_scaled_value(5))

    custom_ui.Button(buttons, text = strings.lang.ok, command = window.destroy, default = "active").pack(side = "right")

    licenses = ScrolledText(window, width = 80, height = 20, wrap = "word", background = custom_ui.colors.entry_bg,
                                 foreground = custom_ui.colors.fg, selectbackground = custom_ui.colors.entry_select,
                                 selectforeground = "#ffffff", highlightthickness = 1, relief = "solid",
                                 highlightbackground = custom_ui.colors.entry_bd, 
                                 highlightcolor = custom_ui.colors.entry_bd, border = 0, font = ("Consolas", 10))

    licenses.insert("1.0", open(preferences.internal + "OPEN_SOURCE_LICENSES.txt", "r", encoding = "utf8").read())
    licenses.configure(state = "disabled")
    licenses.bind("<Button-3>", lambda event: custom_ui.show_readonly_text_context_menu(licenses))

    window.resizable(False, False)
    window.focus_set()