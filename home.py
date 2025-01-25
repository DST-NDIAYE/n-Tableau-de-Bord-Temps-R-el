import streamlit as st

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