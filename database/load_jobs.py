import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = "root"
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "job_market_analytics"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# Project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cleaned CSV path
csv_path = os.path.join(
    project_root,
    "data",
    "processed",
    "cleaned_jobs.csv"
)

# Read cleaned jobs
df = pd.read_csv(csv_path)

print("Jobs loaded from CSV:", len(df))

# Load data into MySQL
df.to_sql(
    "jobs",
    con=engine,
    if_exists="replace",
    index=False
)

print("Successfully loaded jobs into MySQL.")