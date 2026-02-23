#!/bin/bash

# Bot Always Running Script

while true; do
    echo "🚀 Bot ishga tushirilmoqda..."
    python3 bot.py
    
    echo "⚠️ Bot to'xtadi! 10 soniyadan keyin qayta ishga tushadi..."
    sleep 10
done
