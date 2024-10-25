import tkinter as tk, subprocess, shutil, util, separator_wizard, customize_shortcut, open_source_licenses, change_language, strings, custom_ui
from tkinter import ttk, filedialog

window = custom_ui.App()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.iconbitmap(util.internal + "icon.ico")
window.configure(padx = 14, pady = 8)

shortcut_type = tk.StringVar(value = "file")

subprocess.call(f"rmdir /q /s \"{util.working_folder}\\separators\"", shell = True)
shutil.copytree(util.internal + "separators", util.working_folder + "\\separators")

def browse(shortcut_type):
    if shortcut_type == "file":
        file = filedialog.askopenfile(title = strings.lang.choose_a_file, parent = window)

        if not file.name == "": customize_shortcut.show("file", file.name)
        else: return
    else:
        folder = filedialog.askdirectory(title = strings.lang.choose_a_folder, parent = window).replace("\"", "")

        if not folder == "": customize_shortcut.show("folder", folder)
        else: return

def destroy_everything(widget):
    for child in widget.winfo_children():
        child.destroy()

def change_app_language():
    change_language.show()
    window.wait_window(change_language.window)

    draw_ui()

def draw_ui():
    destroy_everything(window)
    strings.load_language(open(util.user_preferences + "\\language", "r").read())

    ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

    ttk.Label(window, text = strings.lang.pin_to_taskbar_a_shortcut_to).pack(anchor = "w", pady = (4, 8))

    custom_ui.CommandLink(window, text = strings.lang.a_file, command = lambda: browse("file")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, text = strings.lang.a_folder, command = lambda: browse("folder")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, text = strings.lang.a_separator, command = separator_wizard.show).pack(fill = "x", expand = True)

    ttk.Label(window, text = strings.lang.settings, font = ("Segoe UI Semibold", 14)).pack(anchor = "w", pady = (16, 4))
    custom_ui.Toolbutton(window, text = strings.lang.change_language, command = change_app_language).pack(anchor = "w")
    custom_ui.Toolbutton(window, text = strings.lang.see_open_source_licenses, command = open_source_licenses.show).pack(anchor = "w")

    window.update()

draw_ui()
window.mainloop()