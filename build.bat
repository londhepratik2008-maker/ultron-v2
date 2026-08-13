@echo off
title Ultron A.I. v2 - Build
cd /d "%~dp0"

echo ============================================
echo   Ultron A.I. v2 - Building .exe
echo ============================================
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo [!] Python not found. Install Python 3.10+ first.
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
pip install pywebview pyinstaller --quiet

echo [2/3] Building executable...
pyinstaller --noconfirm --onefile --windowed ^
    --name "Ultron A.I. v2" ^
    --add-data "index.html;." ^
    --add-data "assets;assets" ^
    --icon NONE ^
    --clean ^
    launcher.py

if errorlevel 1 (
    echo.
    echo [!] Build failed. Check errors above.
    pause
    exit /b 1
)

echo [3/3] Done!
echo.
echo ============================================
echo   Build complete!
echo   EXE location: dist\Ultron A.I. v2.exe
echo ============================================
echo.
pause
