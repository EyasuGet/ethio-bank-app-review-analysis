# scripts/sentiment_theme.py

import pandas as pd
from transformers import pipeline

# Load cleaned data
df = pd.read_csv("data/clean_reviews.csv")

# Load Hugging Face sentiment model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Apply model
def get_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # Limit to 512 tokens
        return result['label'], result['score']
    except:
        return "NEUTRAL", 0.0

print("Computing sentiment scores...")

df[['sentiment_label', 'sentiment_score']] = df['review'].apply(lambda x: pd.Series(get_sentiment(x)))

# Save to new file
df.to_csv("data/sentiment_reviews.csv", index=False)
print("Sentiment analysis completed and saved to data/sentiment_reviews.csv")
