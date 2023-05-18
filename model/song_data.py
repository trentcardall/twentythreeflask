from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

app = Flask(__name__)
db_path = os.path.join(app.instance_path, 'volumes', 'song_data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)

class MySongs(db.Model):
    # Define your model schema here
    # Make sure to include the necessary columns that match your CSV file
    __tablename__ = 'songs'  # Specify the name of your table

    id = db.Column(db.Integer, primary_key=True)  # Example column: an integer primary key
    title = db.Column(db.String(255))  # Example column: a string column with length 255
    artist = db.Column(db.String(255))
    top_genre = db.Column(db.String(255))
    year = db.Column(db.Integer)
    bpm = db.Column(db.Integer)
    energy = db.Column(db.Integer)
    danceability = db.Column(db.Integer)
    loudness = db.Column(db.Integer)
    liveness = db.Column(db.Integer)
    valence = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    acousticness = db.Column(db.Integer)
    speechiness = db.Column(db.Integer)
    popularity = db.Column(db.Integer) # Example column: an integer column


    # Additional columns can be defined here

    def __init__(self, title, artist, top_genre, year, bpm, energy, danceability, loudness, liveness, valence, duration, acousticness, speechiness, popularity):
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

    def serialize(song):
        return {
            'id': song.id,
            'name': song.title,
            'top_genre': song.top_genre, 
            'year': song.year, 
            'bpm': song.bpm, 
            'energy': song.energy,
            'danceability': song.danceability, 
            'loudness': song.loudness,
            'liveness': song.liveness,
            'valence': song.valence,
            'duration': song.duration, 
            'acousticness': song.acousticness, 
            'speechiness': song.speechiness,  
            'popularity': song.popularity

            # Serialize additional columns as needed
        }

@app.route('/songdatabase')
def populate_database():
    # Path to the CSV file
    csv_path = 'song_data.csv'

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Create the database tables based on the model schema
    db.create_all()

    # Iterate over the rows of the DataFrame and populate the database
    for _, row in df.iterrows():
        model_instance = MySongs(**row)  # Create an instance of YourModel
        db.session.add(model_instance)  # Add the instance to the session

    db.session.commit()  # Commit the changes to the database

    return 'Database created and populated'

if __name__ == '__main__':
    app.run(debug=True)
