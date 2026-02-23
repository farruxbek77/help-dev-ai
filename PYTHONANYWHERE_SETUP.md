# 🐍 PythonAnywhere - Tezkor Sozlash

## 🎯 Noutbukni O'chirganda Ham Bot Ishlashi

---

## 📝 Qadamma-qadam (15 daqiqa)

### 1️⃣ Ro'yxatdan O'tish (2 daqiqa)

1. **Saytga kiring:**
   ```
   https://www.pythonanywhere.com
   ```

2. **Sign up bosing**

3. **Beginner account tanlang** (BEPUL)

4. **Ma'lumotlarni kiriting:**
   - Username
   - Email
   - Password

5. **Email'ni tasdiqlang**

---

### 2️⃣ Fayllarni Yuklash (3 daqiqa)

1. **Dashboard → Files**

2. **Upload a file bosing**

3. **Quyidagi fayllarni yuklang:**
   - `bot.py`
   - `site_generator.py`
   - `requirements.txt`
   - `.env`

4. **Yoki ZIP qilib yuklang:**
   ```
   Barcha fayllarni ZIP ga qo'ying
   Upload qiling
   Unzip qiling
   ```

---

### 3️⃣ Console Ochish (1 daqiqa)

1. **Dashboard → Consoles**

2. **Bash bosing**

3. **Yangi console ochiladi**

---

### 4️⃣ Kutubxonalarni O'rnatish (3 daqiqa)

Console'da yozing:

```bash
# Papkaga o'tish
cd mysite  # yoki sizning papkangiz

# Kutubxonalarni o'rnatish
pip3 install --user python-telegram-bot python-dotenv

# Tekshirish
python3 --version
```

---

### 5️⃣ .env Faylini Yaratish (2 daqiqa)

```bash
# .env faylini yaratish
nano .env
```

Ichiga yozing:
```env
TELEGRAM_BOT_TOKEN=8307658680:AAG5RbMpRtyx22daOi8Iw5d78nqKJe3mzV0
```

**Saqlash:**
- `Ctrl + X`
- `Y` (Yes)
- `Enter`

---

### 6️⃣ Botni Ishga Tushirish (1 daqiqa)

```bash
# Botni ishga tushirish
python3 bot.py
```

**Natija:**
```
🌟 Bot ishlayapti - Pro Max Edition! 💎
⭐ Xususiyatlar: 2 ta rasm + 50+ so'z tavsif
```

---

### 7️⃣ Background'da Ishlashi (3 daqiqa)

#### Variant 1: Screen (Oddiy)

```bash
# Screen yaratish
screen -S bot

# Botni ishga tushirish
python3 bot.py

# Screen'dan chiqish (bot ishlaydi)
Ctrl + A, keyin D

# Screen'ga qaytish
screen -r bot
```

#### Variant 2: nohup (Oson)

```bash
# Background'da ishga tushirish
nohup python3 bot.py > bot.log 2>&1 &

# Jarayonni ko'rish
ps aux | grep bot.py

# Log'ni ko'rish
tail -f bot.log
```

---

## 🔄 Avtomatik Restart

### Always-On Task (Pullik)

Bepul versiyada yo'q, lekin Cron job qo'shish mumkin.

### Cron Job Qo'shish

1. **Dashboard → Tasks**

2. **Add a new scheduled task**

3. **Command:**
   ```bash
   /home/username/mysite/restart_bot.sh
   ```

4. **Time:** `00:00` (har kuni)

### restart_bot.sh yaratish

```bash
nano restart_bot.sh
```

Ichiga:
```bash
#!/bin/bash
pkill -f bot.py
cd /home/username/mysite
python3 bot.py > bot.log 2>&1 &
```

Executable qilish:
```bash
chmod +x restart_bot.sh
```

---

## 🧪 Test Qilish

### 1. Telegram'da test qiling:
```
/start
/create_site
```

### 2. Noutbukni o'chiring

### 3. Telefondan test qiling:
```
/start
/create_site
```

### 4. Bot ishlayotganini tekshiring! ✅

---

## 📊 Monitoring

### Botni tekshirish:

```bash
# Jarayonni ko'rish
ps aux | grep bot.py

# Log'ni ko'rish
tail -f bot.log

# Xotira ishlatilishi
free -h
```

---

## 🛑 Botni To'xtatish

```bash
# Jarayonni topish
ps aux | grep bot.py

# To'xtatish
kill -9 <process_id>

# Yoki
pkill -f bot.py
```

---

## 🔄 Botni Yangilash

### 1. Yangi fayllarni yuklash:
```
Dashboard → Files → Upload
```

### 2. Eski botni to'xtatish:
```bash
pkill -f bot.py
```

### 3. Yangi botni ishga tushirish:
```bash
python3 bot.py
```

---

## 💡 Maslahatlar

### 1. Log Faylini Yaratish

`bot.py` ga qo'shing:
```python
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 2. Xatoliklarni Tutish

```python
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'Xatolik: {context.error}')
```

### 3. Restart Script

```bash
#!/bin/bash
while true; do
    python3 bot.py
    echo "Bot to'xtadi, 5 soniyadan keyin qayta ishga tushadi..."
    sleep 5
done
```

---

## 🐛 Muammolarni Hal Qilish

### Bot ishlamayapti:

```bash
# Log'ni tekshirish
cat bot.log

# Python versiyasini tekshirish
python3 --version

# Kutubxonalarni tekshirish
pip3 list | grep telegram
```

### "No module named 'telegram'":

```bash
pip3 install --user python-telegram-bot
```

### "Permission denied":

```bash
chmod +x bot.py
```

---

## 📞 Yordam

### PythonAnywhere Support:
```
Dashboard → Help → Forums
```

### Telegram Bot API:
```
https://core.telegram.org/bots/api
```

---

## ✅ Xulosa

**Endi botingiz 24/7 ishlaydi!**

- ✅ Noutbukni o'chirishingiz mumkin
- ✅ Bot serverda ishlaydi
- ✅ Bepul
- ✅ Ishonchli

---

**Vaqt:** 15 daqiqa  
**Qiyinlik:** Oson  
**Narx:** Bepul  
**Natija:** 24/7 ishlaydigan bot 🚀
