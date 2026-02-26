# Google Search Console Verification

## Saytni Google ga tezroq qo'shish

### 1-usul: HTML meta tag (Eng oson)

Google Search Console dan olingan meta tegni `web/index.html` ga qo'shing:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
  <!-- Google Search Console Verification -->
  <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE" />
  
  <!-- SEO Meta Tags -->
  ...
</head>
```

### 2-usul: HTML fayl yuklash

1. Google Search Console dan HTML fayl yuklab oling
2. Faylni `web/` papkasiga joylashtiring
3. Netlify ga deploy qiling
4. Google da "Verify" tugmasini bosing

### 3-usul: DNS record (Agar domeningiz bo'lsa)

1. Google Search Console dan TXT record ni oling
2. Domain provider da (Namecheap, GoDaddy, va h.k.) DNS sozlamalariga o'ting
3. TXT record qo'shing:
   ```
   Type: TXT
   Host: @
   Value: google-site-verification=XXXXXXXXXX
   ```
4. 1-2 soat kuting
5. Google da "Verify" tugmasini bosing

## Sitemap yuklash

Verification qilingandan keyin:

1. Google Search Console da "Sitemaps" bo'limiga o'ting
2. Sitemap URL ni kiriting: `https://your-site.netlify.app/sitemap.xml`
3. "Submit" tugmasini bosing

## URL Inspection - Tezkor indekslash

1. Google Search Console da "URL Inspection" ga o'ting
2. Sayt URL ni kiriting: `https://your-site.netlify.app`
3. "Request indexing" tugmasini bosing
4. Har bir muhim sahifa uchun takrorlang

## Monitoring

Google Search Console da kuzatish:
- **Performance**: Qancha kishi saytingizni ko'rdi
- **Coverage**: Qancha sahifa indekslandi
- **Enhancements**: Mobil va desktop ko'rinish
- **Links**: Kimlar saytingizga havola berdi

## Tezlashtirish uchun qo'shimcha:

### 1. Google My Business (Agar biznes bo'lsa)
- [https://www.google.com/business/](https://www.google.com/business/)
- Biznes profilini yarating
- Sayt havolasini qo'shing

### 2. Social Media Signals
- Facebook Page yarating
- Instagram profil yarating
- LinkedIn company page yarating
- Barcha joyda sayt havolasini ulashing

### 3. Backlinks
- Telegram kanalda e'lon qiling
- Forum va blog commentlarda havola qoldiring
- Guest posting qiling
- Directory saytlarga qo'shing

### 4. Content Marketing
- Blog yozuvlari yozing
- Video yarating (YouTube)
- Infographic yarating
- Case study yozing

## Natijalarni kuzatish

Har hafta tekshiring:
- Google Search Console - Performance
- Google Analytics - Traffic
- Keyword pozitsiyalari
- Backlink soni

**Sabr qiling!** SEO - bu uzoq muddatli strategiya. 2-3 oy ichida yaxshi natijalar ko'rasiz.
