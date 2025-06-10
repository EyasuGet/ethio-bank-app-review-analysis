# scripts/sentiment_theme.py (continued)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load sentiment-annotated reviews
df = pd.read_csv("data/sentiment_reviews.csv")

# We'll do keyword extraction per bank
banks = df['bank'].unique()

all_keywords = {}

for bank in banks:
    bank_reviews = df[df['bank'] == bank]['review'].fillna("")
    vectorizer = TfidfVectorizer(max_features=20, stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(bank_reviews)
    keywords = vectorizer.get_feature_names_out()
    all_keywords[bank] = keywords.tolist()

# Display top keywords per bank
print("\n=== Top TF-IDF Keywords Per Bank ===")
for bank, keywords in all_keywords.items():
    print(f"\n{bank}:")
    for kw in keywords:
        print(f" - {kw}")

# OPTIONAL: Manually assign themes (basic version)
def assign_theme(text):
    text = text.lower()
    if any(word in text for word in ['login', 'access', 'pin']):
        return 'Account Access Issues'
    elif any(word in text for word in ['slow', 'load', 'delay']):
        return 'Transaction Performance'
    elif any(word in text for word in ['crash', 'bug', 'error']):
        return 'Reliability Issues'
    elif any(word in text for word in ['ui', 'interface', 'design']):
        return 'User Interface'
    elif any(word in text for word in ['feature', 'option', 'update']):
        return 'Feature Requests'
    else:
        return 'General'

df['identified_theme'] = df['review'].apply(assign_theme)

# Save to CSV
df.to_csv("data/final_reviews.csv", index=False)
print("\n✅ Thematic analysis complete and saved to data/final_reviews.csv")
