# backend/app/models/schemas.py
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    sentiment: str
    sentiment_score: float
    word_count: int
    character_count: int
    entities: list
    summary: str
    word_freq: dict