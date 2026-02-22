@echo off
title Telegram Bot
:loop
echo Bot ishga tushirilmoqda...
python3 bot.py
echo Bot to'xtadi. 5 soniyadan keyin qayta ishga tushadi...
timeout /t 5
goto loop
