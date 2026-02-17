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

# Manejar pregunta de ejemplo del sidebar
if "temp_question" in st.session_state:
    prompt = st.session_state.temp_question
    del st.session_state.temp_question
else:
    # Input del usuario
    prompt = st.chat_input("Escribe tu pregunta sobre programación...")

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
