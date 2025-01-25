import streamlit as st
import pandas as pd
import numpy as np


# Set page config
st.set_page_config(
    page_title="Tableau de Bord Temps reel",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# Set page title
st.title("Tableau de Bord Temps reel")
st.header(" **Bienvenue** sur le :blue[ Tableau de Bord Temps reel ]")
st.subheader("Ceci est un exemple de tableau de bord en temps réel")
st.text("lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc ")

html_string = """ <div style="background-color: #f5f5f5; padding: 10px;">
<h2 style="color: #0000FF;">Tableau de Bord Temps reel</h2>

<ul>
    <li> <b>Tableau de Bord Temps reel</b> :blue[ Tableau de Bord Temps reel ]</li>
    <li> <b>Tableau de Bord Temps reel</b> :blue[ Tableau de Bord Temps reel ]</li>
    <li> <b>Tableau de Bord Temps reel</b> :blue[ Tableau de Bord Temps reel ]</li>
</ul>

</div> """
st.markdown(html_string, unsafe_allow_html=True)


# Creating a Dataframe from a Dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Mauro'],
'Age': [25, 33, 47, 19, 28, 17],
'City': ['Rome', 'Milan', 'Naples', 'Turin', 'Florence', 'Turin']}
df = pd.DataFrame(data)

st.write(df)


liste = ["A", "B", "C", "D", "E"]

if st.button("Click Me" , help="Click to see the data" , type="secondary"):
    st.write(liste)



if st.checkbox(" accepter les conditions", help="Check to see the data"):
    st.write("You have accepted the conditions")
else:
    st.write("You have not accepted the conditions")    



option = st.selectbox("Choose an option", liste)


st.text("lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc lore ipsumc  lore ipsumc ")

st.number_input("Enter a number", min_value=0, max_value=100, value=50, step=5, help="Enter a number between 0 and 100")


st.metric("temperature", value=25, delta=2, help="Temperature in Celsius")
st.metric("humidity", value=75, delta=-3, help="Humidity in percentage")

st.dataframe(df.style.highlight_max(axis=0))

# Status messages
st.error(" error",  icon=None)
st.warning("warning", icon=None)
st.info("info" , icon=None)
st.success("succes" , icon=None)

