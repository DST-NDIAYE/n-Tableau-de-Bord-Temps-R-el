import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Charger les clés API
load_dotenv()
cle_meteo = os.getenv("CLE_METEO")
cle_google = os.getenv("CLE_GOOGLE")

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

# Fonction pour récupérer un itinéraire
def obtenir_itineraire(depart="Paris", arrivee="Lyon", mode="driving"):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={depart}&destination={arrivee}&mode={mode}&key={cle_google}"
    reponse = requests.get(url)
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
    
    
# Fonction pour récupérer les prévisions météo
def obtenir_previsions(ville="Paris"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={ville}&appid={cle_meteo}&units=metric&lang=fr"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        donnees = reponse.json()
        previsions = []
        for i in range(0, 40, 8):  # 5 jours, 8 intervalles par jour (chaque 3h)
            jour = donnees["list"][i]
            previsions.append({
                "date": jour["dt_txt"].split(" ")[0],
                "température": jour["main"]["temp"]
            })
        return previsions
    else:
        return None



    
    


# Interface Streamlit
st.title("🌦️ Météo & 🚗 Itinéraires")

# Sélection de la ville pour la météo
ville = st.text_input("🔍 Entrez une ville :", "Paris")

if st.button("Obtenir la météo"):
    meteo = obtenir_meteo(ville)
    if "erreur" in meteo:
        st.error(meteo["erreur"])
    else:
        st.success(f"Météo à {meteo['ville']}")
        st.write(f"🌡️ Température : {meteo['température']}°C")
        st.write(f"💧 Humidité : {meteo['humidité']}%")
        st.write(f"💨 Vent : {meteo['vent']} km/h")
        st.write(f"🌤️ Conditions : {meteo['conditions']}")



# Vérifier si la variable meteo est définie avant d'y accéder
if 'meteo' in locals() and "conditions" in meteo:
    conditions_dangereuses = ["pluie", "orages", "tempête", "neige", "vent fort"]
    alerte = any(mot in meteo["conditions"] for mot in conditions_dangereuses)

    if alerte:
        st.warning(f"⚠️ Attention ! La météo indique : {meteo['conditions']}. Soyez prudent(e).")



# Prévisions météo
import matplotlib.pyplot as plt

if st.button("Afficher les prévisions météo"):
    previsions = obtenir_previsions(ville)
    if previsions:
        dates = [p["date"] for p in previsions]
        temperatures = [p["température"] for p in previsions]

        fig, ax = plt.subplots()
        ax.plot(dates, temperatures, marker="o", linestyle="-", color="b")
        ax.set_title(f"Prévisions à {ville}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Température (°C)")
        ax.grid(True)

        st.pyplot(fig)
    else:
        st.error("Impossible de récupérer les prévisions météo.")




# Sélection du trajet
st.subheader("🚗 Planifiez votre itinéraire")
depart = st.text_input("📍 Ville de départ", "Paris")
arrivee = st.text_input("🎯 Ville d'arrivée", "Lyon")
mode_transport = st.selectbox("🚌 Mode de transport", ["driving", "walking", "transit", "bicycling"])

if st.button("Obtenir l'itinéraire"):
    trajet = obtenir_itineraire(depart, arrivee, mode_transport)
    if "erreur" in trajet:
        st.error(trajet["erreur"])
    else:
        st.success(f"🚗 Itinéraire de {depart} à {arrivee}")
        st.write(f"📏 Distance : {trajet['distance']}")
        st.write(f"⏳ Durée : {trajet['durée']}")
        st.write("📜 Instructions de trajet :")
        for etape in trajet["instructions"]:
            st.markdown(f"- {etape}", unsafe_allow_html=True)

import folium
from streamlit_folium import folium_static

# Fonction pour afficher une carte avec le trajet
def afficher_carte(depart, arrivee):
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=6)  # Centré sur la France
    folium.Marker([48.8566, 2.3522], popup=f"Départ : {depart}", icon=folium.Icon(color="blue")).add_to(carte)
    folium.Marker([45.7640, 4.8357], popup=f"Arrivée : {arrivee}", icon=folium.Icon(color="red")).add_to(carte)
    return carte

# Afficher la carte si un itinéraire est trouvé
if st.button("Afficher la carte du trajet"):
    carte_itineraire = afficher_carte(depart, arrivee)
    folium_static(carte_itineraire)