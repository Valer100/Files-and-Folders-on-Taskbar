import tkinter as tk, pywinstyles, winaccent, sys
from tkinter import ttk

entry_select = winaccent.accent_normal

if winaccent.apps_use_light_theme:
    bg = "#f0f0f0"
    bg_hover = "#e0e0e0"
    bg_press = "#cecece"
    fg = "#000000"
    entry_focus = winaccent.accent_normal
    entry_bd = "#8d8d8d"
    entry_bg = "#ffffff"
    button_bg = "#ffffff"
    button_hover = "#ebebeb"
    button_press = "#dbdbdb"
    button_bd = "#d0d0d0"
    button_bd_active = winaccent.accent_normal
    accent = winaccent.accent_dark
    accent_link = winaccent.accent_dark_2
else:
    bg = "#202020"
    bg_hover = "#292929"
    bg_press = "#333333"
    fg = "#ffffff"
    entry_focus = "#ffffff"
    entry_bd = "#6e6e6e"
    entry_bg = "#404040"
    button_bg = "#333333"
    button_hover = "#454545"
    button_press = "#676767"
    button_bd = "#9b9b9b"
    button_bd_active = "#ffffff"
    accent = winaccent.accent_light
    accent_link = winaccent.accent_light_3

class CommandLink(tk.Frame):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, padx = 8, pady = 4, background = bg, *args, **kwargs)

        arrow = ttk.Label(self, text = "\ue651  ", font = ("Segoe UI", 11), padding = (0, 4, 0, 0), foreground = accent_link)
        arrow.pack(side = "left", anchor = "w")

        text = ttk.Label(self, text = text, font = ("Segoe UI Semibold", 11), foreground = accent_link)
        text.pack(side = "left", anchor = "w")

        def on_enter(event):
            self.configure(background = bg_hover)
            arrow.configure(background = bg_hover)
            text.configure(background = bg_hover)

        def on_leave(event):
            self.configure(background = bg)
            arrow.configure(background = bg)
            text.configure(background = bg)

        def on_click(event):
            self.configure(background = bg_press)
            arrow.configure(background = bg_press)
            text.configure(background = bg_press)

        def on_click_release(event):
            self.configure(background = bg_hover)
            arrow.configure(background = bg_hover)
            text.configure(background = bg_hover)

            if not command is None: command()

        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)
        self.bind("<Button-1>", on_click)
        self.bind("<ButtonRelease-1>", on_click_release)

        arrow.bind("<Enter>", on_enter)
        arrow.bind("<Leave>", on_leave)
        arrow.bind("<Button-1>", on_click)
        arrow.bind("<ButtonRelease-1>", on_click_release)

        text.bind("<Enter>", on_enter)
        text.bind("<Leave>", on_leave)
        text.bind("<Button-1>", on_click)
        text.bind("<ButtonRelease-1>", on_click_release)

class Toolbutton(tk.Button):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, text = text, command = command, padx = 8, pady = 2, background = bg, foreground = accent_link,
                         border = 0, relief = "solid", activebackground = bg_press, activeforeground = accent_link, *args, 
                         **kwargs)
        
        self.bind("<Enter>", lambda event: self.configure(background = bg_hover))
        self.bind("<Leave>", lambda event: self.configure(background = bg))

class Button(tk.Button):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, text = text, command = command, padx = 4, pady = 3, background = button_bg, 
                         foreground = fg, border = 0, relief = "solid", activebackground = button_press, 
                         activeforeground = fg, highlightthickness = 1, highlightbackground = button_bd,
                         highlightcolor = button_bd, *args, **kwargs)
        
        if len(self["text"]) >= 10: self.configure(width = len(self["text"]))
        else: self.configure(width = 10)

        if self["default"] == "active": self.configure(highlightbackground = button_bd_active, highlightcolor = button_bd_active)
        else: self.configure(default = "active")

        self.bind("<Enter>", lambda event: self.configure(background = button_hover))
        self.bind("<Leave>", lambda event: self.configure(background = button_bg))

ttk.Button = Button

class App(tk.Tk):
    def set_titlebar_theme(self):
        pywinstyles.apply_style(self, "dark" if winaccent.apps_use_light_theme == "dark" else "normal")
        pywinstyles.change_header_color(self, bg)

        version = sys.getwindowsversion()
        
        if version.major == 10 and version.build < 22000:
            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.update()

        style = ttk.Style()
        style.configure(".", background = bg, foreground = fg)
        style.configure("TButton", foreground = "#000000")
        style.configure("TEntry", foreground = "#000000")

        self.configure(background = bg)
        self.set_titlebar_theme()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_titlebar_theme()

        return value

class Toplevel(tk.Toplevel):
    def set_titlebar_theme(self):
        pywinstyles.apply_style(self, "dark" if winaccent.apps_use_light_theme == "dark" else "normal")
        pywinstyles.change_header_color(self, bg)

        version = sys.getwindowsversion()
        
        if version.major == 10 and version.build < 22000:
            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.update()
        self.configure(background = bg)
        self.set_titlebar_theme()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_titlebar_theme()

        return value