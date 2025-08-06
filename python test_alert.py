# test_alert.py
# Ce fichier permet de tester l'envoi d'une alerte Telegram via la fonction send_alert du fichier alert.py.
# Il vérifie que le bot peut envoyer un message correctement.

from alert import send_alert

# Test simple
send_alert("🚨 Test d'alerte depuis test_alert.py")
