# Netlify ga Deploy qilish - Tezkor qo'llanma

## 1-usul: Netlify orqali (Eng oson - 5 daqiqa)

### Qadamlar:

1. **Netlify ga kiring:**
   - [https://app.netlify.com/](https://app.netlify.com/) ga o'ting
   - GitHub akkaunt bilan kiring

2. **Yangi sayt qo'shing:**
   - "Add new site" tugmasini bosing
   - "Import an existing project" ni tanlang

3. **GitHub repository ni ulang:**
   - "Deploy with GitHub" ni tanlang
   - Repository ni tanlang: `help-dev-ai`
   - Branch: `main`

4. **Build sozlamalari:**
   ```
   Base directory: web
   Build command: (bo'sh qoldiring)
   Publish directory: .
   ```

5. **Deploy qiling:**
   - "Deploy site" tugmasini bosing
   - 1-2 daqiqada tayyor bo'ladi

6. **Domain sozlang:**
   - Site settings > Domain management
   - "Add custom domain" tugmasini bosing
   - `helpdeveloper.uz` ni kiriting (agar domeningiz bo'lsa)
   - Yoki Netlify ning bepul subdomenidan foydalaning: `your-site-name.netlify.app`

## 2-usul: Netlify CLI orqali

```bash
# Netlify CLI o'rnatish
npm install -g netlify-cli

# Login qilish
netlify login

# Deploy qilish
cd web
netlify deploy --prod
```

## 3-usul: Vercel (Alternativa)

1. [https://vercel.com/](https://vercel.com/) ga kiring
2. "Add New Project" tugmasini bosing
3. GitHub repository ni import qiling
4. Root Directory: `web`
5. Deploy tugmasini bosing

## Deploy qilingandan keyin:

### 1. Google Search Console ga qo'shing

1. [https://search.google.com/search-console](https://search.google.com/search-console) ga kiring
2. "Add property" tugmasini bosing
3. Sayt URL ni kiriting: `https://your-site.netlify.app`
4. Tasdiqlash usulini tanlang:
   - HTML file (Netlify ga yuklang)
   - HTML tag (index.html ga qo'shing)
   - DNS record (Domain sozlamalarida)

5. Sitemap yuklang:
   - Sitemaps bo'limiga o'ting
   - `https://your-site.netlify.app/sitemap.xml` ni qo'shing

### 2. Bing Webmaster Tools

1. [https://www.bing.com/webmasters](https://www.bing.com/webmasters) ga kiring
2. Saytni qo'shing
3. Sitemap yuklang

### 3. Google Analytics (Ixtiyoriy)

1. [https://analytics.google.com/](https://analytics.google.com/) ga kiring
2. Yangi property yarating
3. Tracking code ni oling
4. `web/index.html` ga qo'shing (</head> dan oldin):

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## Kutilayotgan natijalar:

- **1-3 kun**: Google saytni topadi
- **1-2 hafta**: Indekslash boshlanadi
- **2-4 hafta**: "Help Developer" qidiruvi bo'yicha ko'rinadi
- **1-3 oy**: TOP 10 ga kiradi
- **3-6 oy**: TOP 3 ga kiradi

## Tezlashtirish uchun:

1. **Google Search Console da URL Inspection:**
   - Sayt URL ni kiriting
   - "Request indexing" tugmasini bosing

2. **Backlink yarating:**
   - Telegram kanalda sayt havolasini ulashing
   - Facebook, Instagram da e'lon qiling
   - Boshqa saytlarda havola qoldiring

3. **Kontent qo'shing:**
   - Blog bo'limi yarating
   - FAQ qo'shing
   - Video qo'shing

## Muammo yuzaga kelsa:

### Sayt ochilmayapti:
- Netlify build loglarini tekshiring
- Base directory to'g'ri ekanligini tekshiring: `web`

### Google indekslamayapti:
- robots.txt ni tekshiring
- Sitemap to'g'ri ekanligini tekshiring
- Google Search Console da xatolarni ko'ring

### SSL sertifikat xatosi:
- Netlify avtomatik SSL beradi
- 1-2 soat kuting

## Yordam kerak bo'lsa:

- Netlify Support: [https://www.netlify.com/support/](https://www.netlify.com/support/)
- Telegram: @FrontendBackendUz
- Bot: @helpdev_ai_bot

---

**Eslatma:** Sayt deploy qilingandan keyin, `web/index.html` dagi barcha `https://helpdeveloper.uz/` havolalarini o'z domeningizga o'zgartiring!
