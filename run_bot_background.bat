@echo off
cd /d "%~dp0"
start /B python bot.py
echo Bot background'da ishga tushdi!
echo.
echo To'xtatish uchun: stop_bot.bat
timeout /t 3
