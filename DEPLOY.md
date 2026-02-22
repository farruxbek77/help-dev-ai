# Botni 24/7 Ishlatish Yo'llari

## 1. Windows Task Scheduler (Kompyuteringizda)

### Qadamlar:
1. `Win + R` bosing va `taskschd.msc` yozing
2. "Create Basic Task" ni bosing
3. Nom: "Telegram Bot"
4. Trigger: "When the computer starts"
5. Action: "Start a program"
6. Program: `C:\Users\555\Desktop\Bot\run_bot.bat`
7. Finish

Kompyuter yonilganda bot avtomatik ishga tushadi.

## 2. Keep Alive Script (Hozir ishlatish)

Terminalda ishga tushiring:
```bash
python3 keep_alive.py
```

Bu script botni doimo ishlab turadi va xatolik bo'lsa qayta ishga tushiradi.

## 3. Bepul Cloud Hosting (Tavsiya etiladi)

### A) Render.com (Bepul)
1. https://render.com ga ro'yxatdan o'ting
2. "New Web Service" yarating
3. GitHub repo ulang
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python bot.py`

### B) Railway.app (Bepul)
1. https://railway.app ga kiring
2. "New Project" > "Deploy from GitHub"
3. Repo tanlang
4. Avtomatik deploy bo'ladi

### C) PythonAnywhere (Bepul)
1. https://pythonanywhere.com ga ro'yxatdan o'ting
2. Files > Upload files
3. Bash console ochib: `python3 bot.py`
4. "Always-on tasks" qo'shing

### D) Heroku (Pullik, lekin ishonchli)
1. https://heroku.com ga kiring
2. Yangi app yarating
3. GitHub bilan ulang
4. Deploy qiling

## 4. VPS Server (Professional)

### Arzon VPS provayderlar:
- Contabo: $4/oy
- DigitalOcean: $5/oy
- Vultr: $5/oy
- Hetzner: €4/oy

### VPS da o'rnatish:
```bash
# Serverga ulanish
ssh user@server_ip

# Fayllarni yuklash
git clone your_repo

# O'rnatish
cd Bot
pip3 install -r requirements.txt

# Screen bilan ishga tushirish
screen -S telegram_bot
python3 bot.py
# Ctrl+A+D bosib chiqish (bot ishlayveradi)

# Qaytib kirish
screen -r telegram_bot
```

## 5. Hozir Tezkor Ishlatish

Agar kompyuteringiz doim yoniq bo'lsa:

```bash
python3 keep_alive.py
```

Yoki:

```bash
run_bot.bat
```

Bu botni doimo ishlab turadi!

## Tavsiya

Eng yaxshi variant: **Render.com** yoki **Railway.app** - bepul va oson!
