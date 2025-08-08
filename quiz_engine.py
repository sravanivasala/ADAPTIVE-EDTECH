#backend/services/quiz_engine.py


def generate_quiz(user_id, topic):
 return {
    "user_id": user_id,
    "topic": topic,
    "questions": [
        {"q": "what is AI?", "options": ["Math", "Science", "AI", "Biology"], "answer": "AI"},
        {"q": "Python is a?", "options": ["Language", "Animal", "App"], "answer": "Language"}
    ]
}
