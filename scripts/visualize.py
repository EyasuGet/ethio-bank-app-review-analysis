# scripts/visualize.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/final_reviews.csv")

# 1. Sentiment Distribution per Bank
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='sentiment_label', hue='bank')
plt.title('Sentiment Distribution by Bank')
plt.savefig('data/sentiment_distribution.png')
plt.close()

# 2. Theme Frequency per Bank
plt.figure(figsize=(12, 6))
theme_counts = df.groupby(['bank', 'identified_theme']).size().reset_index(name='count')
sns.barplot(data=theme_counts, x='identified_theme', y='count', hue='bank')
plt.xticks(rotation=30)
plt.title('Theme Frequency by Bank')
plt.tight_layout()
plt.savefig('data/theme_frequency.png')
plt.close()

print("✅ Visualizations saved to data folder.")
