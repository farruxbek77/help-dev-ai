# 💎 Premium To'lov Tizimi - Sozlash va Test

## 📁 Yaratilgan Fayllar

1. **payment.html** - To'lov sahifasi (paketlar va forma)
2. **payment.js** - To'lov logikasi
3. **premium.html** - Premium xizmatlar sahifasi (faqat to'lovdan keyin)
4. **premium-check.js** - Kirish tekshirish tizimi
5. **test-premium-button.html** - Test sahifasi

## 🔗 Havolalar Tuzilishi

```
index.html (Premium bo'limi)
    ↓
    [Premium'ga o'tish] → payment.html
    ↓
    To'lov amalga oshiriladi
    ↓
    premium.html (faqat to'lovdan keyin kirish mumkin)
```

## ✅ To'g'ri Ishlashini Tekshirish

### 1. Test Sahifasini Oching
```
web/test-premium-button.html
```
Bu sahifada tugmani bosing va `payment.html` ga o'tishni tekshiring.

### 2. Asosiy Sahifani Tekshirish
```
web/index.html
```
Pastga scroll qiling → "Premium xizmat" bo'limini toping → "Premium'ga o'tish" tugmasini bosing

### 3. Agar Hali Ham Botga O'tsa

**Brauzer keshini tozalang:**

#### Chrome/Edge:
1. `Ctrl + Shift + Delete` bosing
2. "Cached images and files" ni tanlang
3. "Clear data" bosing
4. Yoki: `Ctrl + F5` (hard refresh)

#### Firefox:
1. `Ctrl + Shift + Delete` bosing
2. "Cache" ni tanlang
3. "Clear Now" bosing

#### Yoki oddiy yo'l:
Sahifani ochib, `Ctrl + F5` bosing (hard refresh)

## 🔍 Kod Tekshirish

### index.html da Premium tugmasi:
```html
<a href="payment.html" class="btn-primary">Premium'ga o'tish</a>
```

✅ To'g'ri - `payment.html` ga yo'naltirilgan
❌ Noto'g'ri - `https://t.me/helpdev_ai_bot` ga yo'naltirilgan

### Agar noto'g'ri bo'lsa:
1. Faylni qayta yuklang
2. Brauzer keshini tozalang
3. Sahifani yangilang

## 🧪 To'liq Test Jarayoni

### 1. Boshlash
```
web/index.html → Premium bo'limi → "Premium'ga o'tish"
```

### 2. To'lov Sahifasi
```
payment.html → Paket tanlash → Ma'lumot kiritish → To'lash
```

### 3. Premium Sahifa
```
premium.html → Faqat to'lovdan keyin kirish mumkin
```

### 4. Tekshirish
- Premium sahifaga to'lovsiz kirishga harakat qiling
- Avtomatik `payment.html` ga qaytarilishingiz kerak

## 💾 localStorage Ma'lumotlari

To'lovdan keyin saqlanadigan ma'lumot:
```javascript
{
  telegram: "@username",
  phone: "+998901234567",
  plan: "monthly",
  activatedAt: "2024-02-22T10:00:00.000Z",
  expiresAt: "2024-03-22T10:00:00.000Z"
}
```

### localStorage ni ko'rish:
1. Brauzerda `F12` bosing
2. "Console" tabiga o'ting
3. Quyidagini yozing:
```javascript
localStorage.getItem('premiumUser')
```

### localStorage ni tozalash:
```javascript
localStorage.removeItem('premiumUser')
```

## 🚀 Ishga Tushirish

1. `web/index.html` ni brauzerda oching
2. Pastga scroll qiling
3. "Premium'ga o'tish" tugmasini bosing
4. Paket tanlang va to'lovni amalga oshiring
5. Premium sahifaga kiring

## ⚠️ Muhim Eslatmalar

1. **Demo versiya** - To'lov aslida amalga oshirilmaydi
2. **localStorage** - Ma'lumotlar faqat brauzerda saqlanadi
3. **Real loyiha** uchun backend server kerak bo'ladi
4. **Xavfsizlik** - Real loyihada JWT token va encryption kerak

## 🐛 Muammolarni Hal Qilish

### Muammo: Tugma botga yo'naltiradi
**Yechim:**
1. Brauzer keshini tozalang (`Ctrl + Shift + Delete`)
2. Sahifani hard refresh qiling (`Ctrl + F5`)
3. `test-premium-button.html` ni sinab ko'ring

### Muammo: Premium sahifa ochilmaydi
**Yechim:**
1. Avval to'lov qiling (`payment.html`)
2. localStorage da ma'lumot borligini tekshiring
3. Muddat tugaganligini tekshiring

### Muammo: To'lov formasi ko'rinmaydi
**Yechim:**
1. Paketni tanlang (Oylik yoki Yillik)
2. JavaScript xatolarini tekshiring (F12 → Console)

## 📞 Yordam

Agar muammo hal bo'lmasa:
1. Browser console ni tekshiring (F12)
2. Network tabini tekshiring
3. Fayllar to'g'ri joylashganligini tekshiring

---

**Yaratilgan sana:** 2024-02-22
**Versiya:** 1.0
