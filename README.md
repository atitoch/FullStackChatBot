# 🤖 Chatbot Full Stack Developer

Asistente de IA especializado en desarrollo Full Stack, usando **Groq** (100% gratuito y ultra rápido).

## ✨ ¿Por qué Groq?

- ✅ **100% Gratuito** (sin tarjeta de crédito)
- ✅ **Ultra rápido** (más rápido que OpenAI)
- ✅ **Modelos potentes** (Llama 3.3 70B)
- ✅ **Fácil de configurar**

## 📦 Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Obtener API Key gratis de Groq
1. Ve a https://console.groq.com/keys
2. Crea una cuenta (gratis)
3. Click en "Create API Key"
4. Copia la key generada

### 3. Configurar el archivo .env
```bash
# Windows:
copy .env.example .env

# Mac/Linux:
cp .env.example .env
```
Abre `.env` y pega tu key:
```
GROQ_API_KEY=gsk_tu-key-aqui
```

## 🚀 Ejecutar

**Interfaz Web (recomendado):**
```bash
streamlit run app.py
```

**Terminal:**
```bash
python chatbot.py
```

## 📁 Estructura

```
chatbot-fullstack-dev/
├── .env                  # Tu API key (no subir a git)
├── .env.example         # Plantilla del .env
├── requirements.txt     # Dependencias
├── config.py           # Configuración (modelo, temperatura)
├── prompts.py          # Personalidad del chatbot
├── chatbot.py          # Lógica principal
├── app.py              # Interfaz web con Streamlit
└── tests/
    └── test_chatbot.py
```

## 🎯 Modelos disponibles en Groq (todos gratis)

Cambia el modelo en `config.py`:
- `llama-3.3-70b-versatile` → Más inteligente ⭐ (recomendado)
- `llama-3.1-8b-instant` → Más rápido y ligero
- `mixtral-8x7b-32768` → Muy bueno para código

## 🎓 Conceptos de IA aplicados
1. Procesamiento de Lenguaje Natural (NLP)
2. Modelos de Lenguaje (LLMs)
3. Memoria conversacional (historial de mensajes)
4. Especialización mediante System Prompts

## 👨‍💻 Autor
[Tu Nombre] - Proyecto Final de Inteligencia Artificial
