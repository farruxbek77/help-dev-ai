@echo off
title Telegram Bot - 24/7 Auto Restart
color 0A

:loop
echo ========================================
echo    TELEGRAM BOT ISHGA TUSHIRILMOQDA
echo ========================================
echo.
echo Vaqt: %date% %time%
echo.

cd /d "%~dp0"
python bot.py

echo.
echo ========================================
echo    BOT TO'XTADI!
echo    10 soniyadan keyin qayta ishga tushadi...
echo ========================================
timeout /t 10
goto loop
