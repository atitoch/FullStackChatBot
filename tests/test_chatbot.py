"""
Pruebas básicas para el chatbot Full Stack Developer
(Opcional - para demostrar testing en el proyecto)
"""
import sys
import os

# Agregar el directorio padre al path para importar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot import FullStackChatbot


def test_chatbot_initialization():
    """Prueba que el chatbot se inicializa correctamente"""
    try:
        chatbot = FullStackChatbot()
        assert chatbot is not None
        assert len(chatbot.conversation_history) == 1  # Solo system prompt
        print("✅ Test de inicialización: PASSED")
        return True
    except Exception as e:
        print(f"❌ Test de inicialización: FAILED - {e}")
        return False


def test_conversation_history():
    """Prueba que el historial de conversación funciona"""
    try:
        chatbot = FullStackChatbot()
        initial_count = chatbot.get_message_count()
        
        # Simular conversación (sin hacer llamada real a la API)
        chatbot.conversation_history.append({
            "role": "user",
            "content": "Hola"
        })
        
        assert chatbot.get_message_count() == initial_count + 1
        print("✅ Test de historial: PASSED")
        return True
    except Exception as e:
        print(f"❌ Test de historial: FAILED - {e}")
        return False


def test_reset_conversation():
    """Prueba que reiniciar la conversación funciona"""
    try:
        chatbot = FullStackChatbot()
        
        # Agregar mensajes
        chatbot.conversation_history.append({
            "role": "user",
            "content": "Hola"
        })
        chatbot.conversation_history.append({
            "role": "assistant",
            "content": "Hola!"
        })
        
        # Resetear
        chatbot.reset_conversation()
        
        assert chatbot.get_message_count() == 0
        assert len(chatbot.conversation_history) == 1  # Solo system prompt
        print("✅ Test de reset: PASSED")
        return True
    except Exception as e:
        print(f"❌ Test de reset: FAILED - {e}")
        return False


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("\n" + "=" * 50)
    print("🧪 Ejecutando pruebas del chatbot")
    print("=" * 50 + "\n")
    
    tests = [
        test_chatbot_initialization,
        test_conversation_history,
        test_reset_conversation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Resultados: {passed} PASSED, {failed} FAILED")
    print("=" * 50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
