# 🚀 Render.com - 5 Daqiqada Bot 24/7 Ishlatish

## ✅ Eng Oson Yo'l (GitHub kerak emas!)

---

## 📝 Qadamlar

### 1️⃣ Render.com'ga Kirish (1 daqiqa)

1. **Saytga kiring:** https://render.com
2. **"Get Started for Free"** bosing
3. **Email bilan ro'yxatdan o'ting** (yoki GitHub bilan)

---

### 2️⃣ New Web Service (1 daqiqa)

1. **Dashboard'da "New +" bosing**
2. **"Web Service" tanlang**
3. **"Build and deploy from a Git repository" o'rniga**
4. **"Public Git repository" tanlang**

---

### 3️⃣ GitHub Repository (Agar yo'q bo'lsa)

#### Variant A: GitHub bor bo'lsa

1. **GitHub'ga kiring:** https://github.com
2. **"New repository" bosing**
3. **Nom:** `telegram-bot-24-7`
4. **Public tanlang**
5. **"Create repository" bosing**

#### Variant B: GitHub yo'q bo'lsa

**Render'da "Public Git repository" URL'ni kiriting:**
```
https://github.com/yourusername/telegram-bot
```

Yoki men sizga tayyor repository yaratib beraman!

---

### 4️⃣ Fayllarni GitHub'ga Yuklash (3 daqiqa)

**Noutbukda PowerShell'da:**

```powershell
# Bot papkasiga o'tish
cd C:\Users\555\Desktop\Bot

# Git sozlash (birinchi marta)
git config --global user.name "Sizning Ismingiz"
git config --global user.email "sizning@email.com"

# Git init
git init
git add .
git commit -m "Bot 24/7"

# GitHub'ga yuklash
git remote add origin https://github.com/yourusername/telegram-bot-24-7.git
git branch -M main
git push -u origin main
```

**Parol so'rasa:** GitHub Personal Access Token kerak
- GitHub → Settings → Developer settings → Personal access tokens → Generate new token

---

### 5️⃣ Render'da Sozlash (2 daqiqa)

**Name:** `telegram-bot-24-7`

**Environment:** `Python 3`

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python bot.py
```

**Instance Type:** `Free`

---

### 6️⃣ Environment Variables (1 daqiqa)

**"Add Environment Variable" bosing:**

| Key | Value |
|-----|-------|
| `TELEGRAM_BOT_TOKEN` | `8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0` |

---

### 7️⃣ Deploy! (2 daqiqa)

1. **"Create Web Service" bosing**
2. **Render avtomatik deploy qiladi**
3. **2-3 daqiqa kuting**
4. **"Live" yozuvi chiqsa - tayyor!** ✅

---

## 🎉 Tayyor!

**Bot endi 24/7 ishlaydi!**

- ✅ Noutbukni o'chirishingiz mumkin
- ✅ Bot serverda ishlaydi
- ✅ Bepul
- ✅ Avtomatik restart

---

## 🧪 Test Qilish

1. **Telegram'da botni oching**
2. **/start** yuboring
3. **Noutbukni o'chiring**
4. **Yana /start yuboring**
5. **Bot javob bersa - muvaffaqiyat!** 🎉

---

## 🔄 Botni Yangilash

**Kod o'zgartirsangiz:**

```powershell
cd C:\Users\555\Desktop\Bot
git add .
git commit -m "Yangilash"
git push
```

**Render avtomatik yangilanadi!**

---

## 📊 Monitoring

**Render Dashboard'da:**
- **Logs** - Bot loglarini ko'rish
- **Metrics** - Xotira va CPU
- **Events** - Deploy tarixi

---

## 🐛 Muammolar

### Bot ishlamayapti?

1. **Render Dashboard → Logs**
2. **Qizil xatoliklarni o'qing**
3. **Ko'pincha:**
   - Token noto'g'ri
   - requirements.txt yo'q
   - Python versiyasi eski

### "Application failed to respond"?

**Start Command'ni o'zgartiring:**
```bash
python3 bot.py
```

### Bot to'xtab qoladi?

**Render Free plan:** 15 daqiqa faoliyatsiz bo'lsa uxlaydi.

**Yechim:** Keep-alive script qo'shing (pastda)

---

## 💡 Keep-Alive (Bot Uxlamasin)

### keep_alive.py yarating:

```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

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
    # ...
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
3. **URL:** Render'dagi bot URL'i
4. **Interval:** 5 daqiqa
5. **Bot har 5 daqiqada ping oladi - uxlamaydi!**

---

## 🎯 Alternativ: Railway.app

**Agar Render ishlamasa:**

1. **railway.app'ga kiring**
2. **"Start a New Project"**
3. **"Deploy from GitHub repo"**
4. **Environment Variables qo'shing**
5. **Deploy!**

**Railway ham bepul va oson!**

---

## 📞 Yordam Kerakmi?

**Telegram:** @FrontendBackendUz

**Render Docs:** https://render.com/docs

---

## ✅ Xulosa

**5 daqiqada bot 24/7 ishlaydi!**

1. Render.com'ga ro'yxatdan o'ting
2. GitHub'ga fayllarni yuklang
3. Render'da sozlang
4. Deploy qiling
5. Noutbukni o'chiring - Bot ishlaydi! 🚀

---

**Vaqt:** 5-10 daqiqa  
**Qiyinlik:** Juda oson  
**Narx:** Bepul  
**Natija:** 24/7 ishlaydigan bot ✅
