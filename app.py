import streamlit as st
import pandas as pd
from users import page_users
from welcome import page_welcome
from presents import page_empty 
import sqlite3
import bcrypt

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Function to check if user credentials are correct
def check_credentials(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query the database for the user
    cursor.execute("SELECT * FROM users WHERE Name = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        # Check if the provided password matches the hashed password
        stored_hashed_password = user[2]  # The password is in the third column of the 'users' table
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            return user  # Return the user data (e.g., user[0] is the ID)
        else:
            return None
    else:
        return None

# Main function to handle login and session state
def main():
    # Initialize session state if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_id = None

    # Check if the user is logged in or not
    if not st.session_state.logged_in:
        st.title('Reis Mags de la familia Tomàs 🎄')
        username = st.text_input('Usuari')
        password = st.text_input('Contraseya', type='password')

        if st.button('Iniciar sessió'):
            user = check_credentials(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user_id = user[0]  # Save the user ID (user[0] is the first column)
                st.rerun()  # Rerun the script to refresh and show the app content
            else:
                st.error('Credencials incorrectes')

    else:        
        page = st.sidebar.radio("Selecciona una pàgina", ("Benvinguda", "Usuaris", "Inserta un Regal"))
        
        if page == "Benvinguda":
            page_welcome()
        elif page == "Usuaris":
            page_users(st.session_state.user_id)
        elif page == "Inserta un Regal":
            page_empty(st.session_state.user_id)

if __name__ == "__main__":
    main()