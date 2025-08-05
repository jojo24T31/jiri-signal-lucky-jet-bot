import requests
from bs4 import BeautifulSoup

def fetch_luckyjet_data(endpoint_url, user_agent):
    headers = {"User-Agent": user_agent}
    response = requests.get(endpoint_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # 🔍 À adapter selon la structure HTML du site Lucky Jet
        data = soup.find("div", class_="lucky-data")
        return data.text.strip() if data else None
    else:
        print("❌ Erreur de scraping :", response.status_code)
        return None
