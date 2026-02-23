# 💻 Windows'da Bot 24/7 Ishlashi

## ❌ Muammo

Terminal yopilganda bot to'xtaydi.

## ✅ 3 ta Yechim

---

## 1️⃣ Windows Service (ENG YAXSHI) ⭐

Bot Windows xizmati sifatida ishlaydi - terminal kerak emas!

### Qadamlar:

#### 1. NSSM yuklab oling
```
https://nssm.cc/download
→ nssm-2.24.zip yuklab oling
→ Ochib, nssm.exe ni Bot papkasiga ko'chiring
```

#### 2. Service yaratish
```cmd
# CMD ni Administrator sifatida oching
# Bot papkasiga o'ting
cd C:\Users\555\Desktop\Bot

# Service yaratish
nssm install TelegramBot
```

#### 3. Sozlamalar
Oyna ochiladi:

**Application tab:**
- Path: `C:\Python\python.exe` (yoki `where python`)
- Startup directory: `C:\Users\555\Desktop\Bot`
- Arguments: `bot.py`

**Details tab:**
- Display name: `Telegram Bot`
- Description: `Professional Telegram Bot Service`
- Startup type: `Automatic`

**Install service** bosing

#### 4. Service'ni ishga tushirish
```cmd
nssm start TelegramBot
```

#### 5. Tekshirish
```cmd
nssm status TelegramBot
```

### Service'ni boshqarish:

```cmd
# To'xtatish
nssm stop TelegramBot

# Qayta ishga tushirish
nssm restart TelegramBot

# O'chirish
nssm remove TelegramBot confirm
```

---

## 2️⃣ Task Scheduler (OSON)

Windows'ning o'zida bor, hech narsa yuklamasdan.

### Qadamlar:

#### 1. Task Scheduler ochish
```
Win + R → taskschd.msc → Enter
```

#### 2. Task yaratish
```
Action → Create Basic Task
```

#### 3. Sozlamalar:

**Name:** `Telegram Bot`

**Trigger:** `When the computer starts`

**Action:** `Start a program`

**Program/script:** 
```
C:\Python\python.exe
```

**Add arguments:**
```
bot.py
```

**Start in:**
```
C:\Users\555\Desktop\Bot
```

#### 4. Qo'shimcha sozlamalar

Task'ni o'ng tugma → Properties:

**General tab:**
- ✅ Run whether user is logged on or not
- ✅ Run with highest privileges

**Conditions tab:**
- ❌ Start the task only if the computer is on AC power

**Settings tab:**
- ✅ Allow task to be run on demand
- ✅ If the task fails, restart every: 1 minute

#### 5. Ishga tushirish

Task'ni o'ng tugma → Run

---

## 3️⃣ Startup Folder (ENG ODDIY)

Kompyuter yonganda avtomatik ishga tushadi.

### Qadamlar:

#### 1. Startup papkasini ochish
```
Win + R
shell:startup
Enter
```

#### 2. Shortcut yaratish

Bot papkasida `start_bot.bat` yarating:

```batch
@echo off
cd /d "%~dp0"
python bot.py
pause
```

#### 3. Shortcut'ni Startup'ga ko'chirish

`start_bot.bat` ni Startup papkasiga ko'chiring yoki shortcut yarating.

#### 4. Test qilish

Kompyuterni restart qiling - Bot avtomatik ishga tushadi!

---

## 🎯 Qaysi Birini Tanlash?

| Usul | Qiyinlik | Terminal | Restart | Tavsiya |
|------|----------|----------|---------|---------|
| Windows Service | O'rta | Yo'q | Avtomatik | ⭐⭐⭐⭐⭐ |
| Task Scheduler | Oson | Yo'q | Avtomatik | ⭐⭐⭐⭐ |
| Startup Folder | Juda oson | Ha | Qo'lda | ⭐⭐⭐ |

---

## 📁 Kerakli Fayllar

### start_bot.bat
```batch
@echo off
title Telegram Bot
cd /d "%~dp0"
python bot.py
pause
```

### start_bot_hidden.vbs (Terminal ko'rinmasin)
```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d C:\Users\555\Desktop\Bot && python bot.py", 0, False
```

### restart_bot.bat
```batch
@echo off
taskkill /F /IM python.exe
timeout /t 2
start "" python bot.py
```

---

## 🔄 Avtomatik Restart

### keep_alive.bat
```batch
@echo off
:loop
python bot.py
echo Bot to'xtadi! 10 soniyadan keyin qayta ishga tushadi...
timeout /t 10
goto loop
```

---

## 🧪 Test Qilish

### 1. Bot ishga tushiring
```cmd
python bot.py
```

### 2. Terminal'ni yoping

### 3. Telegram'da test qiling
```
/start
```

### 4. Agar ishlamasa:

**Windows Service:** Eng ishonchli
**Task Scheduler:** Yaxshi alternativ
**Startup Folder:** Oddiy, lekin terminal ko'rinadi

---

## 💡 Tavsiyalar

### 1. Log Faylini Yaratish

`bot.py` ga qo'shing:
```python
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### 2. Xatoliklarni Tutish

```python
try:
    app.run_polling()
except Exception as e:
    logging.error(f"Xatolik: {e}")
```

### 3. Restart Mexanizmi

```python
import sys
import os

def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
```

---

## 🐛 Muammolarni Hal Qilish

### Bot ishlamayapti:

```cmd
# Jarayonni tekshirish
tasklist | findstr python

# Log'ni ko'rish
type bot.log

# Qayta ishga tushirish
taskkill /F /IM python.exe
python bot.py
```

### "Python not found":

```cmd
# Python yo'lini topish
where python

# PATH'ga qo'shish
setx PATH "%PATH%;C:\Python"
```

---

## 📊 Monitoring

### Bot ishlayotganini tekshirish:

```cmd
# Task Manager
Ctrl + Shift + Esc
→ Details
→ python.exe

# CMD
tasklist | findstr python

# PowerShell
Get-Process python
```

---

## ✅ Xulosa

**Eng yaxshi yechim:** Windows Service (NSSM)

**Afzalliklari:**
- ✅ Terminal kerak emas
- ✅ Avtomatik ishga tushadi
- ✅ Avtomatik restart
- ✅ Background'da ishlaydi
- ✅ Kompyuter yonganda avtomatik

**Qadamlar:**
1. NSSM yuklab oling
2. Service yarating
3. Ishga tushiring
4. Terminal yoping - Bot ishlaydi! ✅

---

**Vaqt:** 10 daqiqa  
**Qiyinlik:** Oson  
**Natija:** Terminal yopilganda ham bot ishlaydi 🚀
