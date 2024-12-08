import subprocess
import sys

# Ensure the requests library is installed
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = 'd8315686'
BASE_URL = 'http://www.omdbapi.com/'

def fetch_movie_data(title):
    url = f"{BASE_URL}?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return data
        else:
            return {"error": f"Movie not found: {data['Error']}"}
    else:
        return {"error": f"Error: {response.status_code}"}

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = [
        {"id": 1, "title": "Inception", "year": 2010},
        {"id": 2, "title": "The Matrix", "year": 1999},
        {"id": 3, "title": "Interstellar", "year": 2014}
    ]
    return jsonify(movies)

@app.route('/movie', methods=['GET'])
def get_movie():
    title = request.args.get('title')
    if title:
        movie_data = fetch_movie_data(title)
        return jsonify(movie_data)
    else:
        return jsonify({"error": "No movie title provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
