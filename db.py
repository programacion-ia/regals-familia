import sqlite3
import bcrypt
import secrets
import string

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Create the database and tables if they don't exist
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Password TEXT NOT NULL
        )
    ''')

    # Create the gifts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Observations TEXT,
            Link TEXT,
            User_ID INTEGER,
            FOREIGN KEY (User_ID) REFERENCES users(ID)
        )
    ''')

    conn.commit()
    conn.close()

# List of users to insert
users = [
    "Marisa", "Isi", "Aitana", "Juanmi", "Maria", "Pau", 
    "Joan", "Diana", "Paco", "Ana", "Anna", "Saul"
]

# Function to generate bcrypt password hashes
def generate_random_password(length=12):
    # Generate a random password containing letters and digits
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return password, hashed_password

# Insert users with bcrypt hashed passwords and save plain text passwords to a file
def insert_users_and_save_passwords():
    conn = get_db_connection()
    cursor = conn.cursor()

    passwords = {}
    
    # Open file to save plain-text passwords
    with open('user_passwords.txt', 'w') as file:
        for user in users:
            password, hashed_password = generate_random_password()
            cursor.execute("INSERT INTO users (Name, Password) VALUES (?, ?)", (user, hashed_password))
            passwords[user] = password  # Store plain text password for later use
            
            # Write plain-text password to the file
            file.write(f"{user}: {password}\n")

    conn.commit()
    conn.close()
    
    return passwords

def insert_gift(title, observations, link, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the new gift into the database
    cursor.execute('''
        INSERT INTO gifts (Title, Observations, Link, User_ID)
        VALUES (?, ?, ?, ?)
    ''', (title, observations, link, user_id))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to get users from the database
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to get gifts for a specific user from the database
def get_user_gifts(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Title, Observations, Link FROM gifts WHERE User_ID = ?", (user_id,))
    gifts = cursor.fetchall()
    conn.close()
    return gifts

def delete_gift(gift_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gifts WHERE ID = ?", (gift_id,))
    conn.commit()
    conn.close()
    
# Create tables and insert users
# create_tables()
# insert_users_and_save_passwords()

