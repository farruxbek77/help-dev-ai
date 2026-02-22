@echo off
echo ========================================
echo   BOT AVTOMATIK ISHGA TUSHIRISHNI O'CHIRISH
echo ========================================
echo.

set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

if exist "%STARTUP_FOLDER%\TelegramBot.lnk" (
    del "%STARTUP_FOLDER%\TelegramBot.lnk"
    echo Avtomatik ishga tushirish o'chirildi.
) else (
    echo Avtomatik ishga tushirish topilmadi.
)

echo.
pause
