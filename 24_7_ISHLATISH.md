# Bot 24/7 Ishlatish - Terminal Kerak Emas

## Tezkor Boshlash

### 1. O'rnatish (Bir marta)
```
install_service.bat ni ikki marta bosing
```

Bot endi:
- ✅ Background'da ishlaydi
- ✅ Terminal kerak emas
- ✅ Windows yonilganda avtomatik ishga tushadi
- ✅ Xatolik bo'lsa avtomatik qayta ishga tushadi
- ✅ 24/7 ishlaydi

### 2. Boshqarish

**Botni to'xtatish:**
```
stop_service.bat
```

**Botni qayta ishga tushirish:**
```
start_service.vbs
```

**Bot holatini tekshirish:**
```
check_status.bat
```

**Service'ni o'chirish:**
```
uninstall_service.bat
```

## Qanday Ishlaydi?

1. `bot_service.py` - Botni doimo ishlab turadi
2. `start_service.vbs` - Botni yashirin rejimda ishga tushiradi
3. Windows Startup - Kompyuter yonilganda avtomatik ishga tushadi
4. Auto-restart - Xatolik bo'lsa 5 soniyada qayta ishga tushadi

## Loglar

Bot faoliyati `bot_service.log` faylida saqlanadi:
- Bot qachon ishga tushdi
- Xatoliklar
- Qayta ishga tushirish vaqtlari

Loglarni ko'rish:
```
notepad bot_service.log
```

Yoki:
```
check_status.bat
```

## Muammolarni Hal Qilish

### Bot ishlamasa:

1. **Token tekshirish:**
   - `.env` faylini oching
   - `TELEGRAM_BOT_TOKEN` to'g'ri ekanligini tekshiring

2. **Internet aloqasi:**
   - Internet ulanganligini tekshiring

3. **Python o'rnatilgan:**
   ```
   python3 --version
   ```

4. **Loglarni ko'ring:**
   ```
   check_status.bat
   ```

### Bot to'xtab qolsa:

1. `stop_service.bat` ni ishga tushiring
2. `start_service.vbs` ni ishga tushiring

### Kompyuter uxlasa:

Windows uxlash rejimini o'chiring:
1. Settings > System > Power & sleep
2. Sleep: Never
3. Screen: Never

## Fayllar

- `install_service.bat` - Service'ni o'rnatish
- `uninstall_service.bat` - Service'ni o'chirish
- `start_service.vbs` - Botni ishga tushirish
- `stop_service.bat` - Botni to'xtatish
- `check_status.bat` - Holatni tekshirish
- `bot_service.py` - Service dasturi
- `bot_service.log` - Log fayli

## Afzalliklari

✅ Terminal kerak emas
✅ Avtomatik ishga tushadi
✅ Avtomatik qayta ishga tushadi
✅ Background'da ishlaydi
✅ Loglar saqlanadi
✅ Oson boshqarish

## Cloud Hosting (Tavsiya)

Agar kompyuter doim yoniq bo'lmasa, cloud hosting ishlatish yaxshiroq:

1. **Render.com** (Bepul)
2. **Railway.app** (Bepul)
3. **Heroku** (Pullik)

Batafsil: `DEPLOY.md`
