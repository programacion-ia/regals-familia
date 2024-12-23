
import streamlit as st
from db import get_users, get_user_gifts, delete_gift

def page_users(user_id):
    st.title("Regalets 🎁")

    # Get users from the database
    users = get_users()
    user_names = [user[1] for user in users]  # Extract user names for the selectbox

    # Select a user from the dropdown
    user_name = st.selectbox("Selecciona un usuari per a veure més detalls", user_names)

    if user_name:
        # Get the selected user's ID
        selected_user_id = next(user[0] for user in users if user[1] == user_name)
        
        # Fetch gifts for the selected user
        gifts = get_user_gifts(selected_user_id)

        st.subheader(f"Regals de {user_name}")
        
        # Display only gifts for the selected user
        if gifts:
            for gift in gifts:
                st.write(f"**Títol**: {gift[1]}")
                st.write(f"**Observacions**: {gift[2]}")
                
                # Render the gift link as a clickable URL
                if gift[3]:  # Check if there's a link
                    st.markdown(f"**Link**: [{gift[3]}]({gift[3]})")  # Render link as clickable
                
                # Show a delete button for the logged-in user only
                if st.session_state.logged_in and st.session_state.user_id == selected_user_id:
                    if st.button(f"Eliminar regal de {user_name}: {gift[1]}", key=gift[0]):
                        delete_gift(gift[0])  # Delete the gift by ID
                        st.success(f"Regal '{gift[1]}' eliminat amb èxit.")
                st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.write(f"{user_name} no té regals assignats.")

