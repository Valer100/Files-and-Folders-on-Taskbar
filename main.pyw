import tkinter as tk, shutil, custom_ui, tktooltip, strings
from tkinter import ttk, filedialog
from dialogs import separator_wizard, customize_shortcut, about, change_language, change_theme
from utils import preferences

window = custom_ui.App()
window.title("Files & Folders on Taskbar")
window.resizable(False, False)
window.configure(padx = preferences.get_scaled_value(14), pady = preferences.get_scaled_value(8))

shortcut_type = tk.StringVar(value = "file")

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
    def update_strings(widget):
        for child in widget.winfo_children():
            if isinstance(child, (custom_ui.App, custom_ui.Toplevel, tk.Frame, ttk.Frame, tktooltip.ToolTip)):
                update_strings(child)
            else:
                for variable in dir(old_language_module):
                    if isinstance(getattr(old_language_module, variable), str):
                        try:
                            if child["text"] == getattr(old_language_module, variable):
                                child["text"] = getattr(strings.lang, variable)
                            elif child["text"] in [" " + getattr(old_language_module, variable), "  " + getattr(old_language_module, variable)]:
                                child["text"] = child["text"].replace(getattr(old_language_module, variable), getattr(strings.lang, variable))
                        except:
                            pass

    old_language = preferences.language
    old_language_module = strings.lang

    change_language.show()
    window.wait_window(change_language.window)

    if old_language != preferences.language:             
        strings.load_language(preferences.language)
        update_strings(window)


def change_app_theme():
    old_theme = preferences.theme

    change_theme.show()
    window.wait_window(change_theme.window)

    if old_theme != preferences.theme:
        custom_ui.sync_colors(window)


def draw_ui():
    destroy_everything(window)
    strings.load_language(preferences.language)

    ttk.Label(window, text = "Files & Folders on Taskbar", font = ("Segoe UI Semibold", 17)).pack(anchor = "w")

    ttk.Label(window, text = strings.lang.pin_to_taskbar_a_shortcut_to).pack(anchor = "w", pady = (4, 8))

    custom_ui.CommandLink(window, title = strings.lang.a_file, description = strings.lang.file_desc, command = lambda: browse("file")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, title = strings.lang.a_folder, description = strings.lang.folder_desc, command = lambda: browse("folder")).pack(fill = "x", expand = True)
    custom_ui.CommandLink(window, title = strings.lang.a_separator, description = strings.lang.separator_desc, command = separator_wizard.show).pack(fill = "x", expand = True)

    settings = ttk.Frame(window, height = preferences.get_scaled_value(26))
    settings.pack(anchor = "w", pady = (preferences.get_scaled_value(20), preferences.get_scaled_value(2)), fill = "x")
    settings.pack_propagate(False)
    
    language = custom_ui.Toolbutton(settings, text = "\ue774", link = True, icononly = True, anchor = "n", command = change_app_language, font = ("Segoe UI", 12))
    language.pack(anchor = "nw", side = "left")

    theme = custom_ui.Toolbutton(settings, text = "\ue771", link = True, icononly = True, anchor = "n", command = change_app_theme, font = ("Segoe UI", 12))
    theme.pack(anchor = "nw", side = "left", padx = (preferences.get_scaled_value(4), 0))

    about_app = custom_ui.Toolbutton(settings, text = "\ue946", link = True, icononly = True, anchor = "n", command = about.show, font = ("Segoe UI", 13))
    about_app.pack(anchor = "nw", side = "left", padx = (preferences.get_scaled_value(4), 0))
    
    tktooltip.ToolTip(language, strings.lang.change_language, follow = False, delay = 1)
    tktooltip.ToolTip(theme, strings.lang.change_theme, follow = False, delay = 1)
    tktooltip.ToolTip(about_app, strings.lang.about_this_app, follow = False, delay = 1)

    window.update()


draw_ui()
custom_ui.sync_colors_with_system(window)
window.mainloop()