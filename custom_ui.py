import tkinter as tk, pywinstyles, winaccent, sys, hPyT, threading, strings, warnings
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from utils import preferences, icon


is_windows_10 = sys.getwindowsversion().build < 22000 and sys.getwindowsversion().major == 10


class Colors():
    def update(self):
        self.light_theme = winaccent.apps_use_light_theme if preferences.theme == "default" else True if preferences.theme == "light" else False
        self.entry_select = winaccent.accent_normal
        
        if self.light_theme:
            self.bg = "#f0f0f0"
            self.bg_hover = "#e0e0e0"
            self.bg_press = "#cecece"
            self.bg_warning = "#fff4ce"
            self.bg_status_bar = "#e0e0e0"
            self.bd_status_bar = "#cacaca"
            self.fg = "#000000"
            self.fg_desc = "#404040"
            self.entry_focus = winaccent.accent_dark
            self.entry_bd = "#8d8d8d"
            self.entry_bg = "#ffffff"
            self.button_bg = "#ffffff"
            self.button_hover = "#ebebeb"
            self.button_press = "#dbdbdb"
            self.button_bd = "#d0d0d0"
            self.button_bd_active = winaccent.accent_dark
            self.tooltip_bg = "#ffffff"
            self.tooltip_bd = "#767676"
            self.tooltip_fg = "#575757"
            self.selection_bd = winaccent._utils.blend_colors(winaccent.accent_dark, self.bg, 70)
            self.selection = winaccent._utils.blend_colors(winaccent.accent_dark, self.bg, 20)
            self.selection_hover = winaccent._utils.blend_colors(winaccent.accent_dark, self.bg, 30)
            self.selection_press = winaccent._utils.blend_colors(winaccent.accent_dark, self.bg, 40)
            self.input_unchecked = "#404040"
            self.input_hover = "#808080"
            self.input_press = "#afafaf"
            self.scrollbar_arrow = "#606060"
            self.scrollbar_arrow_disabled = "#bfbfbf"
            self.scrollbar_thumb = "#cdcdcd"
            self.accent = winaccent.accent_dark
            self.accent_hover = winaccent._utils.blend_colors(self.accent, self.bg, 90)
            self.accent_press = winaccent._utils.blend_colors(self.accent, self.bg, 80)
            self.accent_link = winaccent.accent_dark_2

            if is_windows_10:
                self.button_bg = "#e1e1e1"
                self.button_hover = "#d0d0d0"
                self.button_press = "#c0c0c0"
                self.button_bd = "#adadad"
        else:
            self.bg = "#202020"
            self.bg_hover = "#333333"
            self.bg_press = "#292929"
            self.bg_warning = "#433519"
            self.bg_status_bar = "#1a1a1a"
            self.bd_status_bar = "#272727"
            self.fg = "#ffffff"
            self.fg_desc = "#a0a0a0"
            self.entry_focus = winaccent.accent_light_3
            self.entry_bd = "#6e6e6e"
            self.entry_bg = "#404040"
            self.button_bg = "#333333"
            self.button_hover = "#454545"
            self.button_press = "#676767"
            self.button_bd = "#9b9b9b"
            self.button_bd_active = winaccent.accent_light_3
            self.tooltip_bg = "#2b2b2b"
            self.tooltip_bd = "#747474"
            self.tooltip_fg = "#ffffff"
            self.selection_bd = winaccent._utils.blend_colors(winaccent.accent_light, self.bg, 40)
            self.selection = winaccent._utils.blend_colors(winaccent.accent_light, self.bg, 10)
            self.selection_hover = winaccent._utils.blend_colors(winaccent.accent_light, self.bg, 15)
            self.selection_press = winaccent._utils.blend_colors(winaccent.accent_light, self.bg, 20)
            self.input_unchecked = "#404040"
            self.input_hover = "#4f4f4f"
            self.input_press = "#5f5f5f"
            self.scrollbar_arrow = "#676767"
            self.scrollbar_arrow_disabled = "#404040"
            self.scrollbar_thumb = "#4d4d4d"
            self.accent = winaccent.accent_light
            self.accent_hover = winaccent._utils.blend_colors(self.accent, self.bg, 80)
            self.accent_press = winaccent._utils.blend_colors(self.accent, self.bg, 60)
            self.accent_link = winaccent.accent_light_3


class Icons():
    def initialize(self):
        self.app_about = tk.PhotoImage()
        self.arrow_up = tk.PhotoImage()
        self.arrow_down = tk.PhotoImage()

    def update(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message = "Image was not the expected size", category = UserWarning, module = "PIL")

            icon.extract_and_tint_icon(preferences.internal + "icons\\icon_about.ico", None, 50, icons.app_about)
            icon.extract_and_tint_icon(preferences.internal + "icons\\arrow_up.ico", colors.fg, 9, icons.arrow_up)
            icon.extract_and_tint_icon(preferences.internal + "icons\\arrow_down.ico", colors.fg, 9, icons.arrow_down)


colors = Colors()
icons = Icons()

colors.update()


class CommandLink(tk.Frame):
    def __init__(self, master, title: str = "", description: str = "", command: callable = None, *args, **kwargs):
        super().__init__(master, padx = 8, pady = 8, background = colors.bg, *args, **kwargs)

        ver = sys.getwindowsversion()

        if ver.major == 10 and ver.build >= 22000:
            self.arrow = ttk.Label(self, text = "\ue651  ", font = ("Segoe Fluent Icons", 13), padding = (0, 4, 0, 0), foreground = colors.accent_link)
        else:
            self.arrow = ttk.Label(self, text = "\ue0ad  ", font = ("Segoe MDL2 Assets", 13), padding = (0, 4, 0, 0), foreground = colors.accent_link)
        
        self.arrow.pack(side = "left", anchor = "w")

        self.text = tk.Frame(self, background = colors.bg)
        self.text.pack(fill = "x")

        self.title_w = ttk.Label(self.text, text = title, font = ("Segoe UI Semibold", 13), foreground = colors.accent_link)
        self.title_w.pack(anchor = "w", fill = "x")

        self.description_w = ttk.Label(self.text, text = description, foreground = colors.fg_desc)
        self.description_w.pack(anchor = "w", fill = "x")

        is_touched = False

        def on_enter(event):
            global is_touched
            is_touched = True

            self.configure(background = colors.bg_hover)
            self.arrow.configure(background = colors.bg_hover, foreground = colors.accent_link)
            self.title_w.configure(background = colors.bg_hover, foreground = colors.accent_link)
            self.description_w.configure(background = colors.bg_hover)
            self.text.configure(background = colors.bg_hover)

        def on_leave(event):
            global is_touched
            is_touched = False

            self.configure(background = colors.bg)
            self.arrow.configure(background = colors.bg, foreground = colors.accent_link)
            self.title_w.configure(background = colors.bg, foreground = colors.accent_link)
            self.description_w.configure(background = colors.bg)
            self.text.configure(background = colors.bg)

        def on_click(event):
            global is_touched
            is_touched = True

            self.configure(background = colors.bg_press)
            self.arrow.configure(background = colors.bg_press, foreground = colors.accent)
            self.title_w.configure(background = colors.bg_press, foreground = colors.accent)
            self.description_w.configure(background = colors.bg_press)
            self.text.configure(background = colors.bg_press)

        def on_click_release(event):
            global is_touched

            self.configure(background = colors.bg_hover)
            self.arrow.configure(background = colors.bg_hover, foreground = colors.accent_link)
            self.title_w.configure(background = colors.bg_hover, foreground = colors.accent_link)
            self.description_w.configure(background = colors.bg_hover)
            self.text.configure(background = colors.bg_hover)

            if not command is None and is_touched: command(); is_touched = False

        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)
        self.bind("<Button-1>", on_click)
        self.bind("<ButtonRelease-1>", on_click_release)

        self.arrow.bind("<Enter>", on_enter)
        self.arrow.bind("<Leave>", on_leave)
        self.arrow.bind("<Button-1>", on_click)
        self.arrow.bind("<ButtonRelease-1>", on_click_release)

        self.title_w.bind("<Enter>", on_enter)
        self.title_w.bind("<Leave>", on_leave)
        self.title_w.bind("<Button-1>", on_click)
        self.title_w.bind("<ButtonRelease-1>", on_click_release)

        self.description_w.bind("<Enter>", on_enter)
        self.description_w.bind("<Leave>", on_leave)
        self.description_w.bind("<Button-1>", on_click)
        self.description_w.bind("<ButtonRelease-1>", on_click_release)

    def update_colors(self):
        self["background"] = colors.bg
        self.arrow["background"] = colors.bg
        self.title_w["background"] = colors.bg
        self.text["background"] = colors.bg
        self.description_w["background"] = colors.bg

        self.arrow["foreground"] = colors.accent_link
        self.title_w["foreground"] = colors.accent_link
        self.description_w["foreground"] = colors.fg_desc


class Toolbutton(tk.Button):
    color_exceptions = (colors.selection, colors.selection_hover, colors.selection_press, colors.bg_hover, colors.bg_press)

    def __init__(self, master, text: str = "", command: callable = None, link: bool = False, icononly: bool = False, *args, **kwargs):
        super().__init__(
            master, text = text, command = command, padx = preferences.get_scaled_value(2) if icononly else 4, pady = 2, background = colors.bg, 
            foreground = colors.accent_link if link else colors.fg, border = 0, relief = "solid", 
            activebackground = colors.bg_press, activeforeground = colors.accent if link else colors.fg,
            cursor = "hand2" if link else "", highlightbackground = colors.selection_bd, 
            highlightcolor = colors.selection_bd, *args, **kwargs
        )

        self.link = link

        if icononly: self.configure(width = 2)

        if self["default"] == "active" and self["background"] not in self.color_exceptions:
            self.configure(background = colors.selection, activebackground = colors.selection_press)

        self.bind("<Enter>", lambda event: self.configure(background = colors.selection_hover if self["default"] == "active" else colors.bg_hover, activebackground = colors.selection_press if self["default"] == "active" else colors.bg_press))
        self.bind("<Leave>", lambda event: self.configure(background = colors.selection if self["default"] == "active" else colors.bg))

    def configure(self, *args, **kwargs):
        default_old = self["default"]
        super().configure(*args, **kwargs)

        if self["default"] == "active" and self["background"] not in self.color_exceptions:
            self.configure(background = colors.selection, activebackground = colors.selection_press)
        
        if self["default"] != default_old and self["default"] == "normal":
            self.configure(background = colors.bg, activebackground = colors.bg_press)


    def update_colors(self):
        self.color_exceptions = (colors.selection, colors.selection_hover, colors.selection_press, colors.bg_hover, colors.bg_press)
        
        self.configure(
            background = colors.bg, foreground = colors.accent_link if self.link else colors.fg, activebackground = colors.bg_press, 
            activeforeground = colors.accent if self.link else colors.fg, highlightbackground = colors.selection_bd, 
            highlightcolor = colors.selection_bd
        )
        
        if self["default"] == "active" and self["background"] not in self.color_exceptions:
            self.configure(background = colors.selection, activebackground = colors.selection_press)


class Button(tk.Button):
    def __init__(self, master, text: str = "", command: callable = None, *args, **kwargs):
        super().__init__(
            master, text = text, command = command, padx = 4, pady = 3, background = colors.button_bg, 
            foreground = colors.fg, border = 0, relief = "solid", activebackground = colors.button_press, 
            activeforeground = colors.fg, highlightthickness = 1, highlightbackground = colors.button_bd,
            highlightcolor = colors.button_bd, *args, **kwargs
        )

        if is_windows_10 and self["default"] == "active":
            self.configure(padx = 3, pady = 2, highlightthickness = 2)

        if self["width"] == 0:
            if len(self["text"]) >= 10: self.configure(padx = 10)
            else: self.configure(width = 10)

        if self["default"] == "active": 
            self.configure(highlightbackground = colors.button_bd_active, highlightcolor = colors.button_bd_active)
            self.is_active = True
        else: 
            self.configure(default = "active")
            self.is_active = False

        self.bind("<Enter>", lambda event: self.configure(background = colors.button_hover))
        self.bind("<Leave>", lambda event: self.configure(background = colors.button_bg))
    
    def enable(self, command: callable, active: bool = False):
        self.bind("<Enter>", lambda event: self.configure(background = colors.button_hover))
        self.bind("<Leave>", lambda event: self.configure(background = colors.button_bg))

        self.configure(
            command = command, background = colors.button_bg, activebackground = colors.button_press, 
            highlightbackground = colors.button_bd_active if active else colors.button_bd, 
            highlightcolor = colors.button_bd_active if active else colors.button_bd
        )
        
        self.is_active = active
        pywinstyles.set_opacity(self, 1)

    def disable(self):
        self.unbind("<Enter>")
        self.unbind("<Leave>")

        self.configure(
            command = lambda: None, background = colors.button_bg, activebackground = colors.button_bg, 
            highlightbackground = colors.button_bd, highlightcolor = colors.button_bd
        )
        
        self.is_active = False
        pywinstyles.set_opacity(self, 0.5)

    def update_colors(self):
        self.configure(
            background = colors.button_bg, foreground = colors.fg, activebackground = colors.button_press, 
            activeforeground = colors.fg, highlightbackground = colors.button_bd_active if self.is_active else colors.button_bd,
            highlightcolor = colors.button_bd_active if self.is_active else colors.button_bd
        )


class OptionMenu(tk.OptionMenu):
    def __init__(self, master, variable, value, *values):
        super().__init__(master, variable, value, *values)

        self.configure(
            background = colors.button_bg, foreground = colors.fg, activebackground = colors.button_hover, 
            activeforeground = colors.fg, highlightbackground = colors.button_bd, highlightcolor = colors.fg, 
            image = icons.arrow_down, compound = "right", indicatoron = False, border = 0, relief = "solid", 
            highlightthickness = 1, pady = preferences.get_scaled_value(5), padx = preferences.get_scaled_value(7), 
            takefocus = True
        )

        self["menu"].configure(activebackground = winaccent.accent_normal)

        def open_option_menu(event):
            self["menu"].post(self.winfo_rootx(), self.winfo_rooty() + self.winfo_height())
            return "break"
        
        self.bind("<space>", open_option_menu)

    def update_colors(self):
        self.configure(
            background = colors.button_bg, foreground = colors.fg, activebackground = colors.button_hover, 
            activeforeground = colors.fg, highlightbackground = colors.button_bd, highlightcolor = colors.fg, 
            image = icons.arrow_down
        )

        self["menu"].configure(activebackground = winaccent.accent_normal)


class Checkbutton(tk.Frame):
    touching = False

    def __init__(self, master, text: str = "", variable: tk.BooleanVar = None, command: callable = None):
        super().__init__(master, takefocus = True, background = colors.bg, highlightthickness = 1, highlightbackground = colors.bg, highlightcolor = colors.fg)

        self.variable = variable
        self.command = command

        self.checkbox = ttk.Frame(self)
        self.checkbox.pack(side = "left", pady = (preferences.get_scaled_value(2), 0))
        self.checkbox.pack_propagate(False)

        self.checkbox_glyph = tk.Label(
            self.checkbox, text = "\ue73d" if variable.get() else "\ue739", font = ("Segoe UI", 10), 
            background = colors.bg, foreground = colors.accent if variable.get() else colors.input_unchecked, 
            padx = 0, pady = 0
        )

        self.checkbox_glyph.pack(side = "left")
        self.checkbox_glyph.update()
        self.checkbox.configure(width = self.checkbox_glyph.winfo_reqwidth(), height = self.checkbox_glyph.winfo_reqwidth())

        self.text = ttk.Label(self, text = text, padding = (preferences.get_scaled_value(2), 0, 0, 0))
        self.text.pack(side = "left")

        self.bind("<Button-1>", lambda event: self.checkbox_glyph.configure(foreground = colors.accent_press if self.variable.get() else colors.input_press))
        self.checkbox.bind("<Button-1>", lambda event: self.checkbox_glyph.configure(foreground = colors.accent_press if self.variable.get() else colors.input_press))
        self.checkbox_glyph.bind("<Button-1>", lambda event: self.checkbox_glyph.configure(foreground = colors.accent_press if self.variable.get() else colors.input_press))
        self.text.bind("<Button-1>", lambda event: self.checkbox_glyph.configure(foreground = colors.accent_press if self.variable.get() else colors.input_press))

        self.bind("<ButtonRelease-1>", self.invoke)
        self.checkbox.bind("<ButtonRelease-1>", self.invoke)
        self.checkbox_glyph.bind("<ButtonRelease-1>", self.invoke)
        self.text.bind("<ButtonRelease-1>", self.invoke)

        def on_enter(event): 
            self.touching = True
            self.checkbox_glyph.configure(foreground = colors.accent_hover if self.variable.get() else colors.input_hover)

        def on_leave(event): 
            self.touching = False
            self.checkbox_glyph.configure(foreground = colors.accent if self.variable.get() else colors.input_unchecked)

        self.bind("<Enter>", on_enter)
        self.checkbox.bind("<Enter>", on_enter)
        self.checkbox_glyph.bind("<Enter>", on_enter)
        self.text.bind("<Enter>", on_enter)

        self.bind("<Leave>", on_leave)
        self.checkbox.bind("<Leave>", on_leave)
        self.checkbox_glyph.bind("<Leave>", on_leave)
        self.text.bind("<Leave>", on_leave)

        def invoke_with_keyboard(event):
            if self.focus_get():
                self.touching = True
                self.invoke(event)
                self.touching = False

        self.bind("<space>", invoke_with_keyboard)
        self.variable.trace_add("write", self.on_value_change)

    def __getitem__(self, key):
        if key == "text": return self.text["text"]
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if key == "text": self.text["text"] = value
        else: super().__setitem__(key, value)

    def invoke(self, event: tk.Event = None):
        if (event != None and self.touching) or event == None:
            self.variable.set(not self.variable.get())

        self.checkbox_glyph.configure(
            text = "\ue73d" if self.variable.get() else "\ue739", 
            foreground = colors.accent if self.variable.get() else colors.input_unchecked
        )

        if self.command != None: self.command()

    def on_value_change(self, var = None, index = None, mode = None):
        self.checkbox_glyph.configure(
            text = "\ue73d" if self.variable.get() else "\ue739", 
            foreground = colors.accent if self.variable.get() else colors.input_unchecked
        )

    def update_colors(self):
        self.configure(background = colors.bg, highlightbackground = colors.bg, highlightcolor = colors.fg)
        self.checkbox_glyph.configure(background = colors.bg, foreground = colors.accent if self.variable.get() else colors.input_unchecked)


class Radiobutton(tk.Frame):
    touching = False

    def __init__(self, master, text: str = "", variable = None, value = "", command: callable = None):
        super().__init__(master, takefocus = True, background = colors.bg, highlightthickness = 1, highlightbackground = colors.bg, highlightcolor = colors.fg)

        self.variable = variable
        self.value = value
        self.command = command

        self.radiobutton = ttk.Frame(self)
        self.radiobutton.pack(side = "left", pady = (preferences.get_scaled_value(2), 0))
        self.radiobutton.pack_propagate(False)

        self.radiobutton_glyph = tk.Label(
            self.radiobutton, text = "\ueccb" if variable.get() == self.value else "\uecca", font = ("Segoe UI", 10), 
            background = colors.bg, foreground = colors.accent if variable.get() == self.value else colors.input_unchecked, 
            padx = 0, pady = 0
        )

        self.radiobutton_glyph.pack(side = "left")
        self.radiobutton_glyph.update()
        self.radiobutton.configure(width = self.radiobutton_glyph.winfo_reqwidth(), height = self.radiobutton_glyph.winfo_reqwidth())

        self.text = ttk.Label(self, text = text, padding = (preferences.get_scaled_value(2), 0, 0, 0))
        self.text.pack(side = "left")

        self.bind("<Button-1>", lambda event: self.radiobutton_glyph.configure(foreground = colors.accent_press if self.variable.get() == self.value else colors.input_press))
        self.radiobutton.bind("<Button-1>", lambda event: self.radiobutton_glyph.configure(foreground = colors.accent_press if self.variable.get() == self.value else colors.input_press))
        self.radiobutton_glyph.bind("<Button-1>", lambda event: self.radiobutton_glyph.configure(foreground = colors.accent_press if self.variable.get() == self.value else colors.input_press))
        self.text.bind("<Button-1>", lambda event: self.radiobutton_glyph.configure(foreground = colors.accent_press if self.variable.get() == self.value else colors.input_press))

        self.bind("<ButtonRelease-1>", self.invoke)
        self.radiobutton.bind("<ButtonRelease-1>", self.invoke)
        self.radiobutton_glyph.bind("<ButtonRelease-1>", self.invoke)
        self.text.bind("<ButtonRelease-1>", self.invoke)

        def on_enter(event): 
            self.touching = True
            self.radiobutton_glyph.configure(foreground = colors.accent_hover if self.variable.get() == self.value else colors.input_hover)

        def on_leave(event): 
            self.touching = False
            self.radiobutton_glyph.configure(foreground = colors.accent if self.variable.get() == self.value else colors.input_unchecked)

        self.bind("<Enter>", on_enter)
        self.radiobutton.bind("<Enter>", on_enter)
        self.radiobutton_glyph.bind("<Enter>", on_enter)
        self.text.bind("<Enter>", on_enter)

        self.bind("<Leave>", on_leave)
        self.radiobutton.bind("<Leave>", on_leave)
        self.radiobutton_glyph.bind("<Leave>", on_leave)
        self.text.bind("<Leave>", on_leave)

        def invoke_with_keyboard(event):
            if self.focus_get():
                self.touching = True
                self.invoke(event)
                self.touching = False

        self.bind("<space>", invoke_with_keyboard)
        self.variable.trace_add("write", self.on_value_change)

    def __getitem__(self, key):
        if key == "text": return self.text["text"]
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if key == "text": self.text["text"] = value
        else: super().__setitem__(key, value)

    def invoke(self, event: tk.Event = None):
        if (event != None and self.touching) or event == None:
            self.variable.set(self.value)

        self.radiobutton_glyph.configure(
            text = "\ueccb" if self.variable.get() == self.value else "\uecca", 
            foreground = colors.accent if self.variable.get() == self.value else colors.input_unchecked
        )

        if self.command != None: self.command()

    def on_value_change(self, var = None, index = None, mode = None):
        self.radiobutton_glyph.configure(
            text = "\ueccb" if self.variable.get() == self.value else "\uecca", 
            foreground = colors.accent if self.variable.get() == self.value else colors.input_unchecked
        )

    def update_colors(self):
        self.configure(background = colors.bg, highlightbackground = colors.bg, highlightcolor = colors.fg)
        self.radiobutton_glyph.configure(background = colors.bg, foreground = colors.accent if self.variable.get() == self.value else colors.input_unchecked)


class Radiobutton2(tk.Frame):
    def __init__(self, master, variable: tk.StringVar, value: str, *args, **kwargs):
        self.variable = variable
        self.value = value

        super().__init__(master, highlightthickness = 1, highlightcolor = colors.fg, takefocus = True)
        self.bind("<space>", lambda event: self.radio.invoke())

        self.radio = tk.Radiobutton(
            self, variable = variable, value = value, background = colors.bg, foreground = colors.fg, 
            activebackground = colors.bg_press, activeforeground = colors.fg, indicatoron = False, 
            border = 0, relief = "solid", selectcolor = colors.selection, anchor = "w",
            takefocus = False, *args, **kwargs
        )

        self.radio.pack(anchor = "w", fill = "x")

        self.radio.bind("<Enter>", lambda event: self.configure(background = colors.bg_hover, selectcolor = colors.selection_hover if variable.get() == value else colors.bg_hover))
        self.radio.bind("<Leave>", lambda event: self.configure(background = colors.bg, selectcolor = colors.selection))

        def on_value_change(var = None, index = None, mode = None):
            try: 
                self.configure(background = colors.bg, selectcolor = colors.selection)
                self.config(highlightbackground = colors.selection_bd if self.variable.get() == self.value else colors.bg)
                self.radio.config(activebackground = colors.selection_press if self.variable.get() == self.value else colors.bg_press)
            except: 
                pass

        variable.trace_add("write", on_value_change)
        on_value_change()

    def configure(self, highlightcolor: str = None, highlightbackground: str = None, *args, **kwargs):
        return self.radio.configure(*args, **kwargs)

    def __getitem__(self, key):
        return self.radio.__getitem__(key)

    def __setitem__(self, key, value):
        self.radio.__setitem__(key, value)

    def update_colors(self):
        self.radio.configure(
            background = colors.bg, foreground = colors.fg, activeforeground = colors.fg, relief = "solid", selectcolor = colors.selection,
            activebackground = colors.selection_press if self.variable.get() == self.value else colors.bg_press
        )
        
        self.config(highlightcolor = colors.fg, highlightbackground = colors.selection_bd if self.variable.get() == self.value else colors.bg)
        self.radio.config()


class ScrolledTextTtkScrollbar(ScrolledText):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.vbar.destroy()
        self.vbar = ttk.Scrollbar(self.frame, command = self.yview)
        self.vbar.pack(side = "right", fill = "y")
        self.configure(yscrollcommand = self.vbar.set)


class App(tk.Tk):
    def set_theme(self):
        pywinstyles.apply_style(self, "light" if colors.light_theme else "dark")
        pywinstyles.change_header_color(self, winaccent.titlebar_active if winaccent.is_titlebar_colored and self.focus_get() else colors.bg)

        self.bind("<FocusIn>", lambda event: pywinstyles.change_header_color(self, winaccent.titlebar_active if winaccent.is_titlebar_colored else colors.bg))
        self.bind("<FocusOut>", lambda event: pywinstyles.change_header_color(self, colors.bg))

        style = ttk.Style()
        style.configure(".", background = colors.bg, foreground = colors.fg)
        style.configure("StatusBarBd.TFrame", background = colors.bd_status_bar)
        style.configure("StatusBar.TFrame", background = colors.bg_status_bar)
        style.configure("StatusBar.TLabel", background = colors.bg_status_bar, foreground = colors.fg)
        style.configure("Description.TLabel", foreground = colors.fg_desc)
        
        self.style.configure(
            "Vertical.TScrollbar", background = colors.bg, troughcolor = colors.bg, 
            bordercolor = colors.bg, relief = "solid", padding = (2, 3, 1, 2)
        )

        self.style.map(
            "Vertical.TScrollbar",
            arrowcolor = [("disabled", colors.scrollbar_arrow_disabled), ("", colors.scrollbar_arrow)],
            lightcolor = [("disabled", colors.bg), ("", colors.scrollbar_thumb)],
            darkcolor = [("disabled", colors.bg), ("", colors.scrollbar_thumb)],
            fieldbackground = [("disabled", colors.bg), ("", colors.scrollbar_thumb)],
        )

        self.configure(background = colors.bg)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.style = ttk.Style()
        self.style.element_create("Custom.Vertical.Scrollbar.trough", "from", "clam")
        self.style.element_create("Custom.Vertical.Scrollbar.uparrow", "from", "alt")
        self.style.element_create("Custom.Vertical.Scrollbar.downarrow", "from", "alt")
        self.style.element_create("Custom.Vertical.Scrollbar.thumb", "from", "clam", "field")

        self.style.layout("Vertical.TScrollbar", [("Button.padding", {"sticky": "ns", "children": [("Custom.Vertical.Scrollbar.trough", {"sticky": "ns", "children": [("Custom.Vertical.Scrollbar.uparrow", {"side": "top", "sticky": "nswe"}), ("Custom.Vertical.Scrollbar.downarrow", {"side": "bottom", "sticky": "nswe"}), ("Custom.Vertical.Scrollbar.thumb", {"expand": "1", "sticky": "nswe"})]})]})])

        self.iconbitmap(default = preferences.internal + "icons\\icon.ico")
        self.update()
        self.set_theme()

        icons.initialize()
        icons.update()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_theme()

        return value
    
    def mainloop(self, n = 0):
        self.deiconify()
        super().mainloop(n)


class Toplevel(tk.Toplevel):
    def set_titlebar_theme(self):
        self.update()
        self.configure(background = colors.bg)

        pywinstyles.apply_style(self, "light" if colors.light_theme else "dark")
        pywinstyles.change_header_color(self, winaccent.titlebar_active if winaccent.is_titlebar_colored and self.focus_get() else colors.bg)

        self.bind("<FocusIn>", lambda event: pywinstyles.change_header_color(self, winaccent.titlebar_active if winaccent.is_titlebar_colored else colors.bg))
        self.bind("<FocusOut>", lambda event: pywinstyles.change_header_color(self, colors.bg))

        hPyT.maximize_minimize_button.hide(self)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()
        self.master.unbind("<FocusIn>")

        self.transient(self.master)
        self.focus_set()
        self.geometry(f"+{self.master.winfo_x() + preferences.get_scaled_value(50)}+{self.master.winfo_y()+ preferences.get_scaled_value(50)}")
        
        self.after(100, lambda: self.master.wm_attributes("-disabled", True))
        self.after(100, lambda: self.master.bind("<FocusIn>", lambda event: pywinstyles.change_header_color(self.master, winaccent.titlebar_active if winaccent.is_titlebar_colored else colors.bg)))

        self.bind("<Escape>", lambda event: self.destroy())
        self.set_titlebar_theme()

    def resizable(self, width: bool = None, height: bool = None):
        value = super().resizable(width, height)
        self.set_titlebar_theme()
        self.deiconify()

        return value
    
    def destroy(self):
        self.master.wm_attributes("-disabled", False)
        super().destroy()


def sync_colors(window):
    colors.update()
    icons.update()

    def change_colors_recursively(parent):
        if isinstance(parent, App): parent.set_theme()
        elif isinstance(parent, Toplevel): parent.set_titlebar_theme()

        windows_version = sys.getwindowsversion()

        # A small hack for updating the title bar on Windows 10 (it doesn't update instantly like on Windows 11)
        if isinstance(parent, (App, Toplevel)) and windows_version.major == 10 and windows_version.build <= 22000:
            dummy_frame = tk.Frame(parent)
            dummy_frame.pack()
            parent.update_idletasks()
            dummy_frame.destroy()

        for widget in parent.winfo_children():
            if isinstance(widget, (CommandLink, Toolbutton, Button, OptionMenu, Checkbutton, Radiobutton, Radiobutton2)):
                widget.update_colors()
            elif isinstance(widget, tk.Entry):
                widget.configure(background = colors.entry_bg, foreground = colors.fg, highlightcolor = colors.entry_bg, highlightbackground = colors.entry_bg, insertbackground = colors.fg, selectbackground = colors.entry_select)
                widget.master.configure(highlightbackground = colors.entry_bd, highlightcolor = colors.entry_focus)
            elif isinstance(widget, tk.Text):
                widget.configure(background = colors.entry_bg, foreground = colors.fg, selectbackground = colors.entry_select, highlightbackground = colors.entry_bd, highlightcolor = colors.entry_bd)
            elif isinstance(widget, tk.Canvas):
                widget.configure(background = colors.bg)
            elif isinstance(widget, (Toplevel, ttk.Frame, tk.Frame)):
                change_colors_recursively(widget)

    change_colors_recursively(window)


def sync_colors_with_system(window): 
    threading.Thread(target = lambda: winaccent.on_appearance_changed(lambda: sync_colors(window)), daemon = True).start()


def show_entry_context_menu(entry: tk.Entry):
    entry.focus_set()

    try: entry.selection_get(); some_text_selected = "active"
    except: some_text_selected = "disabled"

    if entry.get() == "": 
        enable_select_all = "disabled"
    else:
        try:
            enable_select_all = "disabled" if entry.selection_get() == entry.get() else "active"
        except:
            enable_select_all = "active"

    try: entry.clipboard_get(); enable_paste = "active"
    except: enable_paste = "disabled"

    entry_menu = tk.Menu(tearoff = 0, activebackground = winaccent.accent_normal)
    entry_menu.add_command(label = strings.lang.cut, state = some_text_selected, command = lambda: entry.event_generate("<<Cut>>"))
    entry_menu.add_command(label = strings.lang.copy, state = some_text_selected, command = lambda: entry.event_generate("<<Copy>>"))
    entry_menu.add_command(label = strings.lang.paste, state = enable_paste, command = lambda: entry.event_generate("<<Paste>>"))
    entry_menu.add_command(label = strings.lang.delete, state = some_text_selected, command = lambda: entry.delete("sel.first", "sel.last"))
    entry_menu.add_separator()
    entry_menu.add_command(label = strings.lang.select_all, state = enable_select_all, command = lambda: entry.select_range(0, tk.END))

    entry_menu.tk_popup(entry.winfo_pointerx(), entry.winfo_pointery())


def show_readonly_text_context_menu(text: tk.Text | ScrolledText):
    text.focus_set()

    try: text.selection_get(); some_text_selected = "active"
    except: some_text_selected = "disabled"

    if text.get("1.0", "end") == "\n": 
        enable_select_all = "disabled"
    else:
        try:
            enable_select_all = "disabled" if text.selection_get() == text.get("1.0", "end") else "active"
        except:
            enable_select_all = "active"

    text_menu = tk.Menu(tearoff = 0, activebackground = winaccent.accent_normal)
    text_menu.add_command(label = strings.lang.copy, state = some_text_selected, command = lambda: text.event_generate("<<Copy>>"))
    text_menu.add_separator()
    text_menu.add_command(label = strings.lang.select_all, state = enable_select_all, command = lambda: text.tag_add("sel", "1.0", "end"))

    text_menu.tk_popup(text.winfo_pointerx(), text.winfo_pointery())


def set_window_loading_cursor(window: App | Toplevel):
    window.configure(cursor = "watch")
    window.update()
    window.update_idletasks()


def set_window_normal_cursor(window: App | Toplevel):
    window.configure(cursor = "arrow")
    window.update()
    window.update_idletasks()