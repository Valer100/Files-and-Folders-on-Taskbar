from . import _info

# Language info
language = "English"
language_en = "English"
author = "Valer100"

# Main window
choose_a_file = "Choose a file"
choose_a_folder = "Choose a folder"
pin_to_taskbar_a_shortcut_to = "Pin to taskbar a shortcut to:"
a_file = "A file"
a_folder = "A folder"
a_separator = "A separator"
file_desc = "Choose a file and create a shortcut"
folder_desc = "Choose a folder and create a shortcut"
separator_desc = "Choose a separator type and create a shortcut"
pin_separator = "Pin separator"
settings = "Settings"

# Pin separator window
choose_a_separator_type = "Choose a separator type:"
vertical_line = "Vertical line"
horizontal_line = "Horizontal line"
transparent = "Transparent"
create_the_shortcut = "Create the shortcut"

# Customize shortcut window
customize_shortcut = "Customize shortcut"
use_folder_icon = "Use folder's icon"
change_icon = "Change icon"
illegal_characters = "\\, /, :, *, ?, <, >, |"
illegal_names = "nul, con, prn, aux, com1, com2, com3, com4, com5, com6, com7, com8, com9, lpt1, lpt2, lpt3, lpt4, lpt5, lpt6, lpt7, lpt8, lpt9"
shortcut_name_invalid = "Invalid shortcut name"
shortcut_name_invalid_description = f"The shortcut's name contains illegal characters, like {illegal_characters} or uses a system-reserved name, like {illegal_names}.\n\nThe illegal characters will be replaced with an underscore (_) and the reserved names will be appended with an underscore (_)."

# Other
open_source_licenses = "Open source licenses"
change_language = "Change language"
change_theme = "Change theme"
light_theme = "Light theme"
dark_theme = "Dark theme"
lang_system_default = "System default"
ok = "OK"
cancel = "Cancel"
shortcut_created_message = "The shortcut has been created.\n\nNow, drag the shortcut from the folder that was opened to your taskbar and then close the File Explorer window.\n\nYou have to do this extra step, because it's not that easy for 3rd party programs to pin a shortcut to the taskbar on Windows 10 and 11."
about_this_app = "About this app"
about_title = "About Files & Folders on Taskbar"
version = f"Version {_info.version}"
last_commit = f"(last commit: {_info.last_commit})"
issues = "Issues"
latest_version = "Latest version"
copy_traceback = "Copy traceback"
license = "License"
translation_made_by = "Translation made by %a"