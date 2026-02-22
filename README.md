# Telegram Bot

Oddiy Telegram bot loyihasi.

## O'rnatish

1. Python 3.8 yoki undan yuqori versiya kerak

2. Kerakli paketlarni o'rnating:
```bash
pip install -r requirements.txt
```

3. Bot Token oling:
   - Telegramda @BotFather ni toping
   - `/newbot` buyrug'ini yuboring
   - Bot uchun nom va foydalanuvchi nomini tanlang
   - Sizga berilgan tokenni nusxalang

4. `.env` faylini yarating:
```bash
copy .env.example .env
```

5. `.env` fayliga bot tokeningizni qo'shing:
```
TELEGRAM_BOT_TOKEN=sizning_bot_tokeningiz
```

## Ishga tushirish

```bash
python bot.py
```

## Imkoniyatlar

- `/start` - Botni ishga tushiradi va buyruqlarni ko'rsatadi
- `/help` - Yordam xabari
- `/info` - Foydalanuvchi va chat ma'lumotlari
- Yuborilgan xabarlarni qaytaradi

## Rivojlantirish

Botga yangi imkoniyatlar qo'shish uchun `bot.py` faylini tahrirlang.
