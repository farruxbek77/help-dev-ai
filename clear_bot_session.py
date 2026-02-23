import os
import requests
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Bot tokenini olish
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Telegram API orqali pending updatelarni tozalash
def clear_pending_updates():
    """Barcha pending updatelarni tozalash"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    
    try:
        # Barcha updatelarni olish
        response = requests.get(url, params={"offset": -1, "timeout": 1})
        data = response.json()
        
        if data.get("ok"):
            updates = data.get("result", [])
            if updates:
                last_update_id = updates[-1]["update_id"]
                # Oxirgi update_id + 1 bilan tozalash
                clear_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
                requests.get(clear_url, params={"offset": last_update_id + 1, "timeout": 1})
                print(f"✅ {len(updates)} ta pending update tozalandi!")
            else:
                print("✅ Pending updatelar yo'q")
        else:
            print(f"❌ Xatolik: {data.get('description')}")
    except Exception as e:
        print(f"❌ Xatolik: {e}")

if __name__ == "__main__":
    print("🧹 Bot sessiyasini tozalash...")
    clear_pending_updates()
    print("✅ Tayyor! Endi botni ishga tushiring: python bot.py")
