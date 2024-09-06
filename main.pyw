import tkinter as tk, subprocess, shutil, util, separator_wizard, customize_shortcut, open_source_licenses, change_language, strings, importlib
from tkinter import ttk, filedialog

window = tk.Tk()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.iconbitmap(util.internal + "icon.ico")
window.configure(padx = 14, pady = 8)

shortcut_type = tk.StringVar(value = "file")

subprocess.call(f"rmdir /q /s \"{util.working_folder}\\separators\"", shell = True)
shutil.copytree(util.internal + "separators", util.working_folder + "\\separators")

def browse():
    if shortcut_type.get() == "file":
        file = filedialog.askopenfile(title = strings.lang.choose_a_file, parent = window)

        if not file.name == "": customize_shortcut.show("file", file.name)
        else: return
    else:
        folder = filedialog.askdirectory(title = strings.lang.choose_a_folder, parent = window).replace("\"", "")

        if not folder == "": customize_shortcut.show("folder", folder)
        else: return

def destroy_everything(widget):
    for child in widget.winfo_children():
        if isinstance(child, (tk.Frame, ttk.Frame)): destroy_everything(child)
        else: child.destroy()

def change_app_language():
    change_language.show()
    window.wait_window(change_language.window)

    draw_ui()

def draw_ui():
    def file_selected(): pin_it_btn["text"] = strings.lang.choose_a_file_pin
    def folder_selected(): pin_it_btn["text"] = strings.lang.choose_a_folder_pin

    destroy_everything(window)
    strings.load_language(open(util.user_preferences + "\\language", "r").read())

    ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

    ttk.Label(window, text = strings.lang.pin_to_taskbar_a_shortcut_to).pack(anchor = "w", pady = (4, 8))
    ttk.Radiobutton(window, text = strings.lang.a_file, variable = shortcut_type, value = "file", command = file_selected).pack(anchor = "w")
    ttk.Radiobutton(window, text = strings.lang.a_folder, variable = shortcut_type, value = "folder", command = folder_selected).pack(anchor = "w")

    pin_it_btn = ttk.Button(window, text = strings.lang.choose_a_file_pin, default = "active", command = browse)
    pin_it_btn.pack(fill = "x", pady = (16, 0))

    if shortcut_type.get() == "folder": folder_selected()

    pin_separator_btn = ttk.Button(window, text = strings.lang.pin_separator, command = separator_wizard.show)
    pin_separator_btn.pack(fill = "x", pady = 4)

    style = ttk.Style()
    style.configure("Highlight.Toolbutton", foreground = "SystemHighlight")

    ttk.Label(window, text = strings.lang.settings, font = ("Segoe UI Semibold", 14)).pack(anchor = "w", pady = (16, 4))
    ttk.Button(window, text = strings.lang.change_language, style = "Highlight.Toolbutton", command = change_app_language).pack(anchor = "w")
    ttk.Button(window, text = strings.lang.see_open_source_licenses, style = "Highlight.Toolbutton", command = open_source_licenses.show).pack(anchor = "w")

    window.update()

draw_ui()
window.mainloop()