# Bot - Terminal Kerak Emas!

## 🚀 Tezkor Ishga Tushirish

### Usul 1: Yashirin Rejim (Eng Oson)
```
start_bot_hidden.vbs ni ikki marta bosing
```
- ✅ Terminal ochilmaydi
- ✅ Bot background'da ishlaydi
- ✅ Hech narsa ko'rinmaydi

### Usul 2: Avtomatik Ishga Tushirish (Tavsiya)
```
install_service.bat ni ikki marta bosing
```
- ✅ Windows yonilganda avtomatik ishga tushadi
- ✅ Terminal kerak emas
- ✅ Xatolik bo'lsa avtomatik qayta ishga tushadi
- ✅ 24/7 ishlaydi

## 📋 Boshqarish

### Botni To'xtatish
```
stop_service.bat
```

### Botni Qayta Ishga Tushirish
```
restart_bot.bat
```

### Holatni Tekshirish
```
check_status.bat
```

### Avtomatik Ishga Tushirishni O'chirish
```
uninstall_service.bat
```

## ✅ Qaysi Usulni Tanlash?

### Agar kompyuter doim yoniq bo'lsa:
👉 `install_service.bat` - Eng yaxshi variant!
- Windows yonilganda avtomatik ishga tushadi
- Xatolik bo'lsa qayta ishga tushadi
- Terminal kerak emas

### Agar vaqti-vaqti bilan ishlatmoqchi bo'lsangiz:
👉 `start_bot_hidden.vbs` - Oddiy variant
- Ikki marta bosing
- Bot ishlaydi
- Terminal yo'q

## 🔍 Bot Ishlayaptimi?

1. `check_status.bat` ni ishga tushiring
2. Yoki Task Manager'da (Ctrl+Shift+Esc) "python.exe" ni qidiring

## 📝 Loglar

Bot faoliyati `bot_service.log` faylida saqlanadi.

Ko'rish:
```
notepad bot_service.log
```

## ⚠️ Muammolar

### Bot ishlamasa:
1. `.env` faylida token to'g'ri ekanligini tekshiring
2. Internet aloqasi borligini tekshiring
3. `check_status.bat` bilan holatni tekshiring

### Bot to'xtab qolsa:
1. `stop_service.bat` ni ishga tushiring
2. `start_bot_hidden.vbs` ni ishga tushiring

## 🎯 Xulosa

Terminal kerak emas! Faqat:
1. `install_service.bat` - bir marta ishga tushiring
2. Bot doimo ishlaydi
3. Hech qanday terminal ochilmaydi

Hammasi! 🎉
