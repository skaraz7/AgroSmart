import re
from unidecode import unidecode

def normalize_text(text: str) -> str:
    """Normalizar texto para búsquedas"""
    text = unidecode(text.lower())
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def extract_area(text: str) -> float:
    """Extraer área numérica del texto"""
    pattern = r'(\d+(?:\.\d+)?)\s*(?:ha|hectarea|hectárea|m2|metro)'
    match = re.search(pattern, text.lower())
    return float(match.group(1)) if match else None