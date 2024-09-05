import tkinter as tk, util
from tkinter import ttk
from PIL import Image

def show(shortcut_type: str, path: str):
    global shortcut_icon, shortcut_icon_index

    shortcut_icon = ""
    shortcut_icon_index = 0

    window = tk.Toplevel()
    window.title("Edit shortcut")
    window.resizable(False, False)
    window.iconbitmap(util.internal + "icon.ico")
    window.configure(padx = 16, pady = 16)

    use_folder_icon = tk.BooleanVar(value = True)

    shortcut_info = ttk.Frame(window)
    shortcut_info.pack()

    icon = tk.Canvas(shortcut_info, width = 32, height = 32, bd = 0, highlightthickness = 0)
    icon.pack(side = "left")

    def update_icon(icon_path: str, icon_index: int = 0):
        global shortcut_icon, shortcut_icon_index, img2

        try:
            if icon_path.endswith(".ico") or icon_index == None: img = Image.open(icon_path)
            else: img = util.extract_icon(icon_path, icon_index)
        except: img = util.extract_icon(icon_path, icon_index)

        img.thumbnail((32, 32), Image.Resampling.LANCZOS)
        img.save(util.working_folder + "\\icon.png")

        img2 = tk.PhotoImage(file = util.working_folder + "\\icon.png")

        icon.delete("all")
        icon.create_image(0, 0, image = img2, anchor = "nw")

        shortcut_icon = icon_path
        shortcut_icon_index = icon_index

    name = ttk.Entry(shortcut_info, width = 40, font = ("Default", 10))
    name.pack(side = "left", padx = (16, 0))
    
    path_list = path.split("/")
    name.insert(0, path_list[len(path_list) - 1])

    def show_change_icon_btn():
        if use_folder_icon.get(): 
            change_icon_btn.forget()

            _icon = util.get_folder_icon(path)
            update_icon(_icon[0], _icon[1])
        else: 
            change_icon_btn.pack(side = "left")
            update_icon("C:/Windows/System32/shell32.dll", 4)

    if shortcut_type == "folder":
        ttk.Checkbutton(window, text = "Use folder's icon", variable = use_folder_icon, command = show_change_icon_btn).pack(pady = (8, 0), anchor = "w")

    buttons = ttk.Frame(window)
    buttons.pack(pady = (16, 0))

    def change_icon():
        shortcut_icon, shortcut_icon_index = util.pick_icon()
        update_icon(shortcut_icon, shortcut_icon_index)

    change_icon_btn = ttk.Button(window, text = "Change icon", width = "13", command = change_icon)
    change_icon_btn.pack(side = "left")

    def create_shortcut():
        shortcut_name = name.get()
        window.destroy()
        
        if shortcut_type == "folder": util.create_folder_shortcut(path, shortcut_name, shortcut_icon, shortcut_icon_index)
        else: util.create_file_shortcut(path, shortcut_name, shortcut_icon, shortcut_icon_index)

    ok_btn = ttk.Button(window, text = "OK", width = "13", default = "active", command = create_shortcut).pack(side = "right", padx = (8, 0))
    cancel_btn = ttk.Button(window, text = "Cancel", width = "13", command = window.destroy).pack(side = "right")

    if shortcut_type == "folder": show_change_icon_btn()
    else: update_icon("C:/Windows/System32/shell32.dll", 0)

    window.focus_set()
    window.bind("<Escape>", lambda event: window.destroy())