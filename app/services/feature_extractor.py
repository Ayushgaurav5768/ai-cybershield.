import re

def extract_features(url: str):
    features = {}

    features["url_length"] = len(url)
    features["has_https"] = 1 if "https" in url else 0
    features["num_dots"] = url.count(".")
    features["has_at"] = 1 if "@" in url else 0
    features["has_dash"] = 1 if "-" in url else 0

    suspicious_words = ["login", "verify", "update", "bank", "secure"]
    features["suspicious_word"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    return features
