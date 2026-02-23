@echo off
title Telegram Bot - Windows Service O'chirish
color 0C

echo ========================================
echo   TELEGRAM BOT - SERVICE O'CHIRISH
echo ========================================
echo.

REM Administrator huquqini tekshirish
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [XATO] Bu skriptni Administrator sifatida ishga tushiring!
    pause
    exit /b 1
)

set BOT_DIR=%~dp0

if not exist "%BOT_DIR%nssm.exe" (
    echo [XATO] nssm.exe topilmadi!
    pause
    exit /b 1
)

echo Service'ni to'xtatish...
"%BOT_DIR%nssm.exe" stop TelegramBot
timeout /t 2 >nul

echo Service'ni o'chirish...
"%BOT_DIR%nssm.exe" remove TelegramBot confirm

echo.
echo ========================================
echo   SERVICE O'CHIRILDI!
echo ========================================
echo.
pause
