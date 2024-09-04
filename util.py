import random, win32com.client, subprocess, ctypes, appdirs, os

if os.path.exists("icon.ico"): internal = ""
else: internal = "_internal\\"

working_folder = appdirs.user_data_dir("Files & Folders on Taskbar", False)

def pick_icon(default_icon = "C:\\Windows\\System32\\shell32.dll,0") -> str:
    delete_remnants()

    icon_file_buffer = ctypes.create_unicode_buffer(260)
    icon_index = ctypes.c_int(0)

    initial_icon_file = "C:\\Windows\\System32\\shell32.dll"
    ctypes.windll.kernel32.lstrcpyW(icon_file_buffer, initial_icon_file)

    result = ctypes.windll.shell32.PickIconDlg(None, icon_file_buffer, ctypes.sizeof(icon_file_buffer), ctypes.byref(icon_index))

    if result: return f"{icon_file_buffer.value},{icon_index.value}"
    else: return default_icon

def create_separator_shortcut(icon: str):
    delete_remnants()

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\Separator.lnk")
    shortcut.TargetPath = "C:\\Windows\\explorer.exe"
    shortcut.WorkingDirectory = working_folder + "\\separators"
    shortcut.Arguments = f"\"separator.vbs\""
    shortcut.IconLocation = working_folder + "\\separators\\separator_" + icon + ".ico"
    shortcut.save()

    post_create_shortcut()

def create_file_shortcut(file_path):
    delete_remnants()

    path_list = file_path.split("/")
    file_name = path_list[len(path_list) - 1]
    random_number = str(random.randint(1000, 9999))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\{file_name}.lnk")
    shortcut.TargetPath = "C:\\Windows\\explorer.exe"
    shortcut.WorkingDirectory = (file_path + random_number).replace(file_name + random_number, "")
    shortcut.Arguments = f"\"{file_name}\""
    shortcut.IconLocation = pick_icon()
    shortcut.save()

    post_create_shortcut()

def create_folder_shortcut(folder_path: str, use_folder_icon: bool):
    folder_icon = "C:\\Windows\\System32\\shell32.dll,4"  # Default folder icon
    folder_config = subprocess.getoutput(f"type \"{folder_path}\\desktop.ini\"").split("\n")

    if use_folder_icon:
        for line in folder_config:
            if line.startswith("IconResource="):
                folder_icon = line.replace("IconResource=", "")
    else: folder_icon = pick_icon("C:\\Windows\\System32\\shell32.dll,4")

    path_list = folder_path.split("/")
    folder_name = path_list[len(path_list) - 1]
    random_number = str(random.randint(1000, 9999))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\{folder_name}.lnk")
    shortcut.TargetPath = "C:\\Windows\\explorer.exe"
    shortcut.WorkingDirectory = (folder_path + random_number).replace(folder_name + random_number, "")
    shortcut.Arguments = f"\"{folder_name}\""
    shortcut.IconLocation = folder_icon
    shortcut.save()

    post_create_shortcut()

def delete_remnants():
    subprocess.call(f"rmdir /q /s \"{working_folder}\\shortcut\"", shell = True)
    subprocess.call(f"mkdir \"{working_folder}\\shortcut\"", shell = True)

def post_create_shortcut():
    subprocess.call(f"explorer \"{working_folder}\\shortcut\"", shell = True)

    ctypes.windll.user32.MessageBoxW(
        None,
        "The shortcut has been created.\n\nNow, a File Explorer window with the folder where was the shortcut created was opened. Drag the shortcut to your taskbar and then close the File Explorer window.\n\nYou have to do this extra step, because it's not that easy for 3rd party programs to pin a shortcut in the taskbar on Windows 10 and 11.", 
        "Files & Folders on Taskbar", 
        0x40 | 0x40000
    )