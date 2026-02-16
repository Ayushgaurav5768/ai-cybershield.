def generate_explanation(url: str, features: dict):
    reasons = []

    if features["url_length"] > 50:
        reasons.append("URL length is unusually long")

    if features["suspicious_word"]:
        reasons.append("Suspicious keyword detected in URL")

    if not features["has_https"]:
        reasons.append("Website does not use HTTPS")

    if features["has_at"]:
        reasons.append("URL contains '@' symbol")

    if features["num_dots"] > 3:
        reasons.append("Too many subdomains detected")

    if not reasons:
        reasons.append("No major phishing indicators found")

    return reasons

