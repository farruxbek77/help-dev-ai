# 🧪 Bot Test Qilish - Pro Max

## ✅ Bot Ishga Tushdi!

Bot endi to'g'ri ishlaydi va quyidagi tartibda so'raydi:

## 📝 Test Jarayoni

### 1. Botni Oching
Telegram'da botingizni oching

### 2. Sayt Yaratishni Boshlang
```
/create_site
```

### 3. Qadamma-qadam

#### ✅ Qadam 1: Sayt Turi
```
Bot so'raydi: Qanday turdagi sayt?
Siz yuboring: 2 (Portfolio sayt)
```

#### ✅ Qadam 2: Sayt Nomi
```
Bot so'raydi: Sayt nomini kiriting
Siz yuboring: Shohruhbek Portfolio
```

#### ✅ Qadam 3: Rang
```
Bot so'raydi: Asosiy rangni kiriting
Siz yuboring: pro max dizaynidagi rang
```

#### ✅ Qadam 4: 1-RASM 📸
```
Bot so'raydi: 1-RASMNI yuboring
Siz: 📎 → Gallery → Rasm tanlang → Yuboring
```

**MUHIM:** Agar matn yuborsangiz, bot qabul qilmaydi va qaytadan rasm so'raydi!

#### ✅ Qadam 5: 2-RASM 📸
```
Bot so'raydi: 2-RASMNI yuboring
Siz: 📎 → Gallery → Rasm tanlang → Yuboring
```

**MUHIM:** Agar matn yuborsangiz, bot qabul qilmaydi va qaytadan rasm so'raydi!

#### ✅ Qadam 6: Batafsil Tavsif (50+ so'z)
```
Bot so'raydi: BATAFSIL TAVSIF yozing (kamida 50 ta so'z)
Siz yuboring: Saytda qanday mazmun bo'lishini xohlaysiz? (qisqacha yozing):

qwertyuiopasdfghjklzxcvbnm, qwertyuiopasdfghjkl;
zxcvbnm.
```

**MUHIM:** Agar 50 ta so'zdan kam yozsangiz, bot:
```
⚠️ Juda qisqa! Siz 15 ta so'z yozdingiz.
❌ Yana 35 ta so'z kerak!
```

#### ✅ Qadam 7: Tayyor! 🎉
```
Bot yuboradi:
✅ Professional Premium saytingiz tayyor! 🎉

📝 Tur: Portfolio sayt
🎨 Rang: pro max dizaynidagi rang
📸 Rasmlar: 2 ta
📄 Tavsif: 52 ta so'z
💎 Dizayn: Pro Max Premium
```

## 🐛 Agar Muammo Bo'lsa

### Muammo: Bot rasm so'ramayapti
**Sabab:** Eski bot jarayoni hali ishlayapti
**Yechim:**
```bash
# Barcha python jarayonlarini to'xtatish
Get-Process python | Stop-Process -Force

# Botni qayta ishga tushirish
python bot.py
```

### Muammo: Matn yuborganimda rasm so'ramayapti
**Yechim:** Bu to'g'ri! Bot faqat RASM qabul qiladi. Matn yuborsangiz, bot qaytadan rasm so'raydi.

### Muammo: 50 ta so'z yozdim, lekin "juda qisqa" deyapti
**Sabab:** Bo'sh joylar va yangi qatorlar hisoblanmaydi
**Yechim:** Haqiqiy so'zlar sonini sanang:
```python
text = "sizning matningiz"
len(text.split())  # Bu so'zlar sonini beradi
```

## 📊 Kutilgan Natija

### Oldingi Versiya (Noto'g'ri):
```
1. Tur → 2. Nom → 3. Rang → 4. Tavsif → ✅ Tayyor
(Rasm so'ramadi ❌)
```

### Yangi Versiya (To'g'ri):
```
1. Tur → 2. Nom → 3. Rang → 4. Rasm1 → 5. Rasm2 → 6. Tavsif (50+) → ✅ Tayyor
(Hamma narsa so'raladi ✅)
```

## 🎯 Tekshirish Ro'yxati

- [ ] Bot `/create_site` buyrug'ini qabul qiladi
- [ ] Sayt turini so'raydi (1-5)
- [ ] Sayt nomini so'raydi
- [ ] Rangni so'raydi
- [ ] 1-rasmni so'raydi (matn qabul qilmaydi)
- [ ] 2-rasmni so'raydi (matn qabul qilmaydi)
- [ ] 50+ so'z tavsif so'raydi
- [ ] Agar kam yozilsa, qaytadan so'raydi
- [ ] Tayyor saytni HTML fayl sifatida yuboradi

## 🚀 Ishga Tushirish

```bash
# Bot ishga tushirish
python bot.py

# Natija:
# 🌟 Bot ishlayapti - Pro Max Edition! 💎
# ⭐ Xususiyatlar: 2 ta rasm + 50+ so'z tavsif
```

---

**Status:** ✅ Tuzatildi va test qilishga tayyor!
