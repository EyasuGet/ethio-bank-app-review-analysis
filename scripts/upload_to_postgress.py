# scripts/upload_to_postgres.py

import pandas as pd
import psycopg2

df = pd.read_csv("data/final_reviews.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Insert banks
bank_ids = {}
banks = df['bank'].unique()
for bank in banks:
    cursor.execute("INSERT INTO banks (name) VALUES (%s) RETURNING id", (bank,))
    bank_id = cursor.fetchone()[0]
    bank_ids[bank] = bank_id

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (
            review_text, rating, review_date, sentiment_label,
            sentiment_score, theme, source, bank_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['review'],
        int(row['rating']),
        row['date'],
        row['sentiment_label'],
        float(row['sentiment_score']),
        row['identified_theme'],
        row['source'],
        bank_ids[row['bank']]
    ))

conn.commit()
cursor.close()
conn.close()
print("✅ Data uploaded to PostgreSQL successfully.")
