# backend/app/api/endpoints.py
from fastapi import APIRouter, HTTPException
from app.models.schemas import TextRequest, AnalysisResponse
from app.services.text_analysis import TextAnalyzer

router = APIRouter(prefix="/api", tags=["analysis"])
analyzer = TextAnalyzer()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: TextRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="El texto no puede estar vacío")
        
        result = analyzer.analyze(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el análisis: {str(e)}")

@router.get("/stats")
async def get_stats():
    return {
        "service": "Text Analysis API",
        "endpoints": ["POST /api/analyze", "GET /api/stats"],
        "languages_supported": ["English"],
        "version": "1.0.0"
    }