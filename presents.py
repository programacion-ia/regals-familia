import streamlit as st
from db import insert_gift
# Página vacía

def page_empty(user_id):
    st.title("Fes la carta als Reis Mags 🎁")

    # Gift form
    title = st.text_input("Títol del regal")
    observations = st.text_area("Observacions")
    link = st.text_input("Link (opcional)", "")

    if st.button("Insertar regal"):

        # Insert the gift into the database
        if title:
            insert_gift(title, observations, link, user_id)
            st.success(f"Regal '{title}' insertat correctament.")
        else:
            st.error("El títol del regal és obligatori.")