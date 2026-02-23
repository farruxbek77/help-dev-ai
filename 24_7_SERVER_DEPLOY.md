# 🌐 Bot 24/7 Ishlashi Uchun - Server Deploy

## 🎯 Maqsad

Noutbukni o'chirganda ham bot ishlashi uchun uni serverga joylashtirish.

---

## ✅ Bepul Server Variantlari

### 1️⃣ PythonAnywhere (Eng Oson) ⭐ TAVSIYA

**Afzalliklari:**
- ✅ 100% bepul
- ✅ Oson sozlash
- ✅ 24/7 ishlaydi
- ✅ Python qo'llab-quvvatlaydi

**Qadamlar:**

#### 1. Ro'yxatdan o'ting
```
https://www.pythonanywhere.com
→ Pricing & signup
→ Create a Beginner account (FREE)
```

#### 2. Console ochish
```
Dashboard → Consoles → Bash
```

#### 3. Botni yuklash
```bash
# Git orqali (agar GitHub'da bo'lsa)
git clone https://github.com/username/bot.git
cd bot

# Yoki fayllarni upload qiling
# Files → Upload a file
```

#### 4. Virtual environment yaratish
```bash
mkvirtualenv --python=/usr/bin/python3.10 mybot
workon mybot
```

#### 5. Kutubxonalarni o'rnatish
```bash
pip install python-telegram-bot python-dotenv
```

#### 6. .env faylini yaratish
```bash
nano .env
```

Ichiga qo'ying:
```env
TELEGRAM_BOT_TOKEN=sizning_tokeningiz
```

`Ctrl + X`, `Y`, `Enter` - Saqlash

#### 7. Botni ishga tushirish
```bash
python bot.py
```

#### 8. Always-on qilish (Pullik)
Bepul versiyada botni doimo ishlatish uchun har kuni bir marta ishga tushirish kerak.

**Yechim:** Cron job qo'shish
```
Dashboard → Tasks
→ Add a new scheduled task
→ Command: /home/username/bot/run_bot.sh
→ Time: 00:00 (har kuni)
```

---

### 2️⃣ Render.com (Yaxshi Variant)

**Afzalliklari:**
- ✅ Bepul
- ✅ Avtomatik deploy
- ✅ GitHub bilan integratsiya

**Qadamlar:**

#### 1. GitHub'ga yuklash
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/bot.git
git push -u origin main
```

#### 2. Render.com'ga kirish
```
https://render.com
→ Sign up with GitHub
```

#### 3. New Web Service
```
Dashboard → New → Web Service
→ Connect GitHub repository
→ Select bot repository
```

#### 4. Sozlamalar
```
Name: telegram-bot
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: python bot.py
```

#### 5. Environment Variables
```
TELEGRAM_BOT_TOKEN = sizning_tokeningiz
```

#### 6. Deploy
```
Create Web Service
```

---

### 3️⃣ Railway.app (Zamonaviy)

**Afzalliklari:**
- ✅ Bepul ($5/oy kredit)
- ✅ Oson deploy
- ✅ Yaxshi interface

**Qadamlar:**

#### 1. Railway.app'ga kirish
```
https://railway.app
→ Login with GitHub
```

#### 2. New Project
```
Dashboard → New Project
→ Deploy from GitHub repo
→ Select bot repository
```

#### 3. Environment Variables
```
Settings → Variables
→ Add Variable
→ TELEGRAM_BOT_TOKEN = sizning_tokeningiz
```

#### 4. Deploy
Avtomatik deploy bo'ladi!

---

### 4️⃣ Heroku (Klassik)

**Eslatma:** 2022-yildan beri bepul plan yo'q, lekin mashhur.

---

## 📁 Kerakli Fayllar

### requirements.txt
```txt
python-telegram-bot==20.7
python-dotenv==1.0.0
```

### Procfile (Render/Heroku uchun)
```
worker: python bot.py
```

### .gitignore
```
.env
__pycache__/
*.pyc
*.html
*.log
```

---

## 🚀 Tezkor Deploy (PythonAnywhere)

### 1. Fayllarni tayyorlash
```bash
# Loyihangizda
pip freeze > requirements.txt
```

### 2. PythonAnywhere'ga yuklash
```
Files → Upload files
→ bot.py, site_generator.py, requirements.txt
```

### 3. Console'da
```bash
pip install --user python-telegram-bot python-dotenv
python bot.py
```

---

## 🔄 Avtomatik Restart (PythonAnywhere)

### run_bot.sh yaratish
```bash
#!/bin/bash
cd /home/username/bot
source /home/username/.virtualenvs/mybot/bin/activate
python bot.py
```

### Cron job qo'shish
```
0 * * * * /home/username/bot/run_bot.sh
```

Har soatda botni restart qiladi.

---

## 💡 Tavsiyalar

### Eng Yaxshi Variant:
1. **PythonAnywhere** - Eng oson, bepul
2. **Railway.app** - Zamonaviy, yaxshi
3. **Render.com** - GitHub integratsiya

### Qaysi Birini Tanlash?

**Agar:**
- Oddiy bot → PythonAnywhere
- GitHub bilan ishlaysiz → Render/Railway
- Professional loyiha → Railway

---

## 🐛 Muammolarni Hal Qilish

### Bot to'xtab qolsa:

**PythonAnywhere:**
```bash
# Console'da
ps aux | grep python
kill -9 <process_id>
python bot.py
```

**Render/Railway:**
```
Dashboard → Restart
```

---

## 📊 Monitoring

### Botni tekshirish:

**PythonAnywhere:**
```bash
tail -f /home/username/bot/bot.log
```

**Render/Railway:**
```
Dashboard → Logs
```

---

## 💰 Narxlar

| Platform | Bepul | Pullik |
|----------|-------|--------|
| PythonAnywhere | ✅ Ha | $5/oy |
| Render | ✅ Ha | $7/oy |
| Railway | ✅ $5 kredit | $5/oy |
| Heroku | ❌ Yo'q | $7/oy |

---

## 🎯 Xulosa

**Eng oson va bepul:** PythonAnywhere

**Qadamlar:**
1. PythonAnywhere.com'ga ro'yxatdan o'ting
2. Fayllarni yuklang
3. Kutubxonalarni o'rnating
4. Botni ishga tushiring
5. Noutbukni o'chiring - Bot ishlaydi! ✅

---

**Vaqt:** 15 daqiqa  
**Qiyinlik:** Oson  
**Narx:** Bepul  
**Natija:** 24/7 ishlaydigan bot 🚀
