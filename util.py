import random, win32com.client, win32ui, win32gui, subprocess, ctypes, os
from PIL import Image

if os.path.exists("icon.ico"): internal = ""
else: internal = "_internal\\"

working_folder = "C:\\Users\\Public\\Documents\\Files & Folders on Taskbar\\"
script_template = "WScript.CreateObject(\"WScript.Shell\").Run \"cmd /c (command)\", 0, True"
script_template_2 = "WScript.CreateObject(\"WScript.Shell\").Run \"(command)\", 0, True"

def pick_icon() -> str:
    delete_remnants()

    icon_file_buffer = ctypes.create_unicode_buffer(260)
    icon_index = ctypes.c_int(0)

    initial_icon_file = "C:\\Windows\\System32\\shell32.dll"
    ctypes.windll.kernel32.lstrcpyW(icon_file_buffer, initial_icon_file)

    result = ctypes.windll.shell32.PickIconDlg(None, icon_file_buffer, ctypes.sizeof(icon_file_buffer), ctypes.byref(icon_index))
    if result: return (icon_file_buffer.value, icon_index.value)

def create_separator_shortcut(icon: str):
    delete_remnants()

    random_number = random.randint(1000000000, 9999999999)

    subprocess.call(f"md \"{working_folder}\\shortcuts\\", shell = True)
    open(working_folder + f"\\shortcuts\\separator_shortcut_{random_number}.vbs", "w", encoding = "utf8").write("")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\Separator {random_number}.lnk")
    shortcut.TargetPath = f"C:\\Windows\\System32\\wscript.exe"
    shortcut.WorkingDirectory = working_folder + "\\separators"
    shortcut.Arguments = f"\"{working_folder}\\shortcuts\\separator_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = working_folder + "\\separators\\separator_" + icon + ".ico"
    shortcut.save()

    post_create_shortcut()

def create_file_shortcut(file_path, name: str, icon_path: str, icon_index: int = 0):
    delete_remnants()

    random_number = random.randint(1000000000, 9999999999)
    path_list = file_path.split("/")
    file_name = path_list[len(path_list) - 1]
    random_number_2 = str(random.randint(1000, 9999))

    subprocess.call(f"md \"{working_folder}\\shortcuts\\", shell = True)
    open(working_folder + f"\\shortcuts\\file_shortcut_{random_number}.bat", "w", encoding = "utf8").write(f"chcp 65001 > nul\n\"{file_path}\"")
    open(working_folder + f"\\shortcuts\\file_shortcut_{random_number}.vbs", "w", encoding = "utf8").write(script_template_2.replace("(command)", f"\"\"{working_folder}\\shortcuts\\file_shortcut_{random_number}.bat\"\""))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\shortcut_{random_number}.lnk")
    shortcut.TargetPath = "C:\\Windows\\System32\\wscript.exe"
    shortcut.WorkingDirectory = (file_path + random_number_2).replace(file_name + random_number_2, "")
    shortcut.Arguments = f"\"{working_folder}\\shortcuts\\file_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = f"{icon_path},{icon_index}"
    shortcut.save()

    os.rename(f"{working_folder}\\shortcut\\shortcut_{random_number}.lnk", f"{working_folder}\\shortcut\\{name}.lnk")

    post_create_shortcut()

def create_folder_shortcut(folder_path: str, name: str, icon_path: str, icon_index: int = 0):
    delete_remnants()
    
    random_number = random.randint(1000000000, 9999999999)

    subprocess.call(f"md \"{working_folder}\\shortcuts\\", shell = True)
    open(working_folder + f"\\shortcuts\\folder_shortcut_{random_number}.bat", "w", encoding = "utf8").write(f"chcp 65001 > nul\nstart \"\" \"{folder_path}\"")
    open(working_folder + f"\\shortcuts\\folder_shortcut_{random_number}.vbs", "w", encoding = "utf8").write(script_template_2.replace("(command)", f"\"\"{working_folder}\\shortcuts\\folder_shortcut_{random_number}.bat\"\""))

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(f"{working_folder}\\shortcut\\shortcut_{random_number}.lnk")
    shortcut.TargetPath = "C:\\Windows\\System32\\wscript.exe"
    shortcut.Arguments = f"\"{working_folder}\\shortcuts\\folder_shortcut_{random_number}.vbs\""
    shortcut.IconLocation = f"{icon_path},{icon_index}"
    shortcut.save()

    os.rename(f"{working_folder}\\shortcut\\shortcut_{random_number}.lnk", f"{working_folder}\\shortcut\\{name}.lnk")

    post_create_shortcut()

def delete_remnants():
    subprocess.call(f"rmdir /q /s \"{working_folder}\\shortcut\"", shell = True)
    subprocess.call(f"mkdir \"{working_folder}\\shortcut\"", shell = True)

def post_create_shortcut():
    subprocess.call(f"explorer \"{working_folder}\\shortcut\"", shell = True)

    ctypes.windll.user32.MessageBoxW(
        None,
        "The shortcut has been created.\n\nNow, drag the shortcut from the folder that was opened to your taskbar and then close the File Explorer window.\n\nYou have to do this extra step, because it's not that easy for 3rd party programs to pin a shortcut to the taskbar on Windows 10 and 11.", 
        "Files & Folders on Taskbar", 
        0x40 | 0x40000
    )

def extract_icon(path: str, index: int = 0):
    # Modified from https://gist.github.com/chyyran/7314682

    large, small = win32gui.ExtractIconEx(path, index)
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))

    icon_bmp = win32ui.CreateBitmap()
    icon_bmp.CreateCompatibleBitmap(hdc, 32, 32)

    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(icon_bmp)
    hdc.DrawIcon((0,0), large[0])

    icon_info = icon_bmp.GetInfo()
    icon_buffer = icon_bmp.GetBitmapBits(True)
    icon = Image.frombuffer('RGBA', (icon_info['bmWidth'], icon_info['bmHeight']), icon_buffer, 'raw', 'BGRA', 0, 1)

    win32gui.DestroyIcon(small[0])
    return icon

def get_folder_icon(folder_path: str) -> str:
    folder_config = subprocess.getoutput(f"type \"{folder_path}\\desktop.ini\"").split("\n")
    folder_icon = ("C:\\Windows\\System32\\shell32.dll", 4)

    for line in folder_config:
        if line.startswith("IconResource="):
            _folder_icon = line.replace("IconResource=", "")

            _folder_icon_path_list = _folder_icon.split(",")
            _folder_icon_path_list.reverse()
            _folder_icon_index = int(_folder_icon_path_list[0])

            _folder_icon = _folder_icon.lower().replace("," + str(_folder_icon_index), "")

            folder_icon = (_folder_icon.replace("," + str(_folder_icon_index), ""), _folder_icon_index)
    
    return folder_icon