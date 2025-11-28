import os
import requests
from dotenv import load_dotenv
from utils.logger import log

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
if not API_KEY:
    raise ValueError(" Missing TMDB_API_KEY in .env file")

def extract_movies(total_pages=10):
    log("Extracting movies from TMDB...")
    all_movies = []

    for page in range(1, total_pages + 1):
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {"api_key": API_KEY, "language": "en-US", "page": page}
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            log(f" Failed to fetch page {page}: {resp.text}")
            continue
        data = resp.json()
        all_movies.extend(data.get("results", []))
        log(f"  ✔ Page {page} fetched, {len(data.get('results', []))} movies")

    log(f" Total movies extracted: {len(all_movies)}")
    return all_movies
