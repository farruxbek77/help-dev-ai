import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# .env faylini yuklash
load_dotenv()

# Bot tokenini olish
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Conversation states
SITE_TYPE, SITE_NAME, SITE_COLOR, SITE_CONTENT, CODE_TYPE, CODE_EXAMPLE = range(6)

# /start buyrug'i
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Assalomu aleykum! Men Telegram botiman. 🤖\n\n'
        'Foydalanish mumkin bo\'lgan buyruqlar:\n'
        '/start - Botni ishga tushirish\n'
        '/help - Yordam xabari\n'
        '/info - Bot haqida ma\'lumot\n'
        '/create_site - Veb-sayt yaratish\n'
        '/codes - Kod namunalari\n'
        '/clear - Chatni tozalash'
    )

# /help buyrug'i
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Yordam menyusi:\n\n'
        'Menga xabar yuborishingiz yoki buyruqlardan foydalanishingiz mumkin.\n'
        'Yuborgan xabarlaringizni qaytarib yuboraman.'
    )

# /info buyrug'i
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Bot ma\'lumotlari:\n'
        f'Foydalanuvchi: {update.effective_user.first_name}\n'
        f'Foydalanuvchi ID: {update.effective_user.id}\n'
        f'Chat ID: {update.effective_chat.id}'
    )

# /create_site buyrug'i
async def create_site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🌐 Veb-sayt yaratish\n\n'
        'Qanday turdagi sayt yaratmoqchisiz?\n\n'
        '1️⃣ Oddiy HTML sayt\n'
        '2️⃣ Portfolio sayt\n'
        '3️⃣ Blog sayt\n'
        '4️⃣ Biznes sayt\n'
        '5️⃣ Landing page\n\n'
        'Raqamni yuboring (1-5):'
    )
    return SITE_TYPE

async def site_type_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    
    site_types = {
        '1': 'Oddiy HTML sayt',
        '2': 'Portfolio sayt',
        '3': 'Blog sayt',
        '4': 'Biznes sayt',
        '5': 'Landing page'
    }
    
    if choice not in site_types:
        await update.message.reply_text('Iltimos, 1-5 oralig\'ida raqam yuboring.')
        return SITE_TYPE
    
    context.user_data['site_type'] = site_types[choice]
    
    await update.message.reply_text(
        f'✅ {site_types[choice]} tanlandi!\n\n'
        'Sayt nomini kiriting:'
    )
    return SITE_NAME

async def site_name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['site_name'] = update.message.text
    
    await update.message.reply_text(
        f'✅ Sayt nomi: {update.message.text}\n\n'
        'Sayt uchun asosiy rangni kiriting (masalan: ko\'k, qizil, yashil):'
    )
    return SITE_COLOR

async def site_color_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['site_color'] = update.message.text
    
    await update.message.reply_text(
        f'✅ Rang: {update.message.text}\n\n'
        'Saytda qanday mazmun bo\'lishini xohlaysiz? (qisqacha yozing):'
    )
    return SITE_CONTENT

async def site_content_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['site_content'] = update.message.text
    
    # Sayt yaratish
    site_type = context.user_data['site_type']
    site_name = context.user_data['site_name']
    site_color = context.user_data['site_color']
    site_content = context.user_data['site_content']
    
    await update.message.reply_text('⏳ Professional sayt yaratilmoqda...')
    
    # Rangni CSS formatiga o'tkazish
    color_map = {
        'ko\'k': '#3498db', 'qizil': '#e74c3c', 'yashil': '#2ecc71',
        'sariq': '#f39c12', 'binafsha': '#7c3aed', 'qora': '#2c3e50',
        'oq': '#ecf0f1', 'pushti': '#ff69b4', 'to\'q ko\'k': '#1e40af'
    }
    main_color = color_map.get(site_color.lower(), '#7c3aed')
    
    # Professional HTML kod yaratish - Bustshop.uz stilida
    html_code = f'''<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --primary: {main_color};
            --primary-light: #a78bfa;
            --primary-dark: #6d28d9;
            --bg-dark: #0a0118;
            --bg-card: rgba(124, 58, 237, 0.08);
            --border: rgba(167, 139, 250, 0.15);
            --text-light: #e2e8f0;
            --text-gray: #94a3b8;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text-light);
            background: var(--bg-dark);
            overflow-x: hidden;
        }}
        
        /* Navbar */
        .navbar {{
            background: rgba(10, 1, 24, 0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 1.2rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid var(--border);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}
        
        .navbar .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary-light) 0%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }}
        
        .nav-links {{
            display: flex;
            list-style: none;
            gap: 2.5rem;
        }}
        
        .nav-links a {{
            color: #cbd5e1;
            text-decoration: none;
            transition: color 0.3s;
            font-weight: 500;
            font-size: 0.95rem;
        }}
        
        .nav-links a:hover {{
            color: var(--primary);
        }}
        
        /* Hero Section */
        .hero {{
            background: radial-gradient(ellipse at top, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
                        radial-gradient(ellipse at bottom, rgba(192, 132, 252, 0.1) 0%, transparent 50%),
                        var(--bg-dark);
            padding: 160px 0 100px;
            text-align: center;
            min-height: 85vh;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }}
        
        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(90deg, transparent 0%, rgba(124, 58, 237, 0.03) 50%, transparent 100%),
                linear-gradient(0deg, transparent 0%, rgba(192, 132, 252, 0.03) 50%, transparent 100%);
            pointer-events: none;
        }}
        
        .hero .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            position: relative;
            z-index: 1;
        }}
        
        .hero-title {{
            font-size: 5rem;
            font-weight: 900;
            margin-bottom: 2rem;
            background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 50%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -3px;
            line-height: 1;
            animation: fadeInUp 0.8s ease;
        }}
        
        .hero-subtitle {{
            font-size: 1.5rem;
            color: var(--text-gray);
            margin-bottom: 3rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.8;
            animation: fadeInUp 0.8s ease 0.2s both;
        }}
        
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 18px 56px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 40px rgba(124, 58, 237, 0.5);
            border: 1px solid rgba(167, 139, 250, 0.3);
            letter-spacing: 0.3px;
            animation: fadeInUp 0.8s ease 0.4s both;
        }}
        
        .btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(124, 58, 237, 0.7);
            background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
        }}
        
        /* Stats */
        .stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3rem;
            margin-top: 5rem;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .stat-item {{
            text-align: center;
            padding: 2.5rem 2rem;
            background: var(--bg-card);
            border-radius: 20px;
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            transition: all 0.3s;
            animation: fadeInUp 0.8s ease 0.6s both;
        }}
        
        .stat-item:hover {{
            background: rgba(124, 58, 237, 0.12);
            border-color: rgba(167, 139, 250, 0.4);
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(124, 58, 237, 0.3);
        }}
        
        .stat-item h3 {{
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            color: var(--primary-light);
            font-weight: 900;
            letter-spacing: -1px;
        }}
        
        .stat-item p {{
            color: #cbd5e1;
            font-size: 1.1rem;
            font-weight: 500;
        }}
        
        /* Features Section */
        .features {{
            padding: 100px 0;
            background: rgba(15, 10, 31, 0.5);
        }}
        
        .section-title {{
            text-align: center;
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #ffffff;
            font-weight: 800;
            letter-spacing: -1px;
        }}
        
        .section-subtitle {{
            text-align: center;
            font-size: 1.25rem;
            color: var(--text-gray);
            margin-bottom: 4rem;
        }}
        
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        .feature-card {{
            background: var(--bg-card);
            padding: 2.5rem;
            border-radius: 20px;
            text-align: center;
            border: 1px solid var(--border);
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }}
        
        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--primary-light));
            transform: scaleX(0);
            transition: transform 0.3s;
        }}
        
        .feature-card:hover::before {{
            transform: scaleX(1);
        }}
        
        .feature-card:hover {{
            transform: translateY(-8px);
            background: rgba(124, 58, 237, 0.12);
            border-color: rgba(167, 139, 250, 0.3);
            box-shadow: 0 20px 60px rgba(124, 58, 237, 0.2);
        }}
        
        .feature-icon {{
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            filter: drop-shadow(0 4px 10px rgba(124, 58, 237, 0.3));
        }}
        
        .feature-card h3 {{
            margin-bottom: 1rem;
            color: #ffffff;
            font-size: 1.4rem;
            font-weight: 700;
        }}
        
        .feature-card p {{
            color: var(--text-gray);
            line-height: 1.7;
        }}
        
        /* Footer */
        footer {{
            background: rgba(10, 1, 24, 0.8);
            color: white;
            padding: 3rem 0 1.5rem;
            border-top: 1px solid var(--border);
            text-align: center;
        }}
        
        footer p {{
            color: #64748b;
        }}
        
        /* Animations */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .hero {{
                min-height: auto;
                padding: 120px 0 60px;
            }}
            
            .hero-title {{
                font-size: 2.8rem;
                letter-spacing: -1.5px;
            }}
            
            .hero-subtitle {{
                font-size: 1.1rem;
            }}
            
            .btn {{
                padding: 16px 40px;
                font-size: 1rem;
            }}
            
            .stats {{
                grid-template-columns: 1fr;
                gap: 2rem;
            }}
            
            .stat-item h3 {{
                font-size: 2.8rem;
            }}
            
            .nav-links {{
                display: none;
            }}
            
            .features-grid {{
                grid-template-columns: 1fr;
            }}
            
            .section-title {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">{site_name}</div>
            <ul class="nav-links">
                <li><a href="#home">Bosh sahifa</a></li>
                <li><a href="#features">Xizmatlar</a></li>
                <li><a href="#contact">Aloqa</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero" id="home">
        <div class="container">
            <h1 class="hero-title">{site_name}</h1>
            <p class="hero-subtitle">{site_content}</p>
            <a href="#features" class="btn">Batafsil ma'lumot</a>
            
            <div class="stats">
                <div class="stat-item">
                    <h3>100+</h3>
                    <p>Mijozlar</p>
                </div>
                <div class="stat-item">
                    <h3>500+</h3>
                    <p>Loyihalar</p>
                </div>
                <div class="stat-item">
                    <h3>24/7</h3>
                    <p>Yordam</p>
                </div>
            </div>
        </div>
    </section>

    <section class="features" id="features">
        <div class="container">
            <h2 class="section-title">Bizning xizmatlar</h2>
            <p class="section-subtitle">{site_type}</p>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Tez va Sifatli</h3>
                    <p>Professional xizmatlar yuqori sifatda va tez vaqt ichida taqdim etiladi</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h3>Zamonaviy Dizayn</h3>
                    <p>Eng so'nggi texnologiyalar va dizayn trendlaridan foydalaniladi</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔒</div>
                    <h3>Xavfsiz va Ishonchli</h3>
                    <p>100% xavfsiz va ishonchli xizmat ko'rsatishga kafolatimiz bor</p>
                </div>
            </div>
        </div>
    </section>

    <footer id="contact">
        <div class="container">
            <p>&copy; 2024 {site_name}. Barcha huquqlar himoyalangan.</p>
        </div>
    </footer>
</body>
</html>'''
    
    # Faylni saqlash
    filename = f"{site_name.replace(' ', '_')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_code)
    
    # Faylni yuborish
    with open(filename, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=filename,
            caption=f'✅ Professional saytingiz tayyor!\n\n'
                    f'📝 Tur: {site_type}\n'
                    f'🎨 Rang: {site_color}\n'
                    f'💎 Dizayn: Premium Pro\n\n'
                    f'Faylni yuklab oling va brauzerda oching!'
        )
    
    # Faylni o'chirish
    os.remove(filename)
    
    return ConversationHandler.END

# /codes buyrug'i
async def codes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '💻 Kod namunalari\n\n'
        'Qaysi tildagi kod kerak?\n\n'
        '1️⃣ Python\n'
        '2️⃣ JavaScript\n'
        '3️⃣ HTML/CSS\n'
        '4️⃣ Java\n'
        '5️⃣ C++\n\n'
        'Raqamni yuboring (1-5):'
    )
    return CODE_TYPE

async def code_type_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    
    code_examples = {
        '1': ('Python', '''# Python - Oddiy kalkulyator
def kalkulyator():
    print("Oddiy Kalkulyator")
    a = float(input("Birinchi son: "))
    b = float(input("Ikkinchi son: "))
    
    print(f"Qo'shish: {a + b}")
    print(f"Ayirish: {a - b}")
    print(f"Ko'paytirish: {a * b}")
    print(f"Bo'lish: {a / b}")

kalkulyator()'''),
        
        '2': ('JavaScript', '''// JavaScript - Array metodlari
const sonlar = [1, 2, 3, 4, 5];

// Map - har bir elementni o'zgartirish
const ikkilangan = sonlar.map(son => son * 2);
console.log(ikkilangan); // [2, 4, 6, 8, 10]

// Filter - shartga mos elementlar
const juftlar = sonlar.filter(son => son % 2 === 0);
console.log(juftlar); // [2, 4]

// Reduce - yig'indi
const yigindi = sonlar.reduce((sum, son) => sum + son, 0);
console.log(yigindi); // 15'''),
        
        '3': ('HTML/CSS', '''<!-- HTML/CSS - Tugma dizayni -->
<!DOCTYPE html>
<html>
<head>
    <style>
        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.3s;
        }
        .btn:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <button class="btn">Bosing</button>
</body>
</html>'''),
        
        '4': ('Java', '''// Java - Oddiy sinf
public class Talaba {
    private String ism;
    private int yosh;
    
    public Talaba(String ism, int yosh) {
        this.ism = ism;
        this.yosh = yosh;
    }
    
    public void malumot() {
        System.out.println("Ism: " + ism);
        System.out.println("Yosh: " + yosh);
    }
    
    public static void main(String[] args) {
        Talaba t = new Talaba("Ali", 20);
        t.malumot();
    }
}'''),
        
        '5': ('C++', '''// C++ - Vektor bilan ishlash
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> sonlar = {1, 2, 3, 4, 5};
    
    // Element qo'shish
    sonlar.push_back(6);
    
    // Elementlarni chiqarish
    for(int son : sonlar) {
        cout << son << " ";
    }
    
    return 0;
}''')
    }
    
    if choice not in code_examples:
        await update.message.reply_text('Iltimos, 1-5 oralig\'ida raqam yuboring.')
        return CODE_TYPE
    
    lang, code = code_examples[choice]
    
    await update.message.reply_text(
        f'💻 {lang} kod namunasi:\n\n'
        f'```\n{code}\n```',
        parse_mode='Markdown'
    )
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('❌ Bekor qilindi.')
    return ConversationHandler.END

# /clear buyrug'i - Chatni tozalash
async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    
    try:
        # Oxirgi 100 ta xabarni o'chirish
        deleted_count = 0
        for i in range(message_id, max(0, message_id - 100), -1):
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=i)
                deleted_count += 1
            except Exception:
                # Xabar topilmasa yoki o'chirib bo'lmasa, davom etamiz
                continue
        
        # Tasdiq xabari (3 soniyadan keyin o'chadi)
        confirm_msg = await update.message.reply_text(
            f'✅ {deleted_count} ta xabar o\'chirildi!\n\n'
            'Bu xabar 3 soniyadan keyin o\'chadi...'
        )
        
        # 3 soniya kutib, tasdiq xabarini ham o'chirish
        import asyncio
        await asyncio.sleep(3)
        await confirm_msg.delete()
        
    except Exception as e:
        await update.message.reply_text(
            '⚠️ Ba\'zi xabarlarni o\'chirib bo\'lmadi.\n\n'
            'Sabab: Bot faqat o\'zi yuborgan xabarlarni o\'chira oladi.\n'
            'Guruh chatlarida admin huquqlari kerak.'
        )

# Xabar ishlovchisi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f'Siz aytdingiz: {user_message}')

# Xatolik ishlovchisi
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Xatolik yuz berdi: {context.error}')

def main():
    # Bot ilovasini yaratish
    app = Application.builder().token(BOT_TOKEN).build()
    
    # /create_site conversation handler
    site_conv = ConversationHandler(
        entry_points=[CommandHandler('create_site', create_site)],
        states={
            SITE_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_type_handler)],
            SITE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_name_handler)],
            SITE_COLOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_color_handler)],
            SITE_CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_content_handler)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    # /codes conversation handler
    codes_conv = ConversationHandler(
        entry_points=[CommandHandler('codes', codes)],
        states={
            CODE_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, code_type_handler)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    # Buyruq ishlovchilari
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('clear', clear_chat))
    app.add_handler(site_conv)
    app.add_handler(codes_conv)
    
    # Xabar ishlovchisi
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Xatolik ishlovchisi
    app.add_error_handler(error_handler)
    
    # Botni ishga tushirish
    print('Bot ishlayapti...')
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
