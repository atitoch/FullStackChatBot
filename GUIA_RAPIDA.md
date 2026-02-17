# 🚀 Guía de Inicio Rápido

## Pasos para ejecutar tu chatbot (5 minutos)

### Paso 1: Obtener tu API Key de OpenAI ⚡

1. Ve a https://platform.openai.com/signup
2. Crea una cuenta (¡es gratis!)
3. Una vez dentro, ve a https://platform.openai.com/api-keys
4. Click en "Create new secret key"
5. Dale un nombre (ejemplo: "chatbot-universitario")
6. **COPIA** la key (comienza con `sk-...`)
7. **IMPORTANTE:** Guárdala, solo la verás una vez

### Paso 2: Configurar el proyecto 📁

1. Abre tu terminal/consola
2. Navega a la carpeta del proyecto:
   ```bash
   cd chatbot-fullstack-dev
   ```

3. Crea el archivo `.env`:
   ```bash
   # Windows:
   copy .env.example .env
   
   # Mac/Linux:
   cp .env.example .env
   ```

4. Abre el archivo `.env` con cualquier editor de texto
5. Pega tu API key:
   ```
   OPENAI_API_KEY=sk-tu-key-aqui
   ```
6. Guarda el archivo

### Paso 3: Instalar dependencias 📦

```bash
# Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar paquetes
pip install -r requirements.txt
```

### Paso 4: Ejecutar el chatbot 🎉

**Opción A - Interfaz Web (la más bonita):**
```bash
streamlit run app.py
```
Se abrirá automáticamente en tu navegador.

**Opción B - Terminal:**
```bash
python chatbot.py
```

### Paso 5: Probar el chatbot ✨

Prueba con estas preguntas:
- "¿Qué es una API REST?"
- "Explícame la diferencia entre React y Vue"
- "Muéstrame un ejemplo de función async en JavaScript"
- "¿Cómo conectar Python con MongoDB?"

---

## 🎯 Para tu presentación universitaria

### Qué incluir:

1. **Demo en vivo** (2-3 minutos)
   - Muestra la interfaz web
   - Haz 2-3 preguntas diferentes
   - Muestra que recuerda el contexto

2. **Explicación técnica** (3-4 minutos)
   - Cómo funciona (API de OpenAI + Prompts)
   - Por qué elegiste este tema
   - Qué tecnologías usaste

3. **Código importante** (2-3 minutos)
   - Muestra `prompts.py` (la "personalidad")
   - Muestra `chatbot.py` (la lógica principal)
   - Explica el flujo de conversación

### Script sugerido:

> "Desarrollé un chatbot especializado en desarrollo Full Stack usando la API de OpenAI. El proyecto utiliza GPT-4o-mini para generar respuestas, pero lo especial está en el 'prompt del sistema' que le da personalidad y conocimiento específico en programación.
>
> La ventaja sobre usar ChatGPT normal es que este está enfocado 100% en ayudar con código y dudas técnicas. Mantiene contexto de la conversación y puede recordar lo que hablamos antes.
>
> Implementé tanto una interfaz web con Streamlit como una versión de terminal. Déjenme mostrarles..."

---

## 📊 Métricas para reportar

Puedes incluir en tu presentación:
- Número de tecnologías que cubre (10+)
- Velocidad de respuesta (~2-5 segundos)
- Costo por consulta (~$0.002 USD)
- Contexto mantenido (toda la conversación)

---

## 🐛 Si algo sale mal

**"No encuentra el módulo openai"**
```bash
pip install openai
```

**"API key inválida"**
- Verifica que copiaste la key completa
- Verifica que no tenga espacios extras
- Intenta generar una nueva key

**"Streamlit no se abre"**
```bash
python -m streamlit run app.py
```

---

## 💡 Extras opcionales (si tienes tiempo)

1. **Agregar más modos de respuesta**
   - Edita `prompts.py`
   - Agrega botones en `app.py` para cambiar entre modos

2. **Guardar conversaciones**
   - Guarda el historial en un archivo JSON
   - Permite cargar conversaciones pasadas

3. **Estadísticas de uso**
   - Cuenta tokens usados
   - Muestra costo estimado

4. **Deploy en la nube**
   - Sube a Streamlit Cloud (gratis)
   - Comparte el link con tus compañeros

---

## ✅ Checklist antes de presentar

- [ ] El chatbot responde correctamente
- [ ] Probaste al menos 5 preguntas diferentes
- [ ] Funciona el botón de "reiniciar"
- [ ] Tienes ejemplos preparados para la demo
- [ ] Entiendes el código básico (prompts, chat function)
- [ ] Tienes el README actualizado con tu nombre
- [ ] Has practicado la explicación
- [ ] Backup: screenshots por si falla internet

---

¡Éxito en tu presentación! 🎓
