# 📋 Replit'ga Ko'chirish Uchun Fayllar

## Har bir faylni Replit'da yarating va quyidagi kodni ko'chiring

---

## 1️⃣ requirements.txt

```txt
python-telegram-bot==21.0
python-dotenv==1.0.0
flask==3.0.0
```

---

## 2️⃣ .env

```env
TELEGRAM_BOT_TOKEN=8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0
```

---

## 3️⃣ keep_alive.py

```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "🚀 Bot 24/7 ishlayapti! ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

---

## 4️⃣ bot.py

**Bu faylni Windows'dan ko'chiring:**

1. Windows'da: `C:\Users\555\Desktop\Bot\bot.py` ni oching
2. Ctrl+A → Ctrl+C
3. Replit'da: bot.py yarating → Ctrl+V

---

## 5️⃣ site_generator.py

**Bu faylni ham Windows'dan ko'chiring:**

1. Windows'da: `C:\Users\555\Desktop\Bot\site_generator.py` ni oching
2. Ctrl+A → Ctrl+C
3. Replit'da: site_generator.py yarating → Ctrl+V

---

## ✅ Barcha Fayllar Tayyor Bo'lgandan Keyin:

1. Replit'da yuqorida **"Run"** tugmasini bosing
2. 1-2 daqiqa kuting (kutubxonalar o'rnatiladi)
3. Console'da ko'rasiz: `🌟 Bot ishlayapti`
4. Yuqorida URL paydo bo'ladi
5. Bu URL'ni UptimeRobot'ga kiriting

**Tayyor! Bot 24/7 ishlaydi!** 🚀
