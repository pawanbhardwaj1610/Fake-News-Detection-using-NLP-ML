from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/fake_news_model.pkl")

@app.route("/")
def home():
    return "API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    text = data["text"]

    prediction = model.predict([text])[0]
    prob = model.predict_proba([text])[0]

    confidence = float(np.max(prob))
    score = round(confidence * 100, 2)

    return jsonify({
        "prediction": prediction,
        "credibility_score": score
    })

if __name__ == "__main__":
    app.run(debug=True)