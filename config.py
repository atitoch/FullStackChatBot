"""
Configuración del chatbot Full Stack Developer
Usando Groq (100% gratuito y ultra rápido)
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Modelos disponibles en Groq (todos gratis):
# - llama-3.3-70b-versatile  -> Más inteligente (recomendado)
# - llama-3.1-8b-instant     -> Más rápido y ligero
# - mixtral-8x7b-32768       -> Bueno para código
MODEL_NAME = "llama-3.3-70b-versatile"

# Parámetros del modelo
TEMPERATURE = 0.7  # Creatividad (0-1, más alto = más creativo)
MAX_TOKENS = 500   # Máximo de tokens por respuesta

# Validar que existe la API key
if not GROQ_API_KEY:
    raise ValueError(
        "No se encontró GROQ_API_KEY. "
        "Obtén tu key gratis en: https://console.groq.com/keys "
        "y crea un archivo .env con: GROQ_API_KEY=tu-key"
    )
