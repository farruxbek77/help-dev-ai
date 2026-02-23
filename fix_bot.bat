@echo off
echo ========================================
echo Bot Sessiyasini Tozalash
echo ========================================
echo.

echo 1. Python jarayonlarini to'xtatish...
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 >nul

echo 2. Webhook ni o'chirish...
curl -s "https://api.telegram.org/bot8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0/deleteWebhook"
echo.
echo.

echo 3. 3 soniya kutish...
timeout /t 3 >nul

echo 4. Botni ishga tushirish...
start "Telegram Bot" python bot.py

echo.
echo ========================================
echo Tayyor! Bot ishga tushdi!
echo ========================================
echo.
echo Telegram'da /start yuboring
pause
