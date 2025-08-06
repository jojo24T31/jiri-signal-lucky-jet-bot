from dotenv import load_dotenv
from alert import send_telegram_alert
from scraper import get_luckyjet_data
import os
import time
from flask import Flask

# Variables d'environnement
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)

@app.route("/")
def home():
    return "Lucky Jet Bot is running!"

def run_bot():
    print("Bot is running!")
    while True:
        try:
            data = get_luckyjet_data()
            if data:
                send_telegram_alert(TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, data)
            else:
                print("Pas de nouvelle donnée")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(30)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(threaded=True, port=5000)
