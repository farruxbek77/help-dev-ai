# Telegram Bot - Ishlatish Yo'riqnomasi

## 1. Oddiy Ishga Tushirish

### Usul 1: Oynali rejim
- `start_bot.bat` ni ikki marta bosing
- Oyna ochiladi va bot ishlaydi
- Oynani yopmasdan qoldiring

### Usul 2: Yashirin rejim (tavsiya)
- `start_bot_hidden.vbs` ni ikki marta bosing
- Bot background'da ishlaydi
- Hech qanday oyna ochilmaydi

## 2. Avtomatik Ishga Tushirish

### O'rnatish:
1. `install_startup.bat` ni ikki marta bosing
2. Bot Windows yonilganda avtomatik ishga tushadi

### O'chirish:
1. `uninstall_startup.bat` ni ikki marta bosing
2. Avtomatik ishga tushirish o'chiriladi

## 3. Botni To'xtatish

### Agar oynali rejimda:
- Oynani yoping yoki Ctrl+C bosing

### Agar yashirin rejimda:
1. Task Manager ni oching (Ctrl+Shift+Esc)
2. "Details" tabiga o'ting
3. "python3.exe" ni toping
4. O'ng tugma > "End task"

Yoki:
```bash
taskkill /F /IM python3.exe
```

## 4. Botni Tekshirish

Bot ishlayotganini tekshirish:
1. Task Manager > Details
2. "python3.exe" jarayonini qidiring
3. Agar bor bo'lsa - bot ishlayapti

## 5. Muammolarni Hal Qilish

### Bot ishlamasa:
1. `.env` faylida token to'g'ri ekanligini tekshiring
2. Internet aloqasi borligini tekshiring
3. `python3 bot.py` buyrug'i bilan xatoliklarni ko'ring

### Bot to'xtab qolsa:
1. `start_bot_hidden.vbs` ni qayta ishga tushiring
2. Yoki `keep_alive.py` dan foydalaning

## 6. 24/7 Ishlash

### Kompyuterda:
1. `install_startup.bat` ni ishga tushiring
2. Kompyuterni uxlatish rejimini o'chiring:
   - Settings > System > Power & sleep
   - Sleep: Never

### Cloud serverda (tavsiya):
- Render.com, Railway.app yoki Heroku'da deploy qiling
- Batafsil: `DEPLOY.md` faylida

## Fayllar

- `start_bot.bat` - Oynali rejimda ishga tushirish
- `start_bot_hidden.vbs` - Yashirin rejimda ishga tushirish
- `install_startup.bat` - Avtomatik ishga tushirishni o'rnatish
- `uninstall_startup.bat` - Avtomatik ishga tushirishni o'chirish
- `keep_alive.py` - Botni doimo ishlab turish
- `run_bot.bat` - Qayta ishga tushirish bilan

## Yordam

Muammo bo'lsa:
1. `python3 bot.py` bilan xatoliklarni ko'ring
2. `.env` faylini tekshiring
3. Internet aloqasini tekshiring
