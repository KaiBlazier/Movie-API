# Movie API This is a Flask application that fetches movie data from the OMDb API and provides endpoints to retrieve movie information. 
## Features - Fetch movie data from the OMDb API - Provide endpoints to retrieve movie information - Ensure the `requests` library is installed automatically 
## Requirements - Python 3.x - Flask - requests
## Installation
1. Clone the repository: ```bash git clone https://github.com/KaiBlazier/Movie-API.git cd Movie-API
2. python -m venv venv
3. source venv/bin/activate
  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
#Usage
Open your web browser and navigate to http://127.0.0.1:5000/movie?title=MovieTitle to fetch data for a specific movie. Replace MovieTitle with the title of the movie you want to search for.
