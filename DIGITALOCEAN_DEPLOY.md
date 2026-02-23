# 🌊 DigitalOcean Deploy Qo'llanmasi

## 📋 Talab qilinadigan narsalar

- DigitalOcean akkaunt
- GitHub repository (sizda bor)
- Bank kartasi (DigitalOcean uchun)

---

## 🚀 1-USUL: DigitalOcean App Platform (Eng oson)

### Bosqich 1: DigitalOcean'ga kirish

1. https://www.digitalocean.com ga o'ting
2. "Sign Up" yoki "Log In" qiling
3. Bank kartangizni ulang (birinchi marta $200 kredit berishadi)

### Bosqich 2: App yaratish

1. Dashboard'da "Create" tugmasini bosing
2. "Apps" ni tanlang
3. "GitHub" ni tanlang
4. GitHub akkauntingizni ulang
5. Repository tanlang: `farruxbek77/help-dev`
6. Branch: `main`
7. "Next" bosing

### Bosqich 3: Sozlamalar

1. **Source Directory**: `web` deb yozing
2. **Build Command**: Bo'sh qoldiring (static site)
3. **Output Directory**: Bo'sh qoldiring
4. **Environment Variables**: Bo'sh qoldiring
5. "Next" bosing

### Bosqich 4: Plan tanlash

1. **Basic** plan tanlang
2. **Static Site** - $0/month (BEPUL!)
3. "Next" bosing

### Bosqich 5: Deploy

1. App nomini kiriting: `help-dev-bot`
2. Region: `New York` yoki `Frankfurt` (yaqin)
3. "Create Resources" bosing
4. 3-5 daqiqa kuting

### Bosqich 6: Tayyor!

Deploy tugagach:
- Sizga URL beriladi: `https://help-dev-bot-xxxxx.ondigitalocean.app`
- Saytingiz ishlaydi!
- Har safar GitHub'ga push qilsangiz, avtomatik yangilanadi

---

## 🖥️ 2-USUL: DigitalOcean Droplet (Server)

### Bosqich 1: Droplet yaratish

1. Dashboard'da "Create" → "Droplets"
2. **Image**: Ubuntu 22.04 LTS
3. **Plan**: Basic ($4/month)
4. **CPU**: Regular (1GB RAM)
5. **Datacenter**: Frankfurt yoki Amsterdam
6. **Authentication**: Password (parol yarating)
7. "Create Droplet" bosing

### Bosqich 2: Server'ga kirish

Terminal'da:
```bash
ssh root@your_droplet_ip
```

Parolni kiriting.

### Bosqich 3: Nginx o'rnatish

```bash
apt update
apt install nginx -y
systemctl start nginx
systemctl enable nginx
```

### Bosqich 4: Git o'rnatish va kod olish

```bash
apt install git -y
cd /var/www
git clone https://github.com/farruxbek77/help-dev.git
```

### Bosqich 5: Nginx sozlash

```bash
nano /etc/nginx/sites-available/help-dev
```

Quyidagini yozing:
```nginx
server {
    listen 80;
    server_name your_droplet_ip;
    
    root /var/www/help-dev/web;
    index index.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

`Ctrl + X`, keyin `Y`, keyin `Enter`

### Bosqich 6: Nginx'ni qayta ishga tushirish

```bash
ln -s /etc/nginx/sites-available/help-dev /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

### Bosqich 7: Tayyor!

Brauzerda: `http://your_droplet_ip`

---

## 🎯 Qaysi usulni tanlash?

### App Platform (1-usul) - TAVSIYA QILINADI ✅

**Afzalliklari:**
- ✅ BEPUL (Static site)
- ✅ Juda oson
- ✅ Avtomatik deploy (GitHub push)
- ✅ SSL sertifikat (HTTPS)
- ✅ CDN (tez yuklash)
- ✅ Server boshqarish kerak emas

**Kamchiliklari:**
- ❌ Faqat static saytlar uchun

### Droplet (2-usul)

**Afzalliklari:**
- ✅ To'liq nazorat
- ✅ Backend ham qo'shish mumkin
- ✅ Bot ham ishlatish mumkin

**Kamchiliklari:**
- ❌ $4/month to'lash kerak
- ❌ Server boshqarish kerak
- ❌ Qiyinroq

---

## 💡 Tavsiya

Sizning saytingiz uchun **App Platform (1-usul)** eng yaxshi variant:
- Bepul
- Oson
- Avtomatik yangilanadi
- Professional URL

---

## 🔄 Avtomatik Deploy

App Platform ishlatilsa:
1. Kodda o'zgartirish qiling
2. GitHub'ga push qiling: `git push`
3. DigitalOcean avtomatik deploy qiladi
4. 2-3 daqiqada sayt yangilanadi

---

## 📞 Yordam

Agar muammo bo'lsa:
1. DigitalOcean dashboard'da "Logs" ni tekshiring
2. Build xatolarini o'qing
3. GitHub repository to'g'ri tanlanganini tekshiring

---

## 🎉 Natija

Deploy tugagach:
- Professional URL: `https://help-dev-bot.ondigitalocean.app`
- 24/7 ishlaydi
- Tez yuklash
- Bepul SSL (HTTPS)
- Avtomatik yangilanish

**Omad!** 🚀
