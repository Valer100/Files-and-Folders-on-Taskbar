<div align="center">
    <img src="assets/banner.png">
</div>

# Files & Folders on Taskbar
[![Release](https://img.shields.io/github/v/release/Valer100/Files-and-Folders-on-Taskbar?label=stable)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/releases/latest)
[![Pre-release](https://img.shields.io/github/v/release/Valer100/Files-and-Folders-on-Taskbar?include_prereleases&label=pre-release)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/releases)
[![Windows](https://img.shields.io/badge/windows-10+-blue)]()
[![Architecture](https://img.shields.io/badge/architecture-x64-blue)]()
[![Downloads](https://img.shields.io/github/downloads/Valer100/Files-and-Folders-on-Taskbar/total)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/releases)
[![Stars](https://img.shields.io/github/stars/Valer100/Files-and-Folders-on-Taskbar?style=flat&color=yellow)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/stargazers)
[![Contributors](https://img.shields.io/github/contributors/Valer100/Files-and-Folders-on-Taskbar)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/Valer100/Files-and-Folders-on-Taskbar)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/commits/main)
[![Commits since latest release](https://img.shields.io/github/commits-since/Valer100/Files-and-Folders-on-Taskbar/latest)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/commits/main)
[![License](https://img.shields.io/github/license/Valer100/Files-and-Folders-on-Taskbar)](https://github.com/Valer100/Files-and-Folders-on-Taskbar/blob/main/LICENSE)

A simple tool for pinning files and folders to the taskbar. It looks like this:

![Screenshot](assets/screenshot.png)

This tool can create a shortcut to a file or folder that can be pinned to your taskbar. 

It can also create a separator shortcut for further organising the shortcuts on your taskbar.

## ℹ️ How it works?
Before creating the shortcut, you'll be asked to pick the file/folder you want to pin to the taskbar. 

After choosing the file or folder, a dialog asking you to customize the shortcut will appear. It looks like this:

![Customization dialog](assets/screenshot_shortcut_customization.png)

This dialog will allow you to change the name of the shortcut and its icon. If you uncheck "Use folder's icon", you will be able to choose a custom icon for the folder's shortcut. You can also choose a custom icon for a file's shortcut.

After customizing the shortcut, a File Explorer window will open with the folder where the shortcut has been saved. Now you'll need to drag the shortcut to your taskbar. I will have to find a way to pin the shortcut directly to the taskbar, but right now it seems complicated...

## 🎨 Separator styles
This app supports the following separator styles:

| Style | Info |
|:------|:-----|
| Vertical | A vertical line. Suitable for horizontal taskbars.
| Horizontal | A horizontal line. Suitable for vertical taskbars.
| Transparent | A completly transparent image.

When creating a separator shortcut, you will be asked about its style in this window:

![Pin separator window](assets/screenshot_separators.png)

## ▶️ Running from source
Before running from the source, you must install the dependencies. To do that, open Command Prompt in the folder of the cloned repository and run the following command:

```
pip install -r requirements.txt
```

After that, open the `main.py` file.

## 🏗️ Building

### Building the app
Just run `build_app.bat`. It will do everything needed to build the app. After the build process is done, you can find the built app in a `build` folder (or in a `dist` folder if the renaming process fails).

### Building the installer
Before building the installer, you must install Inno Setup Compiler on your computer. You can download it [here](https://jrsoftware.org/isdl.php/).

Also, you must build the app first before building the installer. After building the app, make sure a `build` folder appears. If it doesn't and appears a `dist` folder intstead, rename that folder to `build`. After that, right-click `build_installer_x86.iss`, `build_installer_x64.iss` or `build_installer_arm64.iss` (depending on your CPU's architecture) and choose `Compile`. After the installer was built, you can find it in the same `build` folder.

## 💿 Download
Click [here](https://github.com/Valer100/Files-and-Folders-on-Taskbar/releases/latest) to download the latest version. You can download either the portable or the installer version.

> [!WARNING]
> At the moment, the binaries from Releases tab were built only for 64 bit Windows. They will not work on 32 bit Windows.

## 📜 License
[MIT](https://github.com/Valer100/Files-and-Folders-on-Taskbar/blob/main/LICENSE)
