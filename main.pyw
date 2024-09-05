import tkinter as tk, subprocess, shutil, util, separator_wizard, customize_shortcut, open_source_licenses
from tkinter import ttk, filedialog

window = tk.Tk()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.iconbitmap(util.internal + "icon.ico")
window.configure(padx = 14, pady = 8)

shortcut_type = tk.StringVar(value = "file")
use_folder_icon = tk.BooleanVar(value = False)

subprocess.call(f"rmdir /q /s \"{util.working_folder}\\separators\"", shell = True)
shutil.copytree(util.internal + "separators", util.working_folder + "\\separators")

def browse():
    if shortcut_type.get() == "file":
        file = filedialog.askopenfile(title = "Choose a file", parent = window)

        if not file.name == "": customize_shortcut.show("file", file.name)
        else: return
    else:
        folder = filedialog.askdirectory(title = "Choose a folder", parent = window).replace("\"", "")

        if not folder == "": customize_shortcut.show("folder", folder)
        else: return

def file_selected(): pin_it_btn["text"] = "Choose a file & pin it to taskbar"
def folder_selected(): pin_it_btn["text"] = "Choose a folder & pin it to taskbar"

ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")
ttk.Button(window, text = "See open source licenses", style = "Highlight.Toolbutton", command = open_source_licenses.show).pack(anchor = "w")

ttk.Label(window, text = "Pin to taskbar a shortcut to:").pack(anchor = "w", pady = 8)
ttk.Radiobutton(window, text = "A file", variable = shortcut_type, value = "file", command = file_selected).pack(anchor = "w")
ttk.Radiobutton(window, text = "A folder", variable = shortcut_type, value = "folder", command = folder_selected).pack(anchor = "w")

pin_it_btn = ttk.Button(window, text = "Choose a file & pin it to taskbar", default = "active", command = browse)
pin_it_btn.pack(fill = "x", pady = (16, 0))

pin_separator_btn = ttk.Button(window, text = "Pin separator", command = separator_wizard.show)
pin_separator_btn.pack(fill = "x", pady = 4)

style = ttk.Style()
style.configure("Highlight.Toolbutton", foreground = "SystemHighlight")


window.mainloop()