import tkinter as tk, subprocess, ctypes, appdirs, shutil, util
from tkinter import ttk, filedialog

window = tk.Tk()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.configure(padx = 14, pady = 8)

shortcut_type = tk.StringVar(value = "file")
use_folder_icon = tk.BooleanVar(value = False)

subprocess.call(f"rmdir /q /s \"{util.working_folder}\\separators\"", shell = True)
shutil.copytree("separators", util.working_folder + "\\separators")

def browse():
    subprocess.call(f"rmdir /q /s \"{util.working_folder}\\shortcut\"", shell = True)
    subprocess.call(f"mkdir \"{util.working_folder}\"", shell = True)

    if shortcut_type.get() == "file":
        file = filedialog.askopenfile(title = "Choose a file", parent = window)

        if not file.name == "": util.create_file_shortcut(file.name)
        else: return
    else:
        folder = filedialog.askdirectory(title = "Choose a folder", parent = window).replace("\"", "")

        if not folder == "": util.create_folder_shortcut(folder)
        else: return

    ctypes.windll.user32.MessageBoxW(
        0,
        "The shortcut has been created.\n\nNow, a File Explorer window with the folder where was the shortcut created was opened. Drag the shortcut to your taskbar and then close the File Explorer window.\n\nYou have to do this extra step, because it's not that easy for 3rd party programs to pin a shortcut in the taskbar on Windows 10 and 11.", 
        "Files & Folders on Taskbar", 
        0x40 | 0x40000
    )

def file_selected():
    pin_it_btn["text"] = "Choose a file & pin it to taskbar"
    use_folder_icon_tick.forget()

def folder_selected():
    pin_it_btn["text"] = "Choose a folder & pin it to taskbar"
    use_folder_icon_tick.pack(fill = "x", pady = (8, 0))

    pin_it_btn.forget()
    pin_separator_btn.forget()

    pin_it_btn.pack(fill = "x", pady = (16, 0))
    pin_separator_btn.pack(fill = "x", pady = (8, 4))

ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

ttk.Label(window, text = "Pin to taskbar a shortcut to:").pack(anchor = "w", pady = 8)
ttk.Radiobutton(window, text = "A file", variable = shortcut_type, value = "file", command = file_selected).pack(anchor = "w")
ttk.Radiobutton(window, text = "A folder", variable = shortcut_type, value = "folder", command = folder_selected).pack(anchor = "w")

use_folder_icon_tick = ttk.Checkbutton(window, text = "Use folder's icon", variable = use_folder_icon)

pin_it_btn = ttk.Button(window, text = "Choose a file & pin it to taskbar", default = "active", command = browse)
pin_it_btn.pack(fill = "x", pady = (16, 0))

pin_separator_btn = ttk.Button(window, text = "Add separator", command = browse)
pin_separator_btn.pack(fill = "x", pady = (8, 4))

window.mainloop()