# scripts/scraper.py

from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime

apps = {
    "Commercial Bank of Ethiopia": "com.combanketh",
    "Bank of Abyssinia": "com.boa.boamobile",
    "Dashen Bank": "com.dashen.bank",
}

all_reviews = []

for bank, app_id in apps.items():
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=450  # target more to clean up later
    )
    for entry in result:
        all_reviews.append({
            "review": entry['content'],
            "rating": entry['score'],
            "date": entry['at'].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

# Save raw data
df.to_csv("data/raw_reviews.csv", index=False)
print("Saved raw reviews to data/raw_reviews.csv")
