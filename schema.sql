-- Connect to the bank_reviews database
\c bank_reviews;

-- Create banks table
CREATE TABLE banks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Create reviews table
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    review_text TEXT,
    rating INTEGER,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    theme VARCHAR(100),
    source VARCHAR(50),
    bank_id INTEGER REFERENCES banks(id)
);
