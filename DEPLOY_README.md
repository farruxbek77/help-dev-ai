# 🚀 Bot Deploy - Noutbuksiz 24/7 Ishlash

## 🎯 3 ta Oson Variant

---

## 1️⃣ PythonAnywhere (ENG OSON) ⭐

### Afzalliklari:
- ✅ 100% BEPUL
- ✅ 15 daqiqada sozlash
- ✅ Oson interface
- ✅ Python qo'llab-quvvatlaydi

### Qisqacha:
```
1. pythonanywhere.com → Sign up (FREE)
2. Files → Upload (bot.py, site_generator.py, .env)
3. Console → Bash
4. pip3 install --user python-telegram-bot python-dotenv
5. python3 bot.py
6. Noutbukni o'chiring - Bot ishlaydi! ✅
```

### Batafsil:
`PYTHONANYWHERE_SETUP.md` faylini o'qing

---

## 2️⃣ Render.com (GITHUB BILAN)

### Afzalliklari:
- ✅ Bepul
- ✅ GitHub integratsiya
- ✅ Avtomatik deploy

### Qisqacha:
```
1. GitHub'ga yuklang
2. render.com → Sign up
3. New Web Service → Connect GitHub
4. Environment: TELEGRAM_BOT_TOKEN
5. Deploy - Tayyor! ✅
```

---

## 3️⃣ Railway.app (ZAMONAVIY)

### Afzalliklari:
- ✅ $5/oy bepul kredit
- ✅ Yaxshi interface
- ✅ Tez deploy

### Qisqacha:
```
1. railway.app → Login with GitHub
2. New Project → Deploy from GitHub
3. Environment Variables → TELEGRAM_BOT_TOKEN
4. Avtomatik deploy - Tayyor! ✅
```

---

## 📁 Kerakli Fayllar

### requirements.txt
```txt
python-telegram-bot==20.7
python-dotenv==1.0.0
```

### .env
```env
TELEGRAM_BOT_TOKEN=sizning_tokeningiz
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

## 🎯 Qaysi Birini Tanlash?

| Variant | Qiyinlik | Vaqt | Narx | Tavsiya |
|---------|----------|------|------|---------|
| PythonAnywhere | Oson | 15 min | Bepul | ⭐⭐⭐⭐⭐ |
| Render | O'rta | 20 min | Bepul | ⭐⭐⭐⭐ |
| Railway | O'rta | 20 min | $5 kredit | ⭐⭐⭐⭐ |

---

## 🚀 Tezkor Boshlash

### PythonAnywhere (Tavsiya):

1. **Ro'yxatdan o'ting:**
   ```
   https://www.pythonanywhere.com/registration/register/beginner/
   ```

2. **Fayllarni yuklang:**
   - Dashboard → Files → Upload
   - bot.py, site_generator.py, .env

3. **Console ochib, yozing:**
   ```bash
   pip3 install --user python-telegram-bot python-dotenv
   python3 bot.py
   ```

4. **Tayyor!** Bot 24/7 ishlaydi! ✅

---

## 📊 Monitoring

### PythonAnywhere:
```bash
# Console'da
tail -f bot.log
ps aux | grep bot.py
```

### Render/Railway:
```
Dashboard → Logs
```

---

## 🔄 Yangilash

### PythonAnywhere:
```bash
# Eski botni to'xtatish
pkill -f bot.py

# Yangi fayllarni yuklash
# Files → Upload

# Yangi botni ishga tushirish
python3 bot.py
```

### Render/Railway:
```
GitHub'ga push qiling - Avtomatik yangilanadi
```

---

## 💡 Maslahatlar

1. **Log faylini yarating** - Xatoliklarni ko'rish uchun
2. **Restart script qo'shing** - Avtomatik qayta ishga tushirish
3. **Monitoring qiling** - Bot ishlayotganini tekshiring

---

## 🐛 Muammolar

### Bot to'xtab qolsa:

**PythonAnywhere:**
```bash
pkill -f bot.py
python3 bot.py
```

**Render/Railway:**
```
Dashboard → Restart
```

---

## 📞 Yordam

- `24_7_SERVER_DEPLOY.md` - Batafsil ko'rsatma
- `PYTHONANYWHERE_SETUP.md` - PythonAnywhere sozlash
- `web/HOSTING_24_7.md` - Web hosting

---

## ✅ Xulosa

**Eng oson va bepul:** PythonAnywhere

**Qadamlar:**
1. Ro'yxatdan o'ting (2 min)
2. Fayllarni yuklang (3 min)
3. Kutubxonalarni o'rnating (3 min)
4. Botni ishga tushiring (1 min)
5. Noutbukni o'chiring - Bot ishlaydi! ✅

**Jami vaqt:** 15 daqiqa  
**Narx:** Bepul  
**Natija:** 24/7 ishlaydigan bot 🚀

---

**Hoziroq boshlang:** https://www.pythonanywhere.com
