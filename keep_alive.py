import subprocess
import time
import sys

def run_bot():
    """Botni ishga tushirish va xatolik bo'lsa qayta ishga tushirish"""
    while True:
        try:
            print("Bot ishga tushirilmoqda...")
            process = subprocess.Popen([sys.executable, "bot.py"])
            process.wait()
            
            print("Bot to'xtadi. 5 soniyadan keyin qayta ishga tushadi...")
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\nBot to'xtatildi.")
            process.terminate()
            break
        except Exception as e:
            print(f"Xatolik: {e}")
            print("5 soniyadan keyin qayta urinish...")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
