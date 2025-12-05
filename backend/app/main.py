# backend/app/main.py (completo)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Text Analysis API",
    description="API para análisis de texto con NLTK y TextBlob",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(api_router)

@app.get("/")
def read_root():
    return {
        "message": "Text Analysis API",
        "docs": "http://localhost:8000/docs",
        "endpoints": {
            "analyze": "POST /api/analyze",
            "stats": "GET /api/stats"
        }
    }