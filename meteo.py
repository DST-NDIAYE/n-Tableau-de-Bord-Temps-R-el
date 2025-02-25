import requests
import os
from dotenv import load_dotenv

# Charger les clés API
load_dotenv()
cle_meteo = os.getenv("CLE_METEO")

# Fonction pour récupérer la météo
def obtenir_meteo(ville="Paris"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_meteo}&units=metric&lang=fr"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        donnees = reponse.json()
        return {
            "ville": donnees["name"],
            "température": donnees["main"]["temp"],
            "humidité": donnees["main"]["humidity"],
            "vent": donnees["wind"]["speed"],
            "conditions": donnees["weather"][0]["description"]
        }
    else:
        return {"erreur": "Impossible de récupérer les données météo"}

# Test
if __name__ == "__main__":
    print(obtenir_meteo("Paris"))