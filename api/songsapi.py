from flask import Blueprint, jsonify
import pandas as pd
import os

songs_api = Blueprint('songs_api', __name__)

class Song:
    def __init__(self, id, title, artist, top_genre, year, bpm, energy, danceability, loudness, liveness, valence, duration, acousticness, speechiness, popularity):
        self.id = id
        self.title = title
        self.artist = artist
        self.top_genre = top_genre
        self.year = year
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.loudness = loudness
        self.liveness = liveness
        self.valence = valence
        self.duration = duration
        self.acousticness = acousticness
        self.speechiness = speechiness
        self.popularity = popularity

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'top_genre': self.top_genre,
            'year': self.year,
            'bpm': self.bpm,
            'energy': self.energy,
            'danceability': self.danceability,
            'loudness': self.loudness,
            'liveness': self.liveness,
            'valence': self.valence,
            'duration': self.duration,
            'acousticness': self.acousticness,
            'speechiness': self.speechiness,
            'popularity': self.popularity
        }

# API endpoint to fetch all songs
@songs_api.route('/api/songs', methods=['GET'])
def get_songs():
    csv_path = os.path.join('instance', 'volumes', 'song_data.csv')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Convert DataFrame rows to Song objects
    songs = []
    for _, row in df.iterrows():
        song = Song(
            id=row['id'],
            title=row['title'],
            artist=row['artist'],
            top_genre=row['top_genre'],
            year=row['year'],
            bpm=row['bpm'],
            energy=row['energy'],
            danceability=row['danceability'],
            loudness=row['loudness'],
            liveness=row['liveness'],
            valence=row['valence'],
            duration=row['duration'],
            acousticness=row['acousticness'],
            speechiness=row['speechiness'],
            popularity=row['popularity']
        )
        songs.append(song.to_dict())

    return jsonify(songs)
