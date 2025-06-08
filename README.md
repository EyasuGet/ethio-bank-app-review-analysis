# ethio-bank-app-review-analysis

This project is part of the 10 Academy Week 2 Challenge: **Customer Experience Analytics for Fintech Apps**. The goal is to collect, analyze, and derive insights from user reviews of Ethiopian banking apps on the Google Play Store.

## 📌 Objective

To simulate the role of a data analyst at a consultancy firm by:
- Scraping real reviews from mobile banking apps
- Preprocessing and cleaning the data
- Performing sentiment analysis using a transformer-based NLP model
- Extracting recurring themes using TF-IDF

---

## 🗂️ Repository Structure
│
├── data/
│ ├── raw_reviews.csv # Unprocessed scraped data
│ ├── clean_reviews.csv # Cleaned data after preprocessing
│ ├── sentiment_reviews.csv # Data with sentiment scores
│ └── final_reviews.csv # Final data with themes added
│
├── scripts/
│ ├── scraper.py # Scrapes reviews using google-play-scraper
│ ├── preprocess.py # Cleans and formats the raw data
│ └── sentiment_theme.py # Sentiment analysis and keyword-based theme extraction
│
├── requirements.txt # Required Python libraries
├── README.md
└── .gitignore


---

## 🧪 Task 1: Data Collection and Preprocessing

### ✅ Steps
- Scraped 400+ reviews for each bank app:
  - Commercial Bank of Ethiopia
  - Bank of Abyssinia
  - Dashen Bank
- Cleaned data:
  - Removed duplicates
  - Handled missing values
  - Normalized date format to `YYYY-MM-DD`

### 🛠 Tools & Libraries
- [`google-play-scraper`](https://github.com/JoMingyu/google-play-scraper)
- `pandas`

### 📁 Output
- `data/raw_reviews.csv`
- `data/clean_reviews.csv`

---

## 🧠 Task 2: Sentiment and Thematic Analysis

### ✅ Steps
- **Sentiment Analysis**:
  - Used HuggingFace’s `distilbert-base-uncased-finetuned-sst-2-english`
  - Annotated each review with sentiment label (POSITIVE/NEGATIVE) and confidence score

- **Thematic Analysis**:
  - Extracted keywords using `TfidfVectorizer` (unigrams and bigrams)
  - Manually grouped recurring keywords into themes:
    - Account Access Issues
    - Transaction Performance
    - Reliability Issues
    - User Interface
    - Feature Requests

### 🛠 Tools & Libraries
- `transformers`
- `scikit-learn`
- `pandas`

### 📁 Output
- `data/sentiment_reviews.csv`
- `data/final_reviews.csv`

---

## ⚙️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
