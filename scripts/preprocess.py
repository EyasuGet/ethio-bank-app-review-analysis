# scripts/preprocess.py

import pandas as pd

df = pd.read_csv("data/raw_reviews.csv")

# Drop duplicates and missing values
df.drop_duplicates(subset="review", inplace=True)
df.dropna(subset=["review", "rating", "date", "bank"], inplace=True)

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Save clean data
df.to_csv("data/clean_reviews.csv", index=False)
print("Saved cleaned reviews to data/clean_reviews.csv")
