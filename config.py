"""
Configuración del chatbot Full Stack Developer
Usando Groq (100% gratuito y ultra rápido)
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno (funciona en local)
load_dotenv()

# Intentar obtener la key desde Streamlit Secrets (para deploy)
# o desde el archivo .env (para local)
try:
    import streamlit as st
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Modelo a usar
MODEL_NAME = "llama-3.3-70b-versatile"

# Parámetros del modelo
TEMPERATURE = 0.7
MAX_TOKENS = 500

# Validar que existe la API key
if not GROQ_API_KEY:
    raise ValueError(
        "No se encontró GROQ_API_KEY. "
        "Obtén tu key gratis en: https://console.groq.com/keys "
        "y crea un archivo .env con: GROQ_API_KEY=tu-key"
    )