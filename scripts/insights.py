# scripts/insights.py

import pandas as pd

df = pd.read_csv("data/final_reviews.csv")

# Step 1: Summary by Bank + Theme + Sentiment
summary = df.groupby(['bank', 'identified_theme', 'sentiment_label']).size().reset_index(name='count')

# Step 2: Aggregate sentiment by theme
theme_summary = df.groupby(['bank', 'identified_theme'])['sentiment_score'].agg(['mean', 'count']).reset_index()
theme_summary.columns = ['bank', 'theme', 'avg_sentiment', 'review_count']

# Step 3: Identify top 2 drivers (high sentiment themes)
drivers = theme_summary.sort_values(['bank', 'avg_sentiment'], ascending=[True, False]).groupby('bank').head(2)

# Step 4: Identify top 2 pain points (low sentiment themes)
pain_points = theme_summary.sort_values(['bank', 'avg_sentiment'], ascending=[True, True]).groupby('bank').head(2)

# Save results
drivers.to_csv("data/drivers.csv", index=False)
pain_points.to_csv("data/pain_points.csv", index=False)

print("✅ Drivers and pain points identified and saved.")
