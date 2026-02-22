# Saytni Ochish Yo'riqnomasi

## Usul 1: To'g'ridan-to'g'ri ochish (Eng oson)

1. `web` papkasiga kiring
2. `index.html` faylini ikki marta bosing
3. Brauzer avtomatik ochiladi

## Usul 2: Local server bilan (Tavsiya etiladi)

### Python bilan:
```bash
cd web
python -m http.server 8000
```

Keyin brauzerda: http://localhost:8000

### Node.js bilan (agar o'rnatilgan bo'lsa):
```bash
cd web
npx serve
```

## Usul 3: VS Code Live Server

1. VS Code'da `web/index.html` ni oching
2. O'ng tugmani bosing
3. "Open with Live Server" ni tanlang

## Muammolar va Yechimlar

### Agar sayt ko'rinmasa:
1. `style.css` va `script.js` fayllar bir xil papkada ekanligini tekshiring
2. Brauzer cache'ini tozalang (Ctrl+Shift+Delete)
3. Brauzer konsolini oching (F12) va xatoliklarni ko'ring

### Agar ranglar ko'rinmasa:
1. `style.css` fayli to'g'ri yuklanganligini tekshiring
2. Brauzerda F12 bosib, Network tabini tekshiring

### Agar animatsiyalar ishlamasa:
1. `script.js` fayli to'g'ri yuklanganligini tekshiring
2. Brauzer konsolida JavaScript xatoliklari borligini tekshiring

## Fayllar tuzilishi

```
web/
├── index.html      (Asosiy sahifa)
├── style.css       (Dizayn)
├── script.js       (Animatsiyalar)
├── README.md       (Umumiy ma'lumot)
└── OCHISH.md       (Bu fayl)
```

## Yordam

Agar muammo bo'lsa:
1. Barcha fayllar bir papkada ekanligini tekshiring
2. Fayl nomlarini tekshiring (katta-kichik harflar muhim!)
3. Brauzer konsolini tekshiring (F12)

Sayt ishlashi kerak! 🎉
