import ctypes, shutil, os
from io import BytesIO
from PIL import Image, IcoImagePlugin
from icoextract import IconExtractor
from utils import preferences


def pick_icon(window, initial_icon_file_path: str = "C:\\Windows\\System32\\shell32.dll") -> tuple[str, int]:
    icon_file_buffer = ctypes.create_unicode_buffer(260)
    icon_index = ctypes.c_int(0)

    ctypes.windll.kernel32.lstrcpyW(icon_file_buffer, initial_icon_file_path)

    result = ctypes.windll.shell32.PickIconDlg(ctypes.windll.user32.GetParent(window.winfo_id()), icon_file_buffer, ctypes.sizeof(icon_file_buffer), ctypes.byref(icon_index))
    if result: return (os.path.expandvars(icon_file_buffer.value), icon_index.value)


def extract_icon(path: str, index: int) -> None:
    if not path.endswith(".ico"):
        try:
            extractor = IconExtractor(path)
            extractor.export_icon(preferences.temp + "\\icon.ico", index)
        except:
            extractor = IconExtractor(path.lower().replace("system32", "systemresources") + ".mun")
            extractor.export_icon(preferences.temp + "\\icon.ico", index)
    else:
        shutil.copyfile(path, preferences.temp + "\\icon.ico")

    img = IcoImagePlugin.IcoImageFile(preferences.temp + "\\icon.ico")

    closest_size = min(
        img.info["sizes"],
        key = lambda size: (size[0] - int(32 * preferences.scale_factor)) ** 2 + (size[1] - int(32 * preferences.scale_factor)) ** 2
    )

    frames = []

    for index, header in enumerate(img.ico.entry):
        if header.width == closest_size[0] and header.height == closest_size[1]:
            frames.append((index, header, img.ico.frame(index)))

    frames.sort(key = lambda frame_info: frame_info[1].bpp, reverse = True)
    img = frames[0][2]

    img = img.resize((int(32 * preferences.scale_factor), int(32 * preferences.scale_factor)), Image.Resampling.LANCZOS)
    img.save(preferences.temp + "\\preview.png")
    img.close()


def convert_image_to_icon(path: str) -> None:
    img = Image.open(path).convert("RGBA")

    max_side = max(img.size)
    new_img = Image.new("RGBA", (max_side, max_side), (0, 0, 0, 0))

    new_img.paste(img, ((max_side - img.width) // 2, (max_side - img.height) // 2), img)
    img.close()

    new_img.save(fp = preferences.temp + "\\icon.ico", format = "ICO", sizes = [(16, 16), (20, 20), (24, 24), (30, 30), (32, 32), (48, 48), (64, 64), (72, 72), (96, 96), (128, 128), (144, 144), (196, 196), (256, 256)])
    new_img = new_img.resize((int(32 * preferences.scale_factor), int(32 * preferences.scale_factor)), Image.Resampling.LANCZOS)
    new_img.save(preferences.temp + "\\preview.png")
    new_img.close()


def extract_and_tint_icon(image_path, color, width, photoimage):
    img = IcoImagePlugin.IcoImageFile(image_path)

    closest_size = min(
        img.info["sizes"],
        key = lambda size: (size[0] - int(width * preferences.scale_factor)) ** 2 + (size[1] - int(width * preferences.scale_factor)) ** 2
    )

    img.size = closest_size
    img = img.resize((int(width * preferences.scale_factor), int(width * preferences.scale_factor)), Image.Resampling.LANCZOS)
    img = img.convert("RGBA")
    pixels = img.load()

    if not color == None:
        color = color.lstrip("#")
        rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

        for y in range(img.height):
            for x in range(img.width):
                _, _, _, alpha = pixels[x, y]
                if alpha > 0:
                    pixels[x, y] = rgb_color + (alpha,)
    
    buffer = BytesIO()
    img.save(buffer, format = "PNG")
    photoimage.configure(data = buffer.getvalue())