@echo off
title Building Files ^& Folders on taskbar...

echo (1/4) Deleting temporary files...
echo.

rmdir /q /s "build"
rmdir /q /s "dist"
del /f /q "fnf_on_taskbar.spec"

echo.
echo (2/4) Installing dependencies...
echo.

python -m pip install -r requirements.txt
python -m pip install pyinstaller

echo.
echo (3/4) Building with PyInstaller...
echo.

python -m PyInstaller main.pyw --onedir --icon icon.ico --version-file "version.txt" --name "fnf_on_taskbar" --add-data "separators;./separators/" --add-data "icon.ico;." --exclude-module "numpy" --exclude-module "setuptools" --exclude-module "wheel" --exclude-module "importlib_metadata" --exclude-module "markupsafe"

echo .
echo (4/4) Deleting temporary files...
echo.

rmdir /q /s "build"
del /f /q "fnf_on_taskbar.spec"
ren "dist" "build"

echo.
echo Files ^& Folders on taskbar has been successfully built.
echo Press any key to exit...
timeout /t -1 > NUL