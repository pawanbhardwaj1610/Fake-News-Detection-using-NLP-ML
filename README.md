# 🧠 Real-Time Fake News Detection System (ML + FastAPI + Streamlit)

## 📖 Problem Statement

Fake news spreads rapidly across digital platforms and can mislead people, influence opinions, and create misinformation.

The goal of this project is to **detect whether a news article is real or fake in real-time** using Natural Language Processing (NLP) and Machine Learning.

Early detection helps:

* Prevent misinformation spread
* Improve content credibility
* Support fact-checking systems
* Assist users in verifying news

---

## 🚀 Project Highlights

🔹 Machine Learning Model (Logistic Regression)
🔹 FastAPI Backend (Real-time prediction API)
🔹 Streamlit Dashboard (Modern UI)
🔹 News Credibility Score (%)
🔹 Web Scraping Support (URL-based input)
🔹 End-to-End ML Pipeline

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* FastAPI
* Streamlit
* BeautifulSoup (Web Scraping)
* Requests
* Pandas & NumPy

---

## 📂 Dataset Description

The dataset contains:

* News title
* News text/content
* Labels (Fake / Real)

📊 Source: Kaggle Fake & Real News Dataset

---

## 🔍 Approach

* Data collection from dataset
* Data cleaning and preprocessing
* Text vectorization using TF-IDF
* Model training using ML algorithms
* Model saving using Pickle
* API development using FastAPI
* Dashboard creation using Streamlit
* Integration of frontend with backend
* Real-time prediction system

---

## 📊 Model Performance

✅ Model Used: Logistic Regression
🎯 Accuracy: ~90–95% (depends on dataset split)

---

## 📈 Features of Application

🔮 Detect fake news in real-time
🌐 Analyze news via URL (web scraping)
📊 Display credibility score (%)
🟢🔴 Fake/Real classification with color indicator
📉 Clean and modern dashboard UI

---

## 🖥️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/pawanbhardwaj1610/Fake-News-Detection-using-NLP-ML.git
cd Fake-News-Detection-using-NLP-ML
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI server

```bash
uvicorn api.main:app --reload
```

### 4️⃣ Run Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📥 Dataset

Due to size limitations, dataset is not included in this repository.

👉 Download from Kaggle:
[https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 🎯 Future Improvements

* 🤖 Deep Learning model (BERT)
* 🌍 Multi-language support
* ☁️ Cloud deployment (Streamlit Cloud / Render)
* 📊 Advanced analytics dashboard

---

## 👤 Author

**Pawan Bhardwaj**
Aspiring Data Science Intern

💡 Skills: Python, SQL, EDA, Machine Learning, NLP

---
