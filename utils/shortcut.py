import random, win32com.client, ctypes, os, strings, shutil, charset_normalizer
import os, ctypes
from utils import preferences


def create_separator_shortcut(icon: str):
    delete_remnants()
    random_number = random.randint(1000000000, 9999999999)

    if not os.path.exists(preferences.working_folder + "\\shortcuts"):
        os.mkdir(preferences.working_folder + "\\shortcuts")
    
    open(preferences.working_folder + f"\\shortcuts\\separator_shortcut_{random_number}.vbs", "w", encoding = "utf8").write("")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{preferences.working_folder}\\shortcut\\Separator {random_number}.lnk")
    shortcut.TargetPath = f"C:\\Windows\\System32\\wscript.exe"
    shortcut.WorkingDirectory = preferences.working_folder + "\\separators"
    shortcut.Arguments = f"\"{preferences.working_folder}\\shortcuts\\separator_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = preferences.working_folder + "\\separators\\separator_" + icon + ".ico"
    shortcut.save()

    post_create_shortcut()


def create_file_shortcut(file_path, name: str, icon_path: str, icon_index: int = 0):
    delete_remnants()

    random_number = random.randint(1000000000, 9999999999)
    path_list = file_path.split("/")
    file_name = path_list[len(path_list) - 1]
    random_number_2 = str(random.randint(1000, 9999))

    if not os.path.exists(preferences.working_folder + "\\shortcuts"):
        os.mkdir(preferences.working_folder + "\\shortcuts")

    open(preferences.working_folder + f"\\shortcuts\\file_shortcut_{random_number}.bat", "w", encoding = "utf8").write(f"chcp 65001 > nul\ncd \"{(file_path + random_number_2).replace(file_name + random_number_2, '')}\"\n\"{file_path}\"")
    open(preferences.working_folder + f"\\shortcuts\\file_shortcut_{random_number}.vbs", "w", encoding = "utf8").write(preferences.script_template_2.replace("(command)", f"\"\"{preferences.working_folder}\\shortcuts\\file_shortcut_{random_number}.bat\"\""))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{preferences.working_folder}\\shortcut\\shortcut_{random_number}.lnk")
    shortcut.TargetPath = "C:\\Windows\\System32\\wscript.exe"
    shortcut.Arguments = f"\"{preferences.working_folder}\\shortcuts\\file_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = f"{icon_path},{icon_index}"
    shortcut.save()

    os.rename(f"{preferences.working_folder}\\shortcut\\shortcut_{random_number}.lnk", f"{preferences.working_folder}\\shortcut\\{name}.lnk")

    post_create_shortcut()


def create_folder_shortcut(folder_path: str, name: str, icon_path: str, icon_index: int = 0):
    delete_remnants()
    
    random_number = random.randint(1000000000, 9999999999)
    folder_path = folder_path.replace('/', '\\')

    if not os.path.exists(preferences.working_folder + "\\shortcuts"):
        os.mkdir(preferences.working_folder + "\\shortcuts")

    open(preferences.working_folder + f"\\shortcuts\\folder_shortcut_{random_number}.bat", "w", encoding = "utf8").write(f"chcp 65001 > nul\nexplorer \"{folder_path}\"")
    open(preferences.working_folder + f"\\shortcuts\\folder_shortcut_{random_number}.vbs", "w", encoding = "utf8").write(preferences.script_template_2.replace("(command)", f"\"\"{preferences.working_folder}\\shortcuts\\folder_shortcut_{random_number}.bat\"\""))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{preferences.working_folder}\\shortcut\\shortcut_{random_number}.lnk")
    shortcut.TargetPath = "C:\\Windows\\System32\\wscript.exe"
    shortcut.Arguments = f"\"{preferences.working_folder}\\shortcuts\\folder_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = f"{icon_path},{icon_index}"
    shortcut.save()

    os.rename(f"{preferences.working_folder}\\shortcut\\shortcut_{random_number}.lnk", f"{preferences.working_folder}\\shortcut\\{name}.lnk")

    post_create_shortcut()


def delete_remnants():
    if not os.path.exists(preferences.working_folder + "\\shortcut"):
        shutil.rmtree(preferences.working_folder + "\\shortcut")
        os.mkdir(preferences.working_folder + "\\shortcut")


def post_create_shortcut():
    os.startfile(preferences.working_folder + "shortcut")

    ctypes.windll.user32.MessageBoxW(
        None,
        strings.lang.shortcut_created_message,
        "Files & Folders on Taskbar", 
        0x40 | 0x40000
    )


def get_folder_icon(folder_path: str) -> str:
    folder_config = str(charset_normalizer.from_path(folder_path + "\\desktop.ini").best()).splitlines()
    print(folder_config)

    folder_icon = ("C:\\Windows\\System32\\shell32.dll", 4)

    for line in folder_config:
        if line.startswith("IconResource="):
            _folder_icon = line.replace("IconResource=", "")

            _folder_icon_path_list = _folder_icon.split(",")
            _folder_icon_path_list.reverse()
            _folder_icon_index = int(_folder_icon_path_list[0])

            _folder_icon = _folder_icon.lower().removesuffix("," + str(_folder_icon_index))

            folder_icon = (os.path.expandvars(_folder_icon), _folder_icon_index)
    
    return folder_icon