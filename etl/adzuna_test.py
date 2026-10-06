import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")

url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": 50,
    "what": "data analyst",
    "where": "India",
    "content-type": "application/json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    jobs = data["results"]

    rows = []

    for job in jobs:
        rows.append({
            "job_id": job.get("id"),
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "category": job.get("category", {}).get("label"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "contract_type": job.get("contract_type"),
            "contract_time": job.get("contract_time"),
            "created": job.get("created"),
            "description": job.get("description"),
            "redirect_url": job.get("redirect_url")
        })

    df = pd.DataFrame(rows)

    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "raw",
        "adzuna_jobs.csv"
    )
    df.to_csv(output_path, index=False)

    print(f"Successfully collected {len(df)} jobs.")
    print(f"Saved to: {output_path}")
    print(df.head())

else:
    print("API Error:", response.status_code)
    print(response.text)