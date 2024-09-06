import locale, ctypes

def initialize(language: str):
    if language == "default": language = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()]
    
    match language:
        case "ro_RO": from strings import ro_RO
        case _: from strings import en_US