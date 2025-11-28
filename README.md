# 🎬 Movie Pipeline ETL
> An ETL pipeline that extracts top-rated movies from TMDB, transforms the data, and loads it into a MySQL database.

---

## 📊 Workflow
The pipeline follows a standard ETL workflow:
flowchart TD
    A[Start] --> B[Extract Module]
    B --> C[Transform Module]
    C --> D[Load Module (MySQL)]
    D --> E[Visualize Data]

### 🗂️ Project Structure
movie_pipeline/
├─ extract/           # Extract modules (TMDB API requests)
├─ transform/         # Transform modules (cleaning & processing)
├─ load/              # Load modules (MySQL insertion)
├─ utils/             # Utility modules (logging, helpers)
├─ etl_pipeline.py    # Main ETL runner
└─ .env               # Environment variables (API keys, DB credentials)
#### ⚡ Requirements
Python 3.10+
MySQL
Python packages:
pip install -r requirements.txt
##### 🔑 Environment Variables (.env)
The .env file should contain your API keys and database credentials:
TMDB_API_KEY=<your_tmdb_api_key>
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=<your_password>
MYSQL_DB=movie_pipeline
⚠️ Important: Do not commit your .env file to GitHub. Add it to .gitignore.
###### 🏃 Running the ETL Pipeline
Activate your virtual environment and run the pipeline:
1.Activate virtual environment
source venv/bin/activate
2.Run ETL
python etl_pipeline.py
