import os
import time
from flask import Flask
from dotenv import load_dotenv
from bot.telegram_alerts import send_telegram_alert
from utils.luckyjet_scraper import get_luckyjet_data

# Chargement des variables d'environnement
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "Lucky Jet Bot is running!"

def run_bot():
    while True:
        try:
            data = get_luckyjet_data()
            if data:
                send_telegram_alert(TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, data)
            else:
                print("Pas de nouvelle donnée à envoyer.")
        except Exception as e:
            print(f"Erreur : {e}")
        time.sleep(30)  # exécute toutes les 30 secondes

if __name__ == '__main__':
    from threading import Thread
    bot_thread = Thread(target=run_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=5000)
