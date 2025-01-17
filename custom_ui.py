import tkinter as tk, pywinstyles, winaccent, sys, hPyT, util, threading
from tkinter import ttk

entry_select = winaccent.accent_normal

def update_colors():
    global light_theme, bg, bg_hover, bg_press, fg, entry_focus, entry_bd, entry_bg, button_bg, button_hover, button_press, button_bd, button_bd_active, tooltip_bg, tooltip_bd, tooltip_fg, accent, accent_link
    light_theme = winaccent.apps_use_light_theme if util.theme == "default" else True if util.theme == "light" else False

    if light_theme:
        bg = "#f0f0f0"
        bg_hover = "#e0e0e0"
        bg_press = "#cecece"
        fg = "#000000"
        entry_focus = winaccent.accent_dark
        entry_bd = "#8d8d8d"
        entry_bg = "#ffffff"
        button_bg = "#ffffff"
        button_hover = "#ebebeb"
        button_press = "#dbdbdb"
        button_bd = "#d0d0d0"
        button_bd_active = winaccent.accent_dark
        tooltip_bg = "#ffffff"
        tooltip_bd = "#8f8f8f"
        tooltip_fg = "#505050"
        accent = winaccent.accent_dark
        accent_link = winaccent.accent_dark_2
    else:
        bg = "#202020"
        bg_hover = "#333333"
        bg_press = "#292929"
        fg = "#ffffff"
        entry_focus = "#ffffff"
        entry_bd = "#6e6e6e"
        entry_bg = "#404040"
        button_bg = "#333333"
        button_hover = "#454545"
        button_press = "#676767"
        button_bd = "#9b9b9b"
        button_bd_active = "#ffffff"
        tooltip_bg = "#2b2b2b"
        tooltip_bd = "#747474"
        tooltip_fg = "#ffffff"
        accent = winaccent.accent_light
        accent_link = winaccent.accent_light_3

update_colors()

class CommandLink(tk.Frame):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, padx = 8, pady = 8, background = bg, *args, **kwargs)

        ver = sys.getwindowsversion()

        if ver.major == 10 and ver.build >= 22000:
            self.arrow = ttk.Label(self, text = "\ue651  ", font = ("Segoe Fluent Icons", 11), padding = (0, 4, 0, 0), foreground = accent_link)
        else:
            self.arrow = ttk.Label(self, text = "\ue0ad  ", font = ("Segoe MDL2 Assets", 11), padding = (0, 4, 0, 0), foreground = accent_link)
        
        self.arrow.pack(side = "left", anchor = "w")

        self.text = ttk.Label(self, text = text, font = ("Segoe UI Semibold", 11), foreground = accent_link)
        self.text.pack(side = "left", anchor = "w")

        is_touched = False

        def on_enter(event):
            global is_touched
            is_touched = True

            self.configure(background = bg_hover)
            self.arrow.configure(background = bg_hover, foreground = accent_link)
            self.text.configure(background = bg_hover, foreground = accent_link)

        def on_leave(event):
            global is_touched
            is_touched = False

            self.configure(background = bg)
            self.arrow.configure(background = bg, foreground = accent_link)
            self.text.configure(background = bg, foreground = accent_link)

        def on_click(event):
            global is_touched
            is_touched = True

            self.configure(background = bg_press)
            self.arrow.configure(background = bg_press, foreground = accent)
            self.text.configure(background = bg_press, foreground = accent)

        def on_click_release(event):
            global is_touched

            self.configure(background = bg_hover)
            self.arrow.configure(background = bg_hover, foreground = accent_link)
            self.text.configure(background = bg_hover, foreground = accent_link)

            if not command is None and is_touched: command(); is_touched = False

        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)
        self.bind("<Button-1>", on_click)
        self.bind("<ButtonRelease-1>", on_click_release)

        self.arrow.bind("<Enter>", on_enter)
        self.arrow.bind("<Leave>", on_leave)
        self.arrow.bind("<Button-1>", on_click)
        self.arrow.bind("<ButtonRelease-1>", on_click_release)

        self.text.bind("<Enter>", on_enter)
        self.text.bind("<Leave>", on_leave)
        self.text.bind("<Button-1>", on_click)
        self.text.bind("<ButtonRelease-1>", on_click_release)

    def update_colors(self):
        self["background"] = bg
        self.arrow["background"] = bg
        self.text["background"] = bg

        self.arrow["foreground"] = accent_link
        self.text["foreground"] = accent_link

class Toolbutton(tk.Button):
    def __init__(self, master, text: str = "", command: callable = None, link: bool = False, icononly: bool = False, *args, **kwargs):
        super().__init__(master, text = text, command = command, padx = 2 if icononly else 4, pady = 2, background = bg, 
                         foreground = accent_link if link else fg, border = 0, relief = "solid", 
                         activebackground = bg_press, activeforeground = accent if link else fg,
                         cursor = "hand2" if link and not icononly else "", *args, **kwargs)

        self.link = link

        if icononly: self.configure(width = 2)

        self.bind("<Enter>", lambda event: self.configure(background = bg_hover))
        self.bind("<Leave>", lambda event: self.configure(background = bg))

    def update_colors(self):
        self.configure(background = bg, foreground = accent_link if self.link else fg, activebackground = bg_press, activeforeground = accent if self.link else fg)

class Button(tk.Button):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, text = text, command = command, padx = 4, pady = 3, background = button_bg, 
                         foreground = fg, border = 0, relief = "solid", activebackground = button_press, 
                         activeforeground = fg, highlightthickness = 1, highlightbackground = button_bd,
                         highlightcolor = button_bd, *args, **kwargs)

        if self["width"] == 0:
            if len(self["text"]) >= 10: self.configure(width = len(self["text"]))
            else: self.configure(width = 10)

        if self["default"] == "active": 
            self.configure(highlightbackground = button_bd_active, highlightcolor = button_bd_active)
            self.is_active = True
        else: 
            self.configure(default = "active")
            self.is_active = False

        self.bind("<Enter>", lambda event: self.configure(background = button_hover))
        self.bind("<Leave>", lambda event: self.configure(background = button_bg))

    def update_colors(self):
        self.configure(background = button_bg, foreground = fg, activebackground = button_press, 
                       activeforeground = fg, highlightbackground = button_bd_active if self.is_active else button_bd, 
                       highlightcolor = button_bd_active if self.is_active else button_bd)

class OptionMenu(tk.OptionMenu):
    def __init__(self, master, variable, value, *values):
        super().__init__(master, variable, value, *values)

        if light_theme: self.arrow = tk.PhotoImage(file = f"{util.internal}icons/dropdown_light.png")
        else: self.arrow = tk.PhotoImage(file = f"{util.internal}icons/dropdown_dark.png")

        self.configure(background = button_bg, foreground = fg, activebackground = button_hover, 
                       activeforeground = fg, highlightbackground = button_bd, highlightcolor = button_bd, 
                       image = self.arrow, compound = "right", indicatoron = False, border = 0, relief = "solid", 
                       highlightthickness = 1, pady = 4, padx = 7)
        
        self["menu"].configure(activebackground = winaccent.accent_normal)

    def update_colors(self):
        if light_theme: self.arrow = tk.PhotoImage(file = f"{util.internal}icons/dropdown_light.png")
        else: self.arrow = tk.PhotoImage(file = f"{util.internal}icons/dropdown_dark.png")

        self.configure(background = button_bg, foreground = fg, activebackground = button_hover, 
                       activeforeground = fg, highlightbackground = button_bd, highlightcolor = button_bd, 
                       image = self.arrow)

        self["menu"].configure(activebackground = winaccent.accent_normal)

ttk.Button = Button

class App(tk.Tk):
    def set_theme(self):
        pywinstyles.apply_style(self, "light" if light_theme else "dark")
        pywinstyles.change_header_color(self, bg)

        version = sys.getwindowsversion()
        
        if version.major == 10 and version.build < 22000:
            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)

        style = ttk.Style()
        style.configure(".", background = bg, foreground = fg)
        self.configure(background = bg)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.update()
        self.set_theme()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_theme()

        return value

class Toplevel(tk.Toplevel):
    def set_titlebar_theme(self):
        self.update()
        self.configure(background = bg)

        pywinstyles.apply_style(self, "light" if light_theme else "dark")
        pywinstyles.change_header_color(self, bg)

        version = sys.getwindowsversion()
        
        if version.major == 10 and version.build < 22000:
            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)

        hPyT.maximize_minimize_button.hide(self)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grab_set()
        self.focus_set()
        self.bind("<Escape>", lambda event: self.destroy())
        self.set_titlebar_theme()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_titlebar_theme()

        return value
    
def sync_colors(window):
    update_colors()

    if isinstance(window, App): window.set_theme()
    elif isinstance(window, Toplevel): window.set_titlebar_theme()

    for widget in window.winfo_children():
        if isinstance(widget, (CommandLink, Toolbutton, Button, OptionMenu)):
            widget.update_colors()
        elif isinstance(widget, tk.Entry):
            widget.configure(background = entry_bg, foreground = fg, highlightcolor = entry_bg, highlightbackground = entry_bg, insertbackground = fg, selectbackground = entry_select)
            widget.master.configure(highlightbackground = entry_bd, highlightcolor = entry_focus)
        elif isinstance(widget, tk.Canvas):
            widget.configure(background = bg)
        elif isinstance(widget, (Toplevel, ttk.Frame, tk.Frame)):
            sync_colors(widget)

def sync_colors_with_system(window): threading.Thread(target = lambda: winaccent.on_appearance_changed(lambda: sync_colors(window)), daemon = True).start()