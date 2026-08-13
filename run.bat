@echo off
title Ultron A.I. v2
cd /d "%~dp0"
python launcher.py
if errorlevel 1 (
    echo.
    echo [!] Python not found or launcher failed.
    echo     Install Python 3.10+ from https://python.org
    echo     Then run: pip install pywebview
    echo.
    pause
)
