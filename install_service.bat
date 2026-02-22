@echo off
echo ========================================
echo   BOT SERVICE O'RNATISH
echo ========================================
echo.
echo Bu bot Windows yonilganda avtomatik ishga tushadi
echo va doimo background'da ishlaydi.
echo.
pause

REM Startup papkasiga VBS faylni nusxalash
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set CURRENT_DIR=%~dp0

echo.
echo 1. Startup papkasiga shortcut yaratilmoqda...

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTUP_FOLDER%\TelegramBotService.lnk'); $s.TargetPath = '%CURRENT_DIR%start_service.vbs'; $s.WorkingDirectory = '%CURRENT_DIR%'; $s.WindowStyle = 7; $s.Save()"

echo.
echo 2. Botni hozir ishga tushirish...
start "" "%CURRENT_DIR%start_service.vbs"

echo.
echo ========================================
echo   MUVAFFAQIYATLI O'RNATILDI!
echo ========================================
echo.
echo Bot endi:
echo - Background'da ishlayapti
echo - Windows yonilganda avtomatik ishga tushadi
echo - Xatolik bo'lsa avtomatik qayta ishga tushadi
echo.
echo Loglarni ko'rish: bot_service.log
echo Botni to'xtatish: stop_service.bat
echo.
pause
