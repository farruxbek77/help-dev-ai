@echo off
echo Testing bot...
cd /d "%~dp0"
python --version
echo.
echo Starting bot...
python bot.py
