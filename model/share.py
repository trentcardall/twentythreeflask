import sqlite3
from flask import Flask
import os

app = Flask(__name__)
db_path = os.path.join(app.instance_path, 'volumes', 'song_data.db')



def create_table():
    # establish connection and such
    conn = sqlite3.connect('/Users/Trent/vscode/twentythreeflask/instance/volumes/share.db')
    cursor = conn.cursor()

    # creating the table
    songs = '''CREATE TABLE shared_songs(
        _name TEXT,
        _song TEXT,
        _liked INTEGER
    )'''
    cursor.execute(songs)
    print("Table created successfully!")

    # commit new table and close connection
    conn.commit()
    conn.close()

def create_entry():
    name = input("Enter your name:")
    song = input("What is/are some songs you've been suggested?")
    liked = input("What would you rate the song on a scale of 1-10?")
    
    conn = sqlite3.connect('/Users/Trent/vscode/twentythreeflask/instance/volumes/share.db')
    cursor = conn.cursor()
    
    try:
        # Execute an SQL command to insert data into a table
        cursor.execute("INSERT INTO shared_songs (_name, _song, _liked) VALUES (?, ?, ?)", (name, song, liked))
        
        # Commit the changes to the database
        conn.commit()
        print(f"A record for {name} has been created")
                
    except sqlite3.Error as error:
        print("Error while executing the INSERT:", error)

    conn.close()

create_table()
create_entry()
    