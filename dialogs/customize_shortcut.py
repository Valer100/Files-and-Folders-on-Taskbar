import tkinter as tk, strings, custom_ui
from tkinter import ttk, messagebox
from utils import shortcut, preferences, icon

def show(shortcut_type: str, path: str):
    global shortcut_icon, shortcut_icon_index

    shortcut_icon = ""
    shortcut_icon_index = 0

    window = custom_ui.Toplevel()
    window.title(strings.lang.customize_shortcut)
    window.configure(padx = preferences.get_scaled_value(16))

    use_folder_icon = tk.BooleanVar(value = True)

    shortcut_info = ttk.Frame(window)
    shortcut_info.pack(fill = "x", expand = True, pady = (preferences.get_scaled_value(16), 0))

    icon_canvas = tk.Canvas(
        shortcut_info, width = preferences.get_scaled_value(32), height = preferences.get_scaled_value(32), bd = 0, 
        highlightthickness = 0, background = custom_ui.colors.bg
    )
    icon_canvas.pack(side = "left")

    def update_icon(icon_path: str, icon_index: int = 0):
        global shortcut_icon, shortcut_icon_index, img

        icon.extract_icon(icon_path, icon_index)
        img = tk.PhotoImage(file = preferences.temp + "\\preview.png")

        icon_canvas.delete("all")
        icon_canvas.create_image(0, 0, image = img, anchor = "nw")

        shortcut_icon = icon_path
        shortcut_icon_index = icon_index

    name_rame = tk.Frame(shortcut_info, highlightbackground = custom_ui.colors.entry_bd, highlightcolor = custom_ui.colors.entry_focus,
                          highlightthickness = 1)
    name_rame.pack(anchor = "w", padx = (preferences.get_scaled_value(16), 0), side = "left")

    name = tk.Entry(name_rame, width = 50, background = custom_ui.colors.entry_bg, 
                    foreground = custom_ui.colors.fg, border = 0, highlightthickness = 2, 
                    highlightcolor = custom_ui.colors.entry_bg, highlightbackground = custom_ui.colors.entry_bg, 
                    insertbackground = custom_ui.colors.fg, insertwidth = 1, selectbackground = custom_ui.colors.entry_select,
                    selectforeground = "#FFFFFF")
    name.pack()
    
    path_list = path.split("/")
    name.insert(0, path_list[len(path_list) - 1])

    def show_change_icon_btn():
        if use_folder_icon.get(): 
            change_icon_btn.forget()

            _icon = preferences.get_folder_icon(path)
            update_icon(_icon[0], _icon[1])
        else: 
            change_icon_btn.pack(side = "left")
            update_icon("C:/Windows/System32/shell32.dll", 4)

    if shortcut_type == "folder":
        custom_ui.Checkbutton(window, text = strings.lang.use_folder_icon, variable = use_folder_icon, command = show_change_icon_btn).pack(pady = (preferences.get_scaled_value(8), 0), anchor = "w")

    buttons = ttk.Frame(window)
    buttons.pack(pady = preferences.get_scaled_value(16), fill = "x", expand = True)

    def change_icon():
        shortcut_icon, shortcut_icon_index = icon.pick_icon(window)
        update_icon(shortcut_icon, shortcut_icon_index)

    change_icon_btn = custom_ui.Button(buttons, text = strings.lang.change_icon, command = change_icon)
    change_icon_btn.pack(side = "left")

    def create_shortcut():
        shortcut_name = preferences.sanitize_filename(name.get())

        if name.get() != shortcut_name:
            messagebox.showwarning(parent = window, title = strings.lang.shortcut_name_invalid, message = strings.lang.shortcut_name_invalid_description)

        window.destroy()
        
        if shortcut_type == "folder": shortcut.create_folder_shortcut(path, shortcut_name, shortcut_icon, shortcut_icon_index)
        else: shortcut.create_file_shortcut(path, shortcut_name, shortcut_icon, shortcut_icon_index)

    custom_ui.Button(buttons, text = strings.lang.ok, default = "active", command = create_shortcut).pack(side = "right", padx = (preferences.get_scaled_value(8), 0))
    custom_ui.Button(buttons, text = strings.lang.cancel, command = window.destroy).pack(side = "right")

    if shortcut_type == "folder": show_change_icon_btn()
    else: update_icon("C:/Windows/System32/shell32.dll", 0)

    window.bind("<Escape>", lambda event: window.destroy())
    window.resizable(False, False)
    name.focus_set()