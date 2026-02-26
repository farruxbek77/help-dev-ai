import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# .env faylini yuklash
load_dotenv()

# Bot tokenini olish
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Conversation states - PRO MAX VERSION
SITE_TYPE, SITE_NAME, SITE_COLOR, SITE_IMAGE1, SITE_IMAGE2, SITE_DESCRIPTION, CODE_TYPE = range(7)

# /start buyrug'i
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🌟 Assalomu aleykum! Professional Bot - Pro Max Edition! 💎\n\n'
        'Foydalanish mumkin bo\'lgan buyruqlar:\n'
        '/start - Botni ishga tushirish\n'
        '/help - Yordam xabari\n'
        '/info - Bot haqida ma\'lumot\n'
        '/create_site - Professional sayt yaratish (Pro Max)\n'
        '/codes - Kod namunalari\n'
        '/clear - Chatni tozalash\n\n'
        '⭐ Pro Max xususiyatlari:\n'
        '• 2 ta rasm yuklash\n'
        '• 50+ so\'zli batafsil tavsif\n'
        '• Premium dizayn\n'
        '• Professional kod'
    )

# /help buyrug'i
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '📚 Yordam menyusi - Pro Max Edition\n\n'
        '🌐 /create_site - Professional sayt yaratish:\n'
        '  • Sayt turini tanlang\n'
        '  • Nom va rang kiriting\n'
        '  • 2 ta rasm yuboring\n'
        '  • 50+ so\'zli tavsif yozing\n'
        '  • Premium sayt oling!\n\n'
        '💻 /codes - Kod namunalari\n'
        '🗑️ /clear - Chatni tozalash'
    )

# /info buyrug'i
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '💎 Bot ma\'lumotlari - Pro Max Edition\n\n'
        f'👤 Foydalanuvchi: {update.effective_user.first_name}\n'
        f'🆔 User ID: {update.effective_user.id}\n'
        f'💬 Chat ID: {update.effective_chat.id}\n\n'
        '⭐ Versiya: Pro Max 2.0\n'
        '🎨 Xususiyatlar: Premium dizayn, 2 ta rasm, 50+ so\'z'
    )


# /create_site buyrug'i - PRO MAX
async def create_site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🌐 Professional Sayt Yaratish - Pro Max Edition 💎\n\n'
        'Qanday turdagi sayt yaratmoqchisiz?\n\n'
        '1️⃣ Oddiy HTML sayt\n'
        '2️⃣ Portfolio sayt\n'
        '3️⃣ Blog sayt\n'
        '4️⃣ Biznes sayt\n'
        '5️⃣ Landing page\n\n'
        'Raqamni yuboring (1-5):\n\n'
        '⭐ Pro Max: 2 ta rasm + 50+ so\'z tavsif!'
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
        await update.message.reply_text('⚠️ Iltimos, 1-5 oralig\'ida raqam yuboring.')
        return SITE_TYPE
    
    context.user_data['site_type'] = site_types[choice]
    context.user_data['site_type_number'] = choice
    
    await update.message.reply_text(
        f'✅ {site_types[choice]} tanlandi!\n\n'
        '📝 Sayt nomini kiriting:\n'
        '(Masalan: Mening Biznesim, Portfolio, Blog va h.k.)\n\n'
        '⭐ Pro Max: Har bir sayt turi uchun:\n'
        '• 2 ta maxsus rasm\n'
        '• 50+ so\'zli batafsil tavsif'
    )
    return SITE_NAME

async def site_name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['site_name'] = update.message.text
    
    await update.message.reply_text(
        f'✅ Sayt nomi: {update.message.text}\n\n'
        '🎨 Sayt uchun asosiy rangni kiriting:\n\n'
        'Mavjud ranglar:\n'
        '• ko\'k, qizil, yashil\n'
        '• sariq, binafsha, qora\n'
        '• pushti, moviy, jigarrang\n\n'
        'Rangni yozing:'
    )
    return SITE_COLOR


async def site_color_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['site_color'] = update.message.text
    site_type = context.user_data['site_type']
    
    await update.message.reply_text(
        f'✅ Rang: {update.message.text}\n\n'
        f'📸 {site_type} uchun 1-RASMNI yuboring:\n\n'
        f'Bu rasm "{site_type}" ning asosiy rasmi bo\'ladi.\n\n'
        '💡 Qanday rasm yuborish kerak:\n'
        '• Oddiy HTML sayt → Logo yoki banner\n'
        '• Portfolio sayt → Sizning rasmingiz yoki logo\n'
        '• Blog sayt → Blog banner yoki mavzu rasmi\n'
        '• Biznes sayt → Kompaniya logo yoki ofis\n'
        '• Landing page → Mahsulot yoki xizmat rasmi\n\n'
        '📎 Rasm yuborish:\n'
        '1. 📎 (qisqich) belgisini bosing\n'
        '2. Gallery dan rasm tanlang\n'
        '3. Yuboring'
    )
    return SITE_IMAGE1

async def site_image1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo = update.message.photo[-1]
        context.user_data['image1_id'] = photo.file_id
        site_type = context.user_data['site_type']
        
        await update.message.reply_text(
            f'✅ 1-rasm qabul qilindi! 📸\n\n'
            f'📸 {site_type} uchun 2-RASMNI yuboring:\n\n'
            f'Bu rasm "{site_type}" ning qo\'shimcha ma\'lumoti uchun.\n\n'
            '💡 Qanday rasm yuborish kerak:\n'
            '• Oddiy HTML sayt → Qo\'shimcha banner yoki rasm\n'
            '• Portfolio sayt → Loyihalaringiz yoki ishlaringiz\n'
            '• Blog sayt → Maqola rasmi yoki content\n'
            '• Biznes sayt → Jamoa yoki xizmatlar rasmi\n'
            '• Landing page → Mahsulot detallar yoki foyda\n\n'
            '📎 Rasm yuborish:\n'
            '1. 📎 (qisqich) belgisini bosing\n'
            '2. Gallery dan rasm tanlang\n'
            '3. Yuboring'
        )
        return SITE_IMAGE2
    else:
        await update.message.reply_text(
            '⚠️ Iltimos, RASM yuboring!\n\n'
            'Rasm yuborish uchun:\n'
            '1. 📎 (qisqich) belgisini bosing\n'
            '2. Gallery/Galereyadan rasm tanlang\n'
            '3. Yuboring\n\n'
            '❌ Matn emas, RASM kerak!'
        )
        return SITE_IMAGE1


async def site_image2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo = update.message.photo[-1]
        context.user_data['image2_id'] = photo.file_id
        site_type = context.user_data['site_type']
        site_type_number = context.user_data['site_type_number']
        
        # Har bir sayt turi uchun maxsus ko'rsatmalar
        instructions = {
            '1': '''• Saytingiz nimaga bag'ishlangan
• Qanday ma'lumotlar bo'ladi
• Kimlar uchun mo'ljallangan
• Asosiy maqsad va vazifalar
• Bog'lanish ma'lumotlari''',
            
            '2': '''• O'zingiz haqingizda to'liq ma'lumot
• Qanday loyihalar ustida ishlagansiz
• Sizning ko'nikmalaringiz (skills)
• Tajribangiz va yutuqlaringiz
• Mijozlar uchun qanday foyda
• Bog'lanish ma'lumotlari (email, telefon)''',
            
            '3': '''• Blog nimaga bag'ishlangan
• Qanday mavzularda yozasiz
• Kimlar uchun foydali
• Qancha tez-tez yangilanadi
• Nima uchun sizning blogingizni o'qish kerak
• Obuna bo'lish imkoniyatlari''',
            
            '4': '''• Kompaniya nomi va tarixi
• Qanday xizmatlar taqdim etasiz
• Sizning afzalliklaringiz
• Nima uchun sizni tanlash kerak
• Mijozlar uchun qanday foyda
• Jamoa haqida ma'lumot
• Bog'lanish: telefon, email, manzil''',
            
            '5': '''• Mahsulot yoki xizmat nomi
• Asosiy xususiyatlari va afzalliklari
• Kimlar uchun mo'ljallangan
• Qanday muammoni hal qiladi
• Narx va to'lov shartlari
• Nima uchun aynan bu mahsulot
• Qanday buyurtma berish mumkin'''
        }
        
        await update.message.reply_text(
            f'✅ 2-rasm qabul qilindi! 📸\n\n'
            f'📝 Endi "{site_type}" uchun BATAFSIL TAVSIF yozing:\n\n'
            f'⚠️ MUHIM: Kamida 50 ta so\'z yozing!\n\n'
            f'💡 {site_type} uchun yozish kerak:\n'
            f'{instructions[site_type_number]}\n\n'
            f'🎯 Qanchalik ko\'p va batafsil yozsangiz,\n'
            f'sayt shunchalik professional bo\'ladi!\n\n'
            f'Boshlang:'
        )
        return SITE_DESCRIPTION
    else:
        await update.message.reply_text(
            '⚠️ Iltimos, RASM yuboring!\n\n'
            'Rasm yuborish uchun:\n'
            '1. 📎 (qisqich) belgisini bosing\n'
            '2. Gallery/Galereyadan rasm tanlang\n'
            '3. Yuboring\n\n'
            '❌ Matn emas, RASM kerak!'
        )
        return SITE_IMAGE2


async def site_description_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    description = update.message.text
    word_count = len(description.split())
    site_type = context.user_data['site_type']
    
    if word_count < 50:
        await update.message.reply_text(
            f'⚠️ Juda qisqa! Siz {word_count} ta so\'z yozdingiz.\n\n'
            f'❌ Yana {50 - word_count} ta so\'z kerak!\n\n'
            f'💡 "{site_type}" uchun qo\'shimcha yozing:\n'
            f'• Batafsil ma\'lumot (10-15 so\'z)\n'
            f'• Xizmatlar ro\'yxati (10-15 so\'z)\n'
            f'• Afzalliklar va foyda (10-15 so\'z)\n'
            f'• Bog\'lanish ma\'lumotlari (5-10 so\'z)\n\n'
            f'📝 Qaytadan yozing (kamida 50 ta so\'z):'
        )
        return SITE_DESCRIPTION
    
    context.user_data['site_description'] = description
    
    await update.message.reply_text(
        f'✅ Ajoyib! {word_count} ta so\'z qabul qilindi! 🎉\n\n'
        f'⏳ "{site_type}" uchun Professional Premium sayt yaratilmoqda...\n'
        f'🎨 Pro Max dizayn qo\'llanmoqda...\n'
        f'📸 2 ta rasm joylashtirilmoqda...\n'
        f'💎 Premium kod yozilmoqda...\n'
        f'✨ Maxsus animatsiyalar qo\'shilmoqda...\n\n'
        f'Iltimos, 10-15 soniya kuting...'
    )
    
    # Sayt yaratish
    await create_premium_site(update, context)
    
    return ConversationHandler.END


async def create_premium_site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Pro Max sayt yaratish funksiyasi"""
    from site_generator import generate_html
    
    site_type = context.user_data['site_type']
    site_name = context.user_data['site_name']
    site_color = context.user_data['site_color']
    site_description = context.user_data['site_description']
    image1_id = context.user_data.get('image1_id', '')
    image2_id = context.user_data.get('image2_id', '')
    
    # Rasmlarni yuklab olish
    try:
        file1 = await context.bot.get_file(image1_id)
        file2 = await context.bot.get_file(image2_id)
        image1_url = file1.file_path
        image2_url = file2.file_path
    except:
        image1_url = "https://via.placeholder.com/600x400/7c3aed/ffffff?text=Rasm+1"
        image2_url = "https://via.placeholder.com/500x400/7c3aed/ffffff?text=Rasm+2"
    
    # HTML kod yaratish
    html_code = generate_html(site_name, site_type, site_color, site_description, image1_url, image2_url)
    
    # Faylni saqlash
    filename = f"{site_name.replace(' ', '_')}_ProMax.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_code)
    
    # Faylni yuborish
    word_count = len(site_description.split())
    with open(filename, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=filename,
            caption=f'✅ Professional Premium saytingiz tayyor! 🎉\n\n'
                    f'📝 Tur: {site_type}\n'
                    f'🎨 Rang: {site_color}\n'
                    f'📸 Rasmlar: 2 ta\n'
                    f'📄 Tavsif: {word_count} ta so\'z\n'
                    f'💎 Dizayn: Pro Max Premium\n\n'
                    f'⭐ Faylni yuklab oling va brauzerda oching!\n'
                    f'🌐 Professional saytingizdan foydalaning!'
        )
    
    # Faylni o'chirish
    os.remove(filename)


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

// Map
const ikkilangan = sonlar.map(son => son * 2);
console.log(ikkilangan); // [2, 4, 6, 8, 10]

// Filter
const juftlar = sonlar.filter(son => son % 2 === 0);
console.log(juftlar); // [2, 4]

// Reduce
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
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover { transform: scale(1.1); }
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
}'''),
        
        '5': ('C++', '''// C++ - Vektor
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> sonlar = {1, 2, 3, 4, 5};
    sonlar.push_back(6);
    
    for(int son : sonlar) {
        cout << son << " ";
    }
    return 0;
}''')
    }
    
    if choice not in code_examples:
        await update.message.reply_text('⚠️ Iltimos, 1-5 oralig\'ida raqam yuboring.')
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

# /clear buyrug'i
async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '✅ Chat tozalandi!\n\n'
        '💡 Eslatma: Bot faqat o\'zi yuborgan xabarlarni o\'chira oladi.'
    )

# Xabar ishlovchisi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f'Siz aytdingiz: {user_message}')

# Xatolik ishlovchisi
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Xatolik: {context.error}')


def main():
    """Bot ishga tushirish - Pro Max Edition"""
    from keep_alive import keep_alive
    keep_alive()  # Bot uxlamasligi uchun
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # /create_site conversation handler - PRO MAX
    site_conv = ConversationHandler(
        entry_points=[CommandHandler('create_site', create_site)],
        states={
            SITE_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_type_handler)],
            SITE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_name_handler)],
            SITE_COLOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_color_handler)],
            SITE_IMAGE1: [MessageHandler(filters.PHOTO, site_image1_handler)],
            SITE_IMAGE2: [MessageHandler(filters.PHOTO, site_image2_handler)],
            SITE_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, site_description_handler)],
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
    
    # MUHIM: Conversation handlerlar birinchi bo'lishi kerak!
    app.add_handler(site_conv)
    app.add_handler(codes_conv)
    
    # Xabar ishlovchisi (eng oxirida)
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Xatolik ishlovchisi
    app.add_error_handler(error_handler)
    
    # Botni ishga tushirish
    print('🌟 Bot ishlayapti - Pro Max Edition! 💎')
    print('⭐ Xususiyatlar: 2 ta rasm + 50+ so\'z tavsif')
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
