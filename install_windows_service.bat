@echo off
title Telegram Bot - Windows Service O'rnatish
color 0B

echo ========================================
echo   TELEGRAM BOT - WINDOWS SERVICE
echo ========================================
echo.

REM Administrator huquqini tekshirish
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [XATO] Bu skriptni Administrator sifatida ishga tushiring!
    echo.
    echo O'ng tugma bosing va "Run as administrator" tanlang
    pause
    exit /b 1
)

echo [1/5] Python yo'lini topish...
for /f "tokens=*" %%i in ('where python') do set PYTHON_PATH=%%i
if "%PYTHON_PATH%"=="" (
    echo [XATO] Python topilmadi!
    echo Python o'rnatilganligini tekshiring: python --version
    pause
    exit /b 1
)
echo Python topildi: %PYTHON_PATH%
echo.

echo [2/5] Bot papkasini aniqlash...
set BOT_DIR=%~dp0
echo Bot papkasi: %BOT_DIR%
echo.

echo [3/5] NSSM mavjudligini tekshirish...
if not exist "%BOT_DIR%nssm.exe" (
    echo [XATO] nssm.exe topilmadi!
    echo.
    echo NSSM yuklab oling:
    echo 1. https://nssm.cc/download
    echo 2. nssm-2.24.zip yuklab oling
    echo 3. nssm.exe ni Bot papkasiga ko'chiring
    echo.
    pause
    exit /b 1
)
echo NSSM topildi!
echo.

echo [4/5] Service yaratish...
"%BOT_DIR%nssm.exe" install TelegramBot "%PYTHON_PATH%" "%BOT_DIR%bot.py"
"%BOT_DIR%nssm.exe" set TelegramBot AppDirectory "%BOT_DIR%"
"%BOT_DIR%nssm.exe" set TelegramBot DisplayName "Telegram Bot Service"
"%BOT_DIR%nssm.exe" set TelegramBot Description "Professional Telegram Bot - 24/7"
"%BOT_DIR%nssm.exe" set TelegramBot Start SERVICE_AUTO_START
"%BOT_DIR%nssm.exe" set TelegramBot AppStdout "%BOT_DIR%bot_service.log"
"%BOT_DIR%nssm.exe" set TelegramBot AppStderr "%BOT_DIR%bot_service_error.log"
echo Service yaratildi!
echo.

echo [5/5] Service'ni ishga tushirish...
"%BOT_DIR%nssm.exe" start TelegramBot
echo.

echo ========================================
echo   MUVAFFAQIYATLI O'RNATILDI!
echo ========================================
echo.
echo Service nomi: TelegramBot
echo Status: Ishlamoqda
echo.
echo Boshqarish buyruqlari:
echo   nssm start TelegramBot    - Ishga tushirish
echo   nssm stop TelegramBot     - To'xtatish
echo   nssm restart TelegramBot  - Qayta ishga tushirish
echo   nssm status TelegramBot   - Holatni ko'rish
echo   nssm remove TelegramBot   - O'chirish
echo.
echo Log fayllar:
echo   bot_service.log       - Oddiy log
echo   bot_service_error.log - Xatoliklar
echo.
echo Terminal yopilganda ham bot ishlaydi!
echo.
pause
