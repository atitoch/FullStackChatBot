"""
Interfaz web del Chatbot Full Stack Developer usando Streamlit
"""
import streamlit as st
from chatbot import FullStackChatbot


# Configuración de la página
st.set_page_config(
    page_title="Full Stack Dev Assistant",
    page_icon="🤖",
    layout="wide"
)

# Título y descripción
st.title("🤖 Full Stack Developer Assistant")
st.markdown("""
Asistente de IA especializado en desarrollo Full Stack. 
Pregunta sobre frontend, backend, bases de datos, APIs y más.
""")

# Estilos personalizados para mejor UI
st.markdown(
    """
    <style>
    /* Hacer el input sticky y con mejor integración visual */
    div[data-testid="stChatInput"] {
        position: sticky;
        bottom: 0;
        z-index: 100;
        padding: 1.5rem 0;
        background: linear-gradient(to top, var(--default-backgroundColor) 85%, transparent);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }
    
    /* Agregar padding inferior al contenedor de mensajes */
    .main .block-container {
        padding-bottom: 6rem;
    }
    
    /* Mejorar el área de input - hacerla transparente y sin bordes */
    div[data-testid="stChatInput"] > div {
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Ajustar el input interno con mejor padding y borde rojo profesional */
    div[data-testid="stChatInput"] textarea {
        background-color: rgba(38, 39, 48, 0.9) !important;
        border: 2px solid #ff4b4b !important;
        border-radius: 0.75rem !important;
        color: var(--text-color) !important;
        padding: 1rem 1.25rem !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
        min-height: 3rem !important;
        background-clip: padding-box !important;
    }
    
    div[data-testid="stChatInput"] textarea:focus {
        border-color: #ff6b6b !important;
        box-shadow: 0 0 0 3px rgba(255, 75, 75, 0.2) !important;
        outline: none !important;
    }
    
    div[data-testid="stChatInput"] textarea::placeholder {
        color: rgba(250, 250, 250, 0.5) !important;
    }
    
    /* Responsivo para móviles */
    @media (max-width: 768px) {
        div[data-testid="stChatInput"] {
            padding: 1rem 0;
        }
        
        .main .block-container {
            padding-bottom: 5rem;
        }
        
        div[data-testid="stChatInput"] textarea {
            padding: 0.75rem 1rem !important;
            font-size: 0.95rem !important;
            min-height: 2.5rem !important;
            border-radius: 0.5rem !important;
        }
        
        div[data-testid="stChatInput"] textarea:focus {
            box-shadow: 0 0 0 2px rgba(255, 75, 75, 0.2) !important;
        }
    }
    
    /* Extra pequeño para móviles muy pequeños */
    @media (max-width: 480px) {
        div[data-testid="stChatInput"] {
            padding: 0.75rem 0;
        }
        
        div[data-testid="stChatInput"] textarea {
            padding: 0.65rem 0.85rem !important;
            font-size: 0.9rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicializar el chatbot en session_state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = FullStackChatbot()
    st.session_state.messages = []

# Sidebar con información y controles
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    **Áreas de conocimiento:**
    - Frontend (React, Vue, Angular)
    - Backend (Node.js, Python, Java)
    - Bases de datos (SQL, NoSQL)
    - APIs REST y GraphQL
    - DevOps básico
    """)
    
    st.divider()
    
    # Contador de mensajes
    msg_count = st.session_state.chatbot.get_message_count()
    st.metric("Mensajes enviados", msg_count)
    
    st.divider()
    
    # Botón para reiniciar
    if st.button("🔄 Reiniciar conversación", use_container_width=True):
        st.session_state.chatbot.reset_conversation()
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Ejemplos de preguntas
    st.markdown("**💡 Ejemplos de preguntas:**")
    ejemplos = [
        "¿Qué es REST API?",
        "Diferencia entre SQL y NoSQL",
        "¿Cómo usar async/await en JS?",
        "Explica el patrón MVC",
    ]
    
    for ejemplo in ejemplos:
        if st.button(f"📌 {ejemplo}", key=ejemplo, use_container_width=True):
            st.session_state.temp_question = ejemplo

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario (siempre visible)
prompt = st.chat_input("Escribe tu pregunta sobre programación...")

# Manejar pregunta de ejemplo del sidebar
if "temp_question" in st.session_state:
    prompt = st.session_state.temp_question
    del st.session_state.temp_question

# Procesar el mensaje
if prompt:
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Agregar a la lista de mensajes
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Obtener respuesta del chatbot
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.chatbot.chat(prompt)
            st.markdown(response)
    
    # Agregar respuesta a la lista
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.divider()
st.caption("Chatbot Full Stack Developer - Proyecto Universitario de IA")
