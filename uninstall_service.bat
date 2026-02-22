@echo off
echo ========================================
echo   BOT SERVICE O'CHIRISH
echo ========================================
echo.

REM Botni to'xtatish
echo 1. Botni to'xtatish...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM python3.exe 2>nul
taskkill /F /IM pythonw.exe 2>nul

REM Startup'dan o'chirish
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

echo 2. Startup'dan o'chirish...
if exist "%STARTUP_FOLDER%\TelegramBotService.lnk" (
    del "%STARTUP_FOLDER%\TelegramBotService.lnk"
    echo Startup'dan o'chirildi.
) else (
    echo Startup'da topilmadi.
)

echo.
echo ========================================
echo   MUVAFFAQIYATLI O'CHIRILDI!
echo ========================================
echo.
pause
