import os
import pandas as pd

# Project root folder
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input and output paths
input_path = os.path.join(
    project_root,
    "data",
    "raw",
    "adzuna_jobs.csv"
)

output_path = os.path.join(
    project_root,
    "data",
    "processed",
    "cleaned_jobs.csv"
)

# Read raw data
df = pd.read_csv(input_path)

print("Raw rows:", len(df))

# Remove duplicate jobs
df = df.drop_duplicates(subset="job_id")

# Clean text columns
text_columns = ["title", "company", "location", "category", "contract_type", "contract_time"]

for column in text_columns:
    df[column] = df[column].fillna("").astype(str).str.strip()

# Convert salary columns to numeric
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")

# Convert created date
df["created"] = pd.to_datetime(df["created"], errors="coerce")

# Remove rows without a job ID
df = df.dropna(subset=["job_id"])

# Save cleaned data
df.to_csv(output_path, index=False)

print("Cleaned rows:", len(df))
print(f"Saved to: {output_path}")
print("\nFirst 5 cleaned jobs:")
print(df[["job_id", "title", "company", "location", "salary_min", "salary_max"]].head())