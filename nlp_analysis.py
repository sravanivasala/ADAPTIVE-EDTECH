# backend/services/nlp_analysis.py

def analyze_feedback(feedback_text: str) -> dict:
    # Dummy implementation—replace with your actual logic
    sentiment = "positive" if "good" in feedback_text.lower() else "neutral"
    return {"sentiment": sentiment, "keywords": []}
