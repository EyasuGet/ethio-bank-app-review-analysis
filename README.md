# Fintech App Reviews Analysis

This project is part of the 10 Academy Week 2 Challenge: **Customer Experience Analytics for Fintech Apps**. The goal is to collect, analyze, and derive insights from user reviews of Ethiopian banking apps on the Google Play Store.

---

## 📌 Objective

To simulate the role of a data analyst at a consultancy firm by:
- Scraping real reviews from mobile banking apps
- Preprocessing and cleaning the data
- Performing sentiment analysis using a transformer-based NLP model
- Extracting recurring themes using TF-IDF
- Storing processed data in a PostgreSQL database

---

## 🗂️ Repository Structure

fintech-app-reviews-analysis/
│
├── data/
│ ├── raw_reviews.csv
│ ├── clean_reviews.csv
│ ├── sentiment_reviews.csv
│ └── final_reviews.csv
│
├── scripts/
│ ├── scraper.py
│ ├── preprocess.py
│ ├── sentiment_theme.py
│ └── upload_to_postgres.py
│
├── .gitignore
├── requirements.txt
└── README.md



---

## ✅ Task 1: Scraping & Preprocessing

- Scraped 400+ reviews per bank (CBE, BOA, Dashen)
- Cleaned and normalized review data
- Outputs:
  - `data/raw_reviews.csv`
  - `data/clean_reviews.csv`

---

## ✅ Task 2: Sentiment & Thematic Analysis

- Sentiment analysis using HuggingFace DistilBERT model
- TF-IDF keyword extraction
- Manual theme assignment:
  - Account Access Issues
  - Transaction Performance
  - Reliability Issues
  - User Interface
  - Feature Requests
- Outputs:
  - `data/sentiment_reviews.csv`
  - `data/final_reviews.csv`

---

## ✅ Task 3: PostgreSQL Data Storage

### 📦 Database: `bank_reviews`

#### Schema:
- `banks(id SERIAL PRIMARY KEY, name VARCHAR)`
- `reviews(id SERIAL PRIMARY KEY, review_text TEXT, rating INT, review_date DATE, sentiment_label TEXT, sentiment_score FLOAT, theme TEXT, source TEXT, bank_id INT)`

#### Steps:
- Set up PostgreSQL locally
- Create DB and schema
- Load data using `upload_to_postgres.py`

#### Python Script:
- `scripts/upload_to_postgres.py`

---
## ✅ Task 4: Insights & Visualizations

- **Business Insights**:
  - Top 2 satisfaction drivers per bank
  - Top 2 user pain points per bank
  - Based on sentiment scores and themes
- **Visualizations**:
  - Sentiment Distribution per Bank
  - Theme Frequency per Bank
- Outputs:
  - `data/drivers.csv`
  - `data/pain_points.csv`
  - `data/sentiment_distribution.png`
  - `data/theme_frequency.png`

---

## ⚙️ How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt

## ⚙️ How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt
python scripts/scraper.py
python scripts/preprocess.py
python scripts/sentiment_theme.py
python scripts/upload_to_postgres.py
