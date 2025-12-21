from . import _info

# Informations sur la langue
language = "Français"
language_en = "French"
author = "Locktix"

# Fenêtre principale
choose_a_file = "Choisir un fichier"
choose_a_folder = "Choisir un dossier"
pin_to_taskbar_a_shortcut_to = "Épingler à la barre des tâches un raccourci vers :"
a_file = "Un fichier"
a_folder = "Un dossier"
a_separator = "Un séparateur"
file_desc = "Choisir un fichier et créer un raccourci"
folder_desc = "Choisir un dossier et créer un raccourci"
separator_desc = "Choisir un type de séparateur et créer un raccourci"
pin_separator = "Épingler un séparateur"
settings = "Paramètres"

# Fenêtre du séparateur
choose_a_separator_type = "Choisir un type de séparateur :"
vertical_line = "Ligne verticale"
horizontal_line = "Ligne horizontale"
transparent = "Transparent"
create_the_shortcut = "Créer le raccourci"

# Fenêtre de personnalisation du raccourci
customize_shortcut = "Personnaliser le raccourci"
use_folder_icon = "Utiliser l'icône du dossier"
change_icon = "Changer l'icône"
illegal_characters = "\\, /, :, *, ?, <, >, |"
illegal_names = "nul, con, prn, aux, com1, com2, com3, com4, com5, com6, com7, com8, com9, lpt1, lpt2, lpt3, lpt4, lpt5, lpt6, lpt7, lpt8, lpt9"
shortcut_name_invalid = "Nom de raccourci invalide"
shortcut_name_invalid_description = f"Le nom du raccourci contient des caractères interdits, comme {illegal_characters}, ou utilise un nom réservé au système, comme {illegal_names}.\n\nLes caractères interdits seront remplacés par un trait de soulignement (_) et les noms réservés seront suivis d'un trait de soulignement (_)."

# Autre
open_source_licenses = "Licences open source"
change_language = "Changer la langue"
change_theme = "Changer le thème"
light_theme = "Thème clair"
dark_theme = "Thème sombre"
lang_system_default = "Paramètre système par défaut"
ok = "OK"
cancel = "Annuler"
shortcut_created_message = "Le raccourci a été créé.\n\nMaintenant, faites glisser le raccourci depuis le dossier qui vient de s'ouvrir vers votre barre des tâches, puis fermez la fenêtre de l'Explorateur de fichiers.\n\nCette étape supplémentaire est nécessaire car il n'est pas aisé pour un programme tiers d'épingler un raccourci directement sur la barre des tâches de Windows 10 et 11."
about_this_app = "À propos de cette application"
about_title = "À propos de Files & Folders on Taskbar"
version = f"Version {_info.version}"
last_commit = f"(dernier commit : {_info.last_commit})"
issues = "Problèmes / Bugs"
latest_version = "Dernière version"
copy_traceback = "Copier le traceback"
license = "Licence"
translation_made_by = "Traduction réalisée par %a"