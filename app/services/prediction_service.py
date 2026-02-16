import joblib
import os

MODEL_PATH = os.path.join("ml", "model.pkl")
model = joblib.load(MODEL_PATH)

def predict_url(features: dict):
    feature_list = [
        features["url_length"],
        features["has_https"],
        features["num_dots"],
        features["has_at"],
        features["has_dash"],
        features["suspicious_word"]
    ]

    prediction = model.predict([feature_list])[0]
    probability = model.predict_proba([feature_list])[0][1]

    risk_score = int(probability * 100)

    label = "Phishing" if prediction == 1 else "Safe"

    return label, risk_score
