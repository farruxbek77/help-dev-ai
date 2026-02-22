@echo off
echo ========================================
echo   BOT AVTOMATIK ISHGA TUSHIRISH
echo ========================================
echo.
echo Bot Windows yonilganda avtomatik ishga tushadi.
echo.

set SCRIPT_PATH=%~dp0start_bot_hidden.vbs
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

echo Startup papkasiga shortcut yaratilmoqda...
echo.

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTUP_FOLDER%\TelegramBot.lnk'); $s.TargetPath = '%SCRIPT_PATH%'; $s.WorkingDirectory = '%~dp0'; $s.Save()"

echo.
echo ========================================
echo   MUVAFFAQIYATLI O'RNATILDI!
echo ========================================
echo.
echo Bot endi Windows yonilganda avtomatik ishga tushadi.
echo.
echo Shortcut joylashuvi:
echo %STARTUP_FOLDER%\TelegramBot.lnk
echo.
pause
