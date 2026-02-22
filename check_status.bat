@echo off
echo ========================================
echo   BOT HOLATI
echo ========================================
echo.

echo Python jarayonlarini qidirish...
echo.

tasklist /FI "IMAGENAME eq python.exe" 2>NUL | find /I /N "python.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [ISHLAYAPTI] Bot ishlayapti
    echo.
    tasklist /FI "IMAGENAME eq python.exe"
) else (
    tasklist /FI "IMAGENAME eq python3.exe" 2>NUL | find /I /N "python3.exe">NUL
    if "%ERRORLEVEL%"=="0" (
        echo [ISHLAYAPTI] Bot ishlayapti
        echo.
        tasklist /FI "IMAGENAME eq python3.exe"
    ) else (
        echo [TO'XTAGAN] Bot ishlamayapti
    )
)

echo.
echo ========================================
echo.

if exist "bot_service.log" (
    echo Oxirgi 10 ta log yozuvi:
    echo.
    powershell -Command "Get-Content bot_service.log -Tail 10"
) else (
    echo Log fayli topilmadi.
)

echo.
pause
