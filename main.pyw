import tkinter as tk, subprocess, shutil, util, separator_wizard, customize_shortcut, about, change_language, change_theme, strings, custom_ui, tktooltip
from tkinter import ttk, filedialog

window = custom_ui.App()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.iconbitmap(bitmap = util.internal + "icon.ico", default = util.internal + "icon.ico")
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
    old_language = util.language

    change_language.show()
    window.wait_window(change_language.window)

    if old_language != util.language: draw_ui()

def change_app_theme():
    old_theme = util.theme

    change_theme.show()
    window.wait_window(change_theme.window)

    if old_theme != util.theme:
        custom_ui.update_colors()
        window.set_theme()
        draw_ui()

def draw_ui():
    destroy_everything(window)
    strings.load_language(open(util.user_preferences + "\\language", "r").read())

    ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

    ttk.Label(window, text = strings.lang.pin_to_taskbar_a_shortcut_to).pack(anchor = "w", pady = (4, 8))

    custom_ui.CommandLink(window, title = strings.lang.a_file, description = strings.lang.file_desc, command = lambda: browse("file")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, title = strings.lang.a_folder, description = strings.lang.folder_desc, command = lambda: browse("folder")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, title = strings.lang.a_separator, description = strings.lang.separator_desc, command = separator_wizard.show).pack(fill = "x", expand = True)

    settings = ttk.Frame(window, height = 26)
    settings.pack(anchor = "w", pady = (20, 2), fill = "x")
    settings.pack_propagate(False)
    
    language = custom_ui.Toolbutton(settings, text = "\ue774", link = True, icononly = True, anchor = "n", command = change_app_language, font = ("Segoe UI", 12))
    language.pack(anchor = "nw", side = "left")

    theme = custom_ui.Toolbutton(settings, text = "\ue771", link = True, icononly = True, anchor = "n", command = change_app_theme, font = ("Segoe UI", 12))
    theme.pack(anchor = "nw", side = "left", padx = (4, 0))

    about_app = custom_ui.Toolbutton(settings, text = "\ue946", link = True, icononly = True, anchor = "n", command = about.show, font = ("Segoe UI", 13))
    about_app.pack(anchor = "nw", side = "left", padx = (4, 0))
    
    tktooltip.ToolTip(language, strings.lang.change_language, follow = True, delay = 1, bg = custom_ui.tooltip_bg, fg = custom_ui.tooltip_fg, parent_kwargs = {"bg":custom_ui.tooltip_bd, "padx": 1, "pady": 1})
    tktooltip.ToolTip(theme, strings.lang.change_theme, follow = True, delay = 1, bg = custom_ui.tooltip_bg, fg = custom_ui.tooltip_fg, parent_kwargs = {"bg":custom_ui.tooltip_bd, "padx": 1, "pady": 1})
    tktooltip.ToolTip(about_app, strings.lang.about_this_app, follow = True, delay = 1, bg = custom_ui.tooltip_bg, fg = custom_ui.tooltip_fg, parent_kwargs = {"bg":custom_ui.tooltip_bd, "padx": 1, "pady": 1})

    window.update()

draw_ui()
custom_ui.sync_colors_with_system(window)
window.mainloop()