from flask import Flask, jsonify, request, Blueprint
import sqlite3

share_api = Blueprint('share_api', __name__)

app = Flask(__name__)
db_path = 'Users/Trent/vscode/twentythreeflask/instance/volumes/share.db'

# Retrieve all shared songs
@app.route('/api/share', methods=['GET'])
def get_songs():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shared_songs")
    rows = cursor.fetchall()
    conn.close()
    
    songs = []
    for row in rows:
        song = {
            '_name': row[0],
            '_song': row[1],
            '_liked': row[2]
        }
        songs.append(song)
    
    return jsonify(songs)

# Add a new shared song
@app.route('/api/share', methods=['POST'])
def add_song():
    data = request.get_json()
    
    name = data.get('_name')
    song = data.get('_song')
    liked = data.get('_liked')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO shared_songs (_name, _song, _liked) VALUES (?, ?, ?)",
                   (name, song, liked))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Song added successfully'})

if __name__ == '__main__':
    app.run()
