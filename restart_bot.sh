#!/bin/bash

# Bot Restart Script for PythonAnywhere

echo "🔄 Botni qayta ishga tushirish..."

# Eski jarayonni to'xtatish
pkill -f bot.py
echo "✅ Eski jarayon to'xtatildi"

# 2 soniya kutish
sleep 2

# Papkaga o'tish (o'zingiznikini yozing)
cd /home/username/mysite

# Botni ishga tushirish
nohup python3 bot.py > bot.log 2>&1 &

echo "✅ Bot ishga tushdi!"
echo "📊 Log: tail -f bot.log"
