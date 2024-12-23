import streamlit as st

# Página de bienvenida
def page_welcome():
    # Add custom CSS for decoration
    st.markdown("""
    <style>
    .welcome-title {
        font-size: 36px;
        color: #FF5733;
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 20px;
    }
    .welcome-text {
        font-size: 18px;
        color: #5C5C5C;
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 20px;
    }
    .welcome-container {
        text-align: center;
        padding: 30px;
        background-color: #f0f0f0;
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 10px;  /* Remove excessive space at the top */
    }
    .center-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 300px; /* Set image width */
    }
    </style>
    """, unsafe_allow_html=True)

    # Container for the welcome message and image
    st.markdown('<div class="welcome-container">', unsafe_allow_html=True)

    # Add a title in Valencian
    st.markdown('<div class="welcome-title">Benvinguts a l’aplicació per demanar la carta als Reis Mags! 🎁👑</div>', unsafe_allow_html=True)

    # Add a beautiful welcome message in Valencian
    st.markdown('<div class="welcome-text">Aquesta és l’aplicació de la família Tomàs, on podràs escriure i enviar la teua carta als Reis Mags. ¡Estàs a punt de viure una experiència màgica! Gaudeix de la nostra aplicació i explora totes les funcionalitats disponibles. Que la màgia dels Reis t’acompanye!</div>', unsafe_allow_html=True)

    # Display the image with the centered style
    st.image("reyes.jpg", use_container_width=True)  # This will automatically stretch the image to fit the container

    st.markdown('</div>', unsafe_allow_html=True)
