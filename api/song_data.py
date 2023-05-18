from flask import Blueprint, jsonify
import sqlite3
import os

songs_api = Blueprint('songs_api', __name__)

# API endpoint to fetch all songs
@songs_api.route('/api/songs', methods=['GET'])
def get_songs():
    db_path = os.path.join(os.getcwd(), 'instance', 'volumes', 'song_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM songs')
    rows = cursor.fetchall()
    conn.close()

    # Format the data as JSON
    songs = []
    for row in rows:
        song = {
            'id': row[0],
            'title': row[1],
            'artist': row[2],
            'top_genre': row[3],
            'year': row[4],
            'bpm': row[5],
            'energy': row[6],
            'danceability': row[7],
            'loudness': row[8],
            'liveness': row[9],
            'valence': row[10],
            'duration': row[11],
            'acousticness': row[12],
            'speechiness': row[13],
            'popularity': row[14]
        }
        songs.append(song)

    return jsonify(songs)
