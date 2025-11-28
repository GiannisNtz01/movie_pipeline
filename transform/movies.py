from utils.logger import log

def transform_movies(raw_movies):
    log("🔧 Transforming movies...")
    clean_movies = []
    genres_set = set()
    facts = []

    for m in raw_movies:
        if not isinstance(m, dict) or "id" not in m:
            log(f"⚠️ Skipping invalid movie: {m}")
            continue

        movie_id = m["id"]
        title = m.get("title", "Unknown")
        release_year = None
        if m.get("release_date"):
            try:
                release_year = int(m["release_date"].split("-")[0])
            except:
                release_year = None

        popularity = m.get("popularity", 0)
        vote_average = m.get("vote_average", 0)
        vote_count = m.get("vote_count", 0)

        clean_movies.append({
            "id": movie_id,
            "title": title,
            "release_year": release_year,
            "popularity": popularity,
            "vote_average": vote_average,
            "vote_count": vote_count
        })

        for g in m.get("genre_ids", []):
            genres_set.add(g)

        facts.append({
            "movie_id": movie_id,
            "vote_average": vote_average,
            "vote_count": vote_count,
            "popularity": popularity
        })

    log(f"📦 Clean movies: {len(clean_movies)}")
    return clean_movies, list(genres_set), facts
