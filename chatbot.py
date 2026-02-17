"""
Chatbot Full Stack Developer
Lógica principal del asistente de programación usando Groq (gratis)
"""
from typing import List, Optional
import re

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS
from prompts import SYSTEM_PROMPT, OFF_TOPIC_RESPONSE


class FullStackChatbot:
    """Chatbot especializado en desarrollo Full Stack usando Groq"""

    _KEYWORDS = (
        "full stack",
        "fullstack",
        "programacion",
        "programación",
        "programming",
        "software",
        "desarrollo",
        "web",
        "frontend",
        "backend",
        "html",
        "css",
        "javascript",
        "typescript",
        "react",
        "vue",
        "angular",
        "node",
        "node.js",
        "python",
        "django",
        "flask",
        "fastapi",
        "java",
        "php",
        "golang",
        "mysql",
        "postgres",
        "postgresql",
        "mongodb",
        "redis",
        "sql",
        "nosql",
        "api",
        "rest",
        "graphql",
        "websocket",
        "http",
        "https",
        "git",
        "docker",
        "ci/cd",
        "cicd",
        "jwt",
        "mvc",
        "auth",
        "autenticacion",
        "autenticación",
        "seguridad",
        "deploy",
        "despliegue",
        "debug",
        "bug",
        "error",
        "exception",
        "stack trace",
        "endpoint",
        "json",
        "orm",
    )

    _SHORT_TOKEN_PATTERN = re.compile(r"\b(js|ts|sql|api|jwt|mvc|http|https|db)\b")
    
    def __init__(self):
        """Inicializa el cliente de Groq y el historial de conversación"""
        self.client = Groq(api_key=GROQ_API_KEY)
        self.conversation_history: List[ChatCompletionMessageParam] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def _is_in_scope(self, user_message: str) -> bool:
        """Valida que la pregunta sea de desarrollo Full Stack"""
        text = user_message.lower().strip()
        if not text:
            return False
        if "```" in text:
            return True
        if self._SHORT_TOKEN_PATTERN.search(text):
            return True
        return any(keyword in text for keyword in self._KEYWORDS)
    
    def chat(self, user_message: str) -> str:
        """
        Envía un mensaje al chatbot y obtiene una respuesta
        
        Args:
            user_message: Mensaje del usuario
            
        Returns:
            Respuesta del asistente
        """
        # Agregar mensaje del usuario al historial
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        if not self._is_in_scope(user_message):
            self.conversation_history.append({
                "role": "assistant",
                "content": OFF_TOPIC_RESPONSE
            })
            return OFF_TOPIC_RESPONSE
        
        try:
            # Hacer la llamada a la API de Groq
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=self.conversation_history,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            
            # Extraer la respuesta del asistente
            assistant_message: Optional[str] = response.choices[0].message.content
            if assistant_message is None:
                raise RuntimeError("La respuesta de Groq no tiene contenido.")
            
            # Agregar respuesta al historial
            self.conversation_history.append(
                {"role": "assistant", "content": assistant_message}
            )
            
            return assistant_message
            
        except Exception as e:  # pylint: disable=broad-exception-caught
            return f"Error al comunicarse con Groq: {str(e)}"
    
    def reset_conversation(self):
        """Reinicia la conversación manteniendo solo el prompt del sistema"""
        self.conversation_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    
    def get_history(self) -> List[ChatCompletionMessageParam]:
        """Retorna el historial completo de la conversación"""
        return self.conversation_history
    
    def get_message_count(self) -> int:
        """Retorna el número de mensajes (sin contar el system prompt)"""
        return len(self.conversation_history) - 1


# Función auxiliar para usar el chatbot desde terminal
def main():
    """Función principal para ejecutar el chatbot en modo terminal"""
    print("=" * 60)
    print("🤖 Chatbot Full Stack Developer (powered by Groq - Gratis)")
    print("=" * 60)
    print("Escribe 'salir' o 'exit' para terminar")
    print("Escribe 'reset' para reiniciar la conversación")
    print("=" * 60)
    print()
    
    chatbot = FullStackChatbot()
    
    while True:
        # Obtener input del usuario
        user_input = input("Tú: ").strip()
        
        # Verificar comandos especiales
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("\n¡Hasta luego! 👋")
            break
        
        if user_input.lower() == 'reset':
            chatbot.reset_conversation()
            print("\n✅ Conversación reiniciada\n")
            continue
        
        if not user_input:
            continue
        
        # Obtener y mostrar respuesta
        print("\n🤖 Asistente: ", end="")
        response = chatbot.chat(user_input)
        print(response)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
