import tkinter as tk, getpass, random, win32com.client, subprocess
from tkinter import ttk, messagebox, filedialog

window = tk.Tk()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.configure(padx = 16, pady = 8)

shortcut_type = tk.StringVar(value = "file")
use_folder_icon = tk.BooleanVar(value = False)

def browse():
    if shortcut_type.get() == "file":
        file = filedialog.askopenfile(title = "Choose a file", parent = window)
        if not file.name == "": create_file_shortcut(file.name)
    else:
        folder = filedialog.askdirectory(title = "Choose a folder", parent = window).replace("\"", "")
        if not folder == "": create_folder_shortcut(folder)
            

def create_file_shortcut(file_path):
    path_list = file_path.split("/")
    file_name = path_list[len(path_list) - 1]
    random_number = str(random.randint(1000, 9999))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"C:\\Users\\{getpass.getuser()}\\Desktop\\{file_name}.lnk")
    shortcut.TargetPath = "C:\\Windows\\explorer.exe"
    shortcut.WorkingDirectory = (file_path + random_number).replace(file_name + random_number, "")
    shortcut.Arguments = f"\"{file_name}\""
    shortcut.save()

    messagebox.showinfo("Files & Folders on Taskbar", "The shortcut has been created on your Desktop. After customizing it, you can pin it on your taskbar.")

def create_folder_shortcut(folder_path):
    folder_icon = "C:\\Windows\\System32\\shell32.dll,4"  # Default folder icon
    folder_config = subprocess.getoutput(f"type \"{folder_path}\\desktop.ini\"").split("\n")

    for line in folder_config:
        if line.startswith("IconResource="):
            folder_icon = line.replace("IconResource=", "")

    path_list = folder_path.split("/")
    folder_name = path_list[len(path_list) - 1]
    random_number = str(random.randint(1000, 9999))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"C:\\Users\\{getpass.getuser()}\\Desktop\\{folder_name}.lnk")
    shortcut.TargetPath = "C:\\Windows\\explorer.exe"
    shortcut.WorkingDirectory = (folder_path + random_number).replace(folder_name + random_number, "")
    shortcut.Arguments = f"\"{folder_name}\""
    shortcut.IconLocation = folder_icon
    shortcut.save()

    messagebox.showinfo("Files & Folders on Taskbar", "The shortcut has been created on your Desktop. After customizing it, you can pin it on your taskbar.")

def file_selected():
    pin_it_btn["text"] = "Choose a file & pin it to taskbar"
    use_folder_icon_tick.forget()

def folder_selected():
    pin_it_btn["text"] = "Choose a folder & pin it to taskbar"
    use_folder_icon_tick.pack(fill = "x", pady = (8, 0))
    pin_it_btn.forget()
    pin_it_btn.pack(fill = "x", pady = (16, 4))

ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

ttk.Label(window, text = "Pin to taskbar a shortcut to:").pack(anchor = "w", pady = 8)
ttk.Radiobutton(window, text = "A file", variable = shortcut_type, value = "file", command = file_selected).pack(anchor = "w")
ttk.Radiobutton(window, text = "A folder", variable = shortcut_type, value = "folder", command = folder_selected).pack(anchor = "w")

use_folder_icon_tick = ttk.Checkbutton(window, text = "Use folder's icon", variable = use_folder_icon)

pin_it_btn = ttk.Button(window, text = "Choose a file & pin it to taskbar", default = "active", command = browse)
pin_it_btn.pack(fill = "x", pady = (16, 4))

window.mainloop()