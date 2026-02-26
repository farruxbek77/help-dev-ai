# 🚀 Replit.com - 1 Klik Bilan Bot 24/7!

## ✅ Eng Oson Yo'l (3 Daqiqa)

**Hech narsa o'rnatish kerak emas!**

---

## 📝 3 Daqiqada Bot 24/7

### 1️⃣ Replit'ga Kirish (30 soniya)

1. **Saytga kiring:** https://replit.com
2. **"Sign up" bosing**
3. **Google yoki GitHub bilan kiring**

---

### 2️⃣ Yangi Repl Yaratish (30 soniya)

1. **"+ Create Repl" bosing**
2. **"Python" tanlang**
3. **Nom:** `telegram-bot-24-7`
4. **"Create Repl" bosing**

---

### 3️⃣ Fayllarni Yaratish (1 daqiqa)

#### bot.py

**Chap tarafda "Files" → "+" → "bot.py"**

Sizning `bot.py` kodingizni ko'chiring.

#### site_generator.py

**"+" → "site_generator.py"**

Sizning `site_generator.py` kodingizni ko'chiring.

#### requirements.txt

**"+" → "requirements.txt"**

```txt
python-telegram-bot==21.0
python-dotenv==1.0.0
```

#### .env

**"+" → ".env"**

```env
TELEGRAM_BOT_TOKEN=8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0
```

---

### 4️⃣ Botni Ishga Tushirish (30 soniya)

1. **"Run" tugmasini bosing** (yuqorida)
2. **Kutubxonalar avtomatik o'rnatiladi**
3. **Bot ishga tushadi!**

**Natija:**
```
🌟 Bot ishlayapti - Pro Max Edition! 💎
```

---

### 5️⃣ Always On (30 soniya)

**Replit'da bot to'xtamasligi uchun:**

1. **Chap tarafda "Tools" bosing**
2. **"Always On" tanlang**
3. **"Enable Always On" bosing**

**⚠️ Always On - 1 oy bepul, keyin $7/oy**

**Bepul variant:** Keep-alive script (pastda)

---

## 🎉 Tayyor!

**Bot endi 24/7 ishlaydi!**

- ✅ Noutbukni o'chirishingiz mumkin
- ✅ Bot serverda ishlaydi
- ✅ Oson
- ✅ Tez

---

## 💡 Bepul Keep-Alive (Always On o'rniga)

### keep_alive.py yarating:

```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti! 🚀"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

### bot.py ga qo'shing:

```python
from keep_alive import keep_alive

def main():
    keep_alive()  # Bu qatorni qo'shing
    app = Application.builder().token(BOT_TOKEN).build()
    # ... qolgan kod
```

### requirements.txt ga qo'shing:

```txt
python-telegram-bot==21.0
python-dotenv==1.0.0
flask==3.0.0
```

### UptimeRobot sozlang:

1. **uptimerobot.com'ga kiring**
2. **"Add New Monitor" bosing**
3. **Monitor Type:** HTTP(s)
4. **URL:** Replit'dagi bot URL'i (yuqorida ko'rsatiladi)
5. **Monitoring Interval:** 5 daqiqa
6. **"Create Monitor" bosing**

**Bot har 5 daqiqada ping oladi - uxlamaydi!**

---

## 🧪 Test Qilish

1. **Telegram'da botni oching**
2. **/start** yuboring
3. **Bot javob berishi kerak**
4. **Replit'ni yoping**
5. **Yana /start yuboring**
6. **Bot javob bersa - muvaffaqiyat!** 🎉

---

## 📊 Monitoring

**Replit'da:**
- **Console** - Bot loglarini ko'rish
- **Webview** - Keep-alive sahifasini ko'rish

---

## 🔄 Botni Yangilash

**Kod o'zgartirish:**

1. **Faylni oching**
2. **O'zgartiring**
3. **"Run" bosing**

**Replit avtomatik yangilanadi!**

---

## 🛑 Botni To'xtatish

**"Stop" tugmasini bosing** (yuqorida)

---

## 🐛 Muammolar

### Bot ishlamayapti?

**Console'ni tekshiring:**
- Qizil xatoliklarni o'qing
- Ko'pincha token noto'g'ri

### "Module not found"?

**requirements.txt'ni tekshiring:**
- Barcha kutubxonalar yozilganmi?
- "Run" bosing - avtomatik o'rnatiladi

### Bot uxlab qoladi?

**Keep-alive + UptimeRobot ishlatmadingizmi?**

---

## 💰 Narxlar

### Bepul Plan:
- ✅ Cheksiz Repl'lar
- ✅ 500 MB xotira
- ✅ 500 MB disk
- ⚠️ Bot 1 soat faoliyatsiz bo'lsa uxlaydi

### Hacker Plan ($7/oy):
- ✅ Always On
- ✅ 2 GB xotira
- ✅ 10 GB disk
- ✅ Bot hech qachon uxlamaydi

**Bepul variant:** Keep-alive + UptimeRobot (yuqorida)

---

## 🎯 Alternativ: Glitch.com

**Agar Replit ishlamasa:**

1. **glitch.com'ga kiring**
2. **"New Project" → "hello-python"**
3. **Fayllarni yarating**
4. **"Show" bosing**

**Glitch ham bepul va oson!**

---

## 📞 Yordam

**Replit Docs:**
https://docs.replit.com

**Telegram:**
@FrontendBackendUz

---

## ✅ Xulosa

**3 daqiqada bot 24/7 ishlaydi!**

1. Replit'ga kiring
2. Yangi Repl yarating
3. Fayllarni yarating
4. "Run" bosing
5. Keep-alive qo'shing
6. Noutbukni o'chiring - Bot ishlaydi! 🚀

---

**Vaqt:** 3 daqiqa  
**Qiyinlik:** Juda oson  
**Narx:** Bepul (Keep-alive bilan)  
**GitHub:** Kerak emas!  
**Natija:** 24/7 ishlaydigan bot ✅

---

## 🎁 Bonus: Replit'da Secrets

**.env o'rniga Secrets ishlatish:**

1. **Chap tarafda "Tools" → "Secrets"**
2. **"New Secret" bosing**
3. **Key:** `TELEGRAM_BOT_TOKEN`
4. **Value:** `8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0`
5. **"Add Secret" bosing**

**bot.py'da:**
```python
import os
BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
```

**Secrets xavfsizroq!**
