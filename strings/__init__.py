import locale, ctypes

def load_language(language: str):
    global lang
    if language == "default": language = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()]
    
    match language:
        case "ro_RO": import strings.ro_RO; lang = strings.ro_RO
        case "fr_FR": import strings.fr_FR; lang = strings.fr_FR
        case _: import strings.en_US; lang = strings.en_US