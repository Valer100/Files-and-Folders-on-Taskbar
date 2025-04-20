import ctypes, os
import os, appdirs, ctypes, yaml, sys

if getattr(sys, "frozen", False): 
    internal = "_internal\\"
    os.chdir(os.path.dirname(sys.executable))
else: 
    internal = ""
    os.chdir(os.path.dirname(sys.argv[0]))

if os.path.exists("preferences") and os.path.isdir("preferences"):
    user_preferences = os.path.abspath("preferences")
    is_portable = True
else:
    user_preferences = appdirs.user_config_dir(appname = "Files & Folder on Taskbar", appauthor = False, roaming = True)
    is_portable = False

working_folder = "C:\\Users\\Public\\Documents\\Files & Folders on Taskbar\\"
script_template = "WScript.CreateObject(\"WScript.Shell\").Run \"cmd /c (command)\", 0, True"
script_template_2 = "WScript.CreateObject(\"WScript.Shell\").Run \"(command)\", 0, True"
temp = user_preferences + "\\temp"

if not os.path.exists(user_preferences): os.mkdir(user_preferences)
if not os.path.exists(temp): os.mkdir(temp)

theme, language = "default", "default"

def save_settings():
    settings = {
        "theme": theme,
        "language": language,
    }

    settings_file = open(user_preferences + "\\settings.yaml", "w", encoding = "utf8")
    settings_file.write(yaml.safe_dump(data = settings, allow_unicode = True, sort_keys = False))
    settings_file.close()

def load_settings():
    global theme, language, additional_prefs

    settings_file = open(user_preferences + "\\settings.yaml", "r", encoding = "utf8")
    settings_yaml = settings_file.read()
    settings_file.close()
    settings = yaml.safe_load(settings_yaml)

    language = settings["language"]
    theme = settings["theme"]

try:
    load_settings()
except:
    save_settings()


ctypes.windll.shcore.SetProcessDpiAwareness(1)

dpi = ctypes.c_uint()
monitor_handle = ctypes.windll.user32.MonitorFromPoint(0, 0, 2)
ctypes.windll.shcore.GetDpiForMonitor(monitor_handle, 0, ctypes.byref(dpi), ctypes.byref(dpi))

scale_factor = dpi.value / 96

def get_scaled_value(value: int) -> int:
    return int(value * scale_factor + 0.5)


def sanitize_filename(name: str) -> str:
    illegal_characters = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]

    illegal_names = ["nul", "con", "prn", "aux", "com1", "com2", "com3", 
                     "com4", "com5", "com6", "com7", "com8", "com9", "lpt1",
                     "lpt2", "lpt3", "lpt4", "lpt5", "lpt6", "lpt7", "lpt8",
                     "lpt9"]
    
    for character in name:
        if character in illegal_characters: name = name.replace(character, "_")

    for illegal_name in illegal_names:
        if name == illegal_name: name = illegal_name + "_"

    return name