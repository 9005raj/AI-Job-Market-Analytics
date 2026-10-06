import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

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

with engine.connect() as connection:
    result = connection.execute(text("SELECT DATABASE();"))
    print("Connected to database:", result.fetchone()[0])