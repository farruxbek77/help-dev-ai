# 🚀 Replit - Qisqa Qo'llanma (3 Daqiqa)

## ✅ Tayyor Fayllar

Sizning kompyuteringizda endi quyidagi fayllar tayyor:

- ✅ `bot.py` (keep_alive qo'shilgan)
- ✅ `site_generator.py`
- ✅ `keep_alive.py` (yangi)
- ✅ `requirements.txt` (flask qo'shilgan)
- ✅ `.env`

---

## 📝 3 Daqiqada Qilish Kerak

### 1️⃣ Replit'ga Kiring (30 soniya)

**Brauzer ochildi:** https://replit.com

1. **"Sign up"** bosing
2. **Google** bilan kiring (tezroq)
3. Yoki email bilan ro'yxatdan o'ting

---

### 2️⃣ Yangi Repl Yaratish (30 soniya)

1. **"+ Create Repl"** bosing
2. **Template:** "Python" tanlang
3. **Title:** `telegram-bot-24-7`
4. **"Create Repl"** bosing

---

### 3️⃣ Fayllarni Yuklash (1 daqiqa)

**Replit'da chap tarafda "Files" bo'limi:**

#### Variant A: Drag & Drop (Eng Oson)

1. **Windows Explorer'da** `C:\Users\555\Desktop\Bot` papkasini oching
2. **Quyidagi fayllarni** Replit'ga sudrab tashlang:
   - `bot.py`
   - `site_generator.py`
   - `keep_alive.py`
   - `requirements.txt`
   - `.env`

#### Variant B: Qo'lda Yaratish

**Har bir fayl uchun:**

1. **"+" belgisini** bosing
2. **Fayl nomini** yozing (masalan: `bot.py`)
3. **Faylni oching** (Windows'da)
4. **Kodni ko'chiring** (Ctrl+A, Ctrl+C)
5. **Replit'ga joylashtiring** (Ctrl+V)
6. **Ctrl+S** bosing (saqlash)

---

### 4️⃣ Botni Ishga Tushirish (1 daqiqa)

1. **Yuqorida "Run" tugmasini** bosing (yashil tugma)
2. **Kutubxonalar o'rnatiladi** (1-2 daqiqa)
3. **Console'da ko'rasiz:**
   ```
   🌟 Bot ishlayapti - Pro Max Edition! 💎
   ```

**✅ Bot ishlayapti!**

---

### 5️⃣ UptimeRobot Sozlash (1 daqiqa)

**Bot uxlamasligi uchun:**

1. **Yangi tab oching:** https://uptimerobot.com
2. **"Sign Up Free"** bosing
3. **Email bilan ro'yxatdan o'ting**
4. **"Add New Monitor"** bosing
5. **Sozlamalar:**
   - **Monitor Type:** HTTP(s)
   - **Friendly Name:** Telegram Bot
   - **URL:** Replit'dagi URL (yuqorida ko'rsatiladi)
     - Masalan: `https://telegram-bot-24-7.username.repl.co`
   - **Monitoring Interval:** 5 minutes
6. **"Create Monitor"** bosing

**✅ Bot har 5 daqiqada ping oladi va uxlamaydi!**

---

## 🎉 Tayyor!

**Bot endi 24/7 ishlaydi!**

### Test Qiling:

1. **Telegram'da** botingizni oching
2. **/start** yuboring
3. **Bot javob berishi kerak**
4. **Replit'ni yoping**
5. **5 daqiqa kuting**
6. **Yana /start yuboring**
7. **Bot javob bersa - muvaffaqiyat!** 🎉

---

## 📊 Replit'da URL Topish

**Bot URL'ini topish uchun:**

1. **Replit'da "Run" bosganingizdan keyin**
2. **Yuqorida "Webview" oynasi ochiladi**
3. **URL ko'rsatiladi:**
   ```
   https://telegram-bot-24-7.username.repl.co
   ```
4. **Bu URL'ni UptimeRobot'ga kiriting**

---

## 🐛 Muammolar

### "Module not found"?

**Yechim:** `requirements.txt` to'g'ri yaratilganini tekshiring:
```txt
python-telegram-bot==21.0
python-dotenv==1.0.0
flask==3.0.0
```

### Bot javob bermayapti?

**Yechim:** 
1. Replit'da Console'ni tekshiring
2. Qizil xatoliklarni o'qing
3. Token to'g'ri kiritilganini tekshiring

### Bot uxlab qoladi?

**Yechim:**
1. `keep_alive.py` yaratilganini tekshiring
2. `bot.py`'da `keep_alive()` chaqirilganini tekshiring
3. UptimeRobot sozlanganini tekshiring

---

## 💡 Maslahatlar

### 1. Replit'da Secrets Ishlatish

**.env o'rniga (xavfsizroq):**

1. **Chap tarafda "Tools" → "Secrets"**
2. **"New Secret"** bosing
3. **Key:** `TELEGRAM_BOT_TOKEN`
4. **Value:** `8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0`
5. **"Add Secret"** bosing

**bot.py'da:**
```python
import os
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
```

### 2. Log'larni Ko'rish

**Replit'da:**
- **Console** - Bot loglarini ko'rish
- **Webview** - Keep-alive sahifasini ko'rish

### 3. Botni To'xtatish

**"Stop" tugmasini** bosing (yuqorida)

---

## 📞 Yordam

**Agar biror narsa ishlamasa:**

1. **Console'dagi xatoliklarni o'qing**
2. **Fayllarni qayta tekshiring**
3. **Menga yozing:** @FrontendBackendUz

---

## ✅ Xulosa

**3 daqiqada bot 24/7 ishlaydi!**

1. ✅ Replit'ga kiring
2. ✅ Yangi Repl yarating
3. ✅ Fayllarni yuklang
4. ✅ "Run" bosing
5. ✅ UptimeRobot sozlang
6. ✅ Noutbukni o'chiring - Bot ishlaydi! 🚀

**Omad!** 🍀
