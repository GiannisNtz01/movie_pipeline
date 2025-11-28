import os
import mysql.connector
from utils.logger import log

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DB", "movie_pipeline")
    )

def load_dim_movie(conn, movies):
    cursor = conn.cursor()
    log("➡ Loading dim_movie...")
    for m in movies:
        cursor.execute("""
            INSERT INTO dim_movie (movie_id, title, release_year)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                title = VALUES(title),
                release_year = VALUES(release_year)
        """, (m["id"], m["title"], m["release_year"]))
    conn.commit()
    cursor.close()
    log("dim_movie loaded.")

def load_dim_genre(conn, genres):
    cursor = conn.cursor()
    log("➡ Loading dim_genre...")
    genre_map = {
        28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
        80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
        14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
        9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
        10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western"
    }
    for genre_id in genres:
        cursor.execute("""
            INSERT INTO dim_genre (genre_id, name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """, (genre_id, genre_map.get(genre_id, "Unknown")))
    conn.commit()
    cursor.close()
    log(" dim_genre loaded.")

def load_fact_movie_rating(conn, facts):
    cursor = conn.cursor()
    log("➡ Loading fact_movie_rating...")
    for f in facts:
        cursor.execute("""
            INSERT INTO fact_movie_rating (movie_id, vote_average, vote_count, popularity)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                vote_average = VALUES(vote_average),
                vote_count = VALUES(vote_count),
                popularity = VALUES(popularity)
        """, (f["movie_id"], f["vote_average"], f["vote_count"], f["popularity"]))
    conn.commit()
    cursor.close()
    log(" fact_movie_rating loaded.")
