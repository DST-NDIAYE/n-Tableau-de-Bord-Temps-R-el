import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les clés API
cle_meteo = os.getenv("CLE_METEO")
cle_google = os.getenv("CLE_GOOGLE")

print(f"Clé Météo : {cle_meteo}")
print(f"Clé Google Maps : {cle_google}")