import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.preprocess import clean_text

# Load data
data = pd.read_csv("data/final_dataset.csv")

# Clean text
data["text"] = data["text"].apply(clean_text)

# Balance dataset (VERY IMPORTANT)
fake = data[data["label"] == "FAKE"]
real = data[data["label"] == "REAL"]

min_len = min(len(fake), len(real))

data = pd.concat([
    fake.sample(min_len),
    real.sample(min_len)
])

# Shuffle
data = data.sample(frac=1)

X = data["text"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.7)),
    ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

# Accuracy check
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/fake_news_model.pkl")

print("✅ Model trained successfully")