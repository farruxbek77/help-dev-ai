@echo off
echo ========================================
echo   BOT QAYTA ISHGA TUSHIRISH
echo ========================================
echo.

echo 1. Botni to'xtatish...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM python3.exe 2>nul
timeout /t 2 >nul

echo 2. Botni ishga tushirish...
start "" "%~dp0start_service.vbs"

echo.
echo Bot qayta ishga tushirildi!
echo.
timeout /t 3
