# config.py

"""
📄 config.py

Ce fichier contient les paramètres de configuration du bot Telegram Lucky Jet.

🔐 TOKEN : Clé d'accès au bot Telegram (à garder secrète)
👤 CHAT_ID : Identifiant Telegram de l'utilisateur cible
🌐 ENDPOINT_URL : Lien du site Lucky Jet à scraper
🧭 USER_AGENT : Identité du navigateur simulé pour le scraping

✅ Ce fichier est utilisé par main.py et luckyjet_scraper.py pour envoyer des alertes en temps réel.
🇨🇮 Fièrement développé en Côte d'Ivoire
🌟🌟🌟 Niveau : Trois étoiles de qualité
"""

# 🔐 Ton token Telegram (garde-le secret)
TOKEN = "8265254011:AAF1KPCHDBVNG4P4XG78PQwYmz9NZ8jhlXc"

# 👤 Ton ID Telegram
CHAT_ID = 8364289022

# 🌐 Lien du site Lucky Jet sur 1Win
ENDPOINT_URL = "https://1winbet.ci/lucky-jet/"

# 🧭 User-Agent pour simuler un navigateur
USER_AGENT = "Mozilla/5.0"
