import requests
import os
from dotenv import load_dotenv

# Charger la clé API Google Maps
load_dotenv()
cle_google = os.getenv("CLE_GOOGLE")

# Fonction pour récupérer un itinéraire
def obtenir_itineraire(depart="Paris", arrivee="Lyon", mode="driving"):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={depart}&destination={arrivee}&mode={mode}&key={cle_google}"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        donnees = reponse.json()
        if "routes" in donnees and donnees["routes"]:
            trajet = donnees["routes"][0]
            return {
                "distance": trajet["legs"][0]["distance"]["text"],
                "durée": trajet["legs"][0]["duration"]["text"],
                "instructions": [etape["html_instructions"] for etape in trajet["legs"][0]["steps"]]
            }
        else:
            return {"erreur": "Aucune route trouvée"}
    else:
        return {"erreur": "Impossible de récupérer les données"}

# Test
if __name__ == "__main__":
    print(obtenir_itineraire("Paris", "Lyon", mode="transit"))