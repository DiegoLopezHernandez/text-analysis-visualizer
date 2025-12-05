# backend/app/services/text_analysis.py
import nltk
from textblob import TextBlob
from collections import Counter
import re

# Auto-descargar recursos NLTK si no existen
def ensure_nltk_data():
    """Descarga automáticamente los datos necesarios de NLTK"""
    resources = {
        'punkt': 'tokenizers/punkt',
        'vader_lexicon': 'sentiment/vader_lexicon.zip',
        'stopwords': 'corpora/stopwords'
    }
    
    for resource_name, resource_path in resources.items():
        try:
            nltk.data.find(resource_path)
            print(f"✓ {resource_name} ya está instalado")
        except LookupError:
            print(f"📥 Descargando {resource_name}...")
            nltk.download(resource_name, quiet=True)
            print(f"✅ {resource_name} descargado")

# Llamar al inicio
ensure_nltk_data()

# Ahora importar después de asegurar datos
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

class TextAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
    
    def analyze(self, text: str) -> dict:
        # Tu código de análisis aquí...
        pass