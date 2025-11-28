import os
from dotenv import load_dotenv
from extract.movies import extract_movies
from transform.movies import transform_movies
from load.mysql import connect_db, load_dim_movie, load_dim_genre, load_fact_movie_rating
from utils.logger import log

load_dotenv()

def run_etl(total_pages=10):
    log("\n Starting full ETL pipeline...")

    conn = connect_db()
    raw_movies = extract_movies(total_pages=total_pages)
    movies, genres, facts = transform_movies(raw_movies)

    load_dim_movie(conn, movies)
    load_dim_genre(conn, genres)
    load_fact_movie_rating(conn, facts)

    conn.close()
    log("\n ETL pipeline completed successfully!\n")

if __name__ == "__main__":
    run_etl(total_pages=10)
