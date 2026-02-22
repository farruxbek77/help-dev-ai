import os
import sys
import time
import subprocess
import logging
from pathlib import Path

# Logging sozlash
log_file = Path(__file__).parent / 'bot_service.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def run_bot():
    """Botni ishga tushirish va xatolik bo'lsa qayta ishga tushirish"""
    bot_path = Path(__file__).parent / 'bot.py'
    
    while True:
        try:
            logging.info("Bot ishga tushirilmoqda...")
            
            # Botni ishga tushirish
            process = subprocess.Popen(
                [sys.executable, str(bot_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            
            logging.info(f"Bot ishga tushdi (PID: {process.pid})")
            
            # Bot to'xtagunga qadar kutish
            stdout, stderr = process.communicate()
            
            if stdout:
                logging.info(f"Bot output: {stdout}")
            if stderr:
                logging.error(f"Bot error: {stderr}")
            
            # Agar bot to'xtasa
            if process.returncode != 0:
                logging.error(f"Bot xatolik bilan to'xtadi (kod: {process.returncode})")
            else:
                logging.info("Bot normal to'xtadi")
            
            # 5 soniya kutib qayta ishga tushirish
            logging.info("5 soniyadan keyin qayta ishga tushiriladi...")
            time.sleep(5)
            
        except KeyboardInterrupt:
            logging.info("Bot to'xtatildi (Ctrl+C)")
            break
        except Exception as e:
            logging.error(f"Kutilmagan xatolik: {e}")
            logging.info("10 soniyadan keyin qayta urinish...")
            time.sleep(10)

if __name__ == '__main__':
    logging.info("=" * 50)
    logging.info("Bot Service ishga tushdi")
    logging.info("=" * 50)
    run_bot()
