# 🚀 Render.com - Eng Oson Deploy (5 daqiqa)

## ✅ Nima Uchun Render?

- ✅ Juda oson
- ✅ GitHub bilan ishlaydi
- ✅ Avtomatik deploy
- ✅ Bepul
- ✅ 5 daqiqada tayyor

---

## 📝 Qadamlar

### 1️⃣ GitHub'ga Yuklash (Agar yo'q bo'lsa)

Noutbukda PowerShell'da:

```powershell
cd C:\Users\555\Desktop\Bot

# Git init
git init
git add .
git commit -m "Bot deploy"

# GitHub'ga yuklash (agar repository bor bo'lsa)
git remote add origin https://github.com/username/bot.git
git push -u origin main
```

---

### 2️⃣ Render.com'ga Kirish

1. **Saytga kiring:**
   ```
   https://render.com
   ```

2. **"Get Started for Free" bosing**

3. **"Sign up with GitHub" bosing**

4. **GitHub'ga ruxsat bering**

---

### 3️⃣ New Web Service

1. **Dashboard → "New +" → "Web Service"**

2. **"Connect GitHub repository"**

3. **Bot repository'ni tanlang**

---

### 4️⃣ Sozlamalar

**Name:** `telegram-bot`

**Environment:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
python bot.py
```

---

### 5️⃣ Environment Variables

**"Add Environment Variable" bosing:**

**Key:** `TELEGRAM_BOT_TOKEN`

**Value:** `8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0`

---

### 6️⃣ Deploy

**"Create Web Service" bosing**

Render avtomatik deploy qiladi (2-3 daqiqa).

---

### 7️⃣ Tayyor!

Bot ishlaydi! Noutbukni o'chiring - Bot ishlaydi! ✅

---

## 🎯 Agar GitHub Yo'q Bo'lsa

### GitHub Repository Yaratish:

1. **github.com'ga kiring**
2. **"New repository" bosing**
3. **Nom: `telegram-bot`**
4. **"Create repository" bosing**

Keyin yuqoridagi git buyruqlarini yozing.

---

## ⚠️ Muhim

`requirements.txt` faylini yarating:

```txt
python-telegram-bot==20.7
python-dotenv==1.0.0
```

`.gitignore` faylini yarating:

```
.env
__pycache__/
*.pyc
```

`.env` faylini GitHub'ga yuklamang! Faqat Render'da Environment Variable sifatida qo'shing.

---

## 🔄 Yangilash

GitHub'ga push qiling - Render avtomatik yangilanadi:

```powershell
git add .
git commit -m "Update"
git push
```

---

**Vaqt:** 5 daqiqa  
**Qiyinlik:** Oson  
**Natija:** Noutbuk o'chiq bo'lsa ham bot ishlaydi! ✅
