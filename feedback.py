#NLP based feedback analysis
# backend/routers/

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class Feedback(BaseModel):#single level inhritance
    user_id: str
    text: str

@router.post("/analyze")
def feedback_analysis(feedback: Feedback):
    return analyze_feedback(feedback.text)
