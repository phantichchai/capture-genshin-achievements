@echo off

rem Check if the argument is provided
if "%path%"=="" (
    echo Please provide the directory path using the "path" argument.
    exit /b
)

rem Navigate to the specified directory
cd /d %path%

rem Run PyInstaller to build the executable
pyinstaller ^
--noconsole ^
--add-data "resources/*;resources/" ^
--icon "resources/icon.ico" ^
--clean ^
main.py
