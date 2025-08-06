import requests
import os

def send_telegram_alert(message):
    """
    Envoie une alerte Telegram avec le message fourni.

    Args:
        message (str): Le message à envoyer.
    """
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("Erreur : TOKEN ou CHAT_ID manquant.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Erreur d'envoi : {response.text}")
        else:
            print("✅ Message Telegram envoyé avec succès.")
    except Exception as e:
        print(f"❌ Exception lors de l'envoi du message : {e}")
