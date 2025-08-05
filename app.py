from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

# Charger les variables d'environnement depuis .env
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)

# Variables d'environnement
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Route principale (accueil)
@app.route('/')
def home():
    return "Lucky Jet Bot est en ligne 🚀"

# Exemple de route pour recevoir des données
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # 🔐 Ici tu peux traiter les données et envoyer une alerte
    print("Données reçues :", data)
    return "OK", 200

# Lancer l'app Flask
if __name__ == "__main__":
    app.run(debug=True)
