from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/songdata', methods=['GET'])
def get_data():
    data = []
    with open('songdata.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return jsonify(data)

if __name__ == '__main__':
    app.run()

