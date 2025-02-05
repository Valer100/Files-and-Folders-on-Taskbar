; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Files & Folders on Taskbar"
#define MyAppVersion "2.0.0 beta 2"
#define MyAppPublisher "Valer"
#define MyAppURL "https://github.com/Valer100/Files-and-Folders-on-Taskbar"
#define MyAppExeName "fnf_on_taskbar.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FED850FD-CA08-4EAE-871D-A21B839842F6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableDirPage=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
DisableWelcomePage=no
LicenseFile=LICENSE
PrivilegesRequired=lowest
OutputDir=build
OutputBaseFilename=fnf_on_taskbar_installer_x64
SetupIconFile=assets/installer/icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
MinVersion=10.0
UninstallDisplayName=Files & Folders on Taskbar
UninstallDisplayIcon={app}\{#MyAppExeName}
WizardSmallImageFile=assets\installer\icon_100.bmp,assets\installer\icon_125.bmp,assets\installer\icon_150.bmp,assets\installer\icon_175.bmp,assets\installer\icon_200.bmp,assets\installer\icon_225.bmp,assets\installer\icon_250.bmp
WizardImageFile=assets\installer\banner.bmp
WizardSizePercent=100
VersionInfoVersion=2.0.0

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "build\fnf_on_taskbar\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\fnf_on_taskbar\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

