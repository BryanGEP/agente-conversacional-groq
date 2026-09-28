# 💬 Agente Conversacional con IA (Groq)

Chatbot de línea de comandos escrito en Python que mantiene una conversación en lenguaje
natural usando la **API de Groq** sobre el modelo open-weight `openai/gpt-oss-120b`, con
**memoria de corto plazo** para recordar los últimos mensajes del intercambio.

Es un proyecto base que introduce los fundamentos de un agente conversacional (llamada al
modelo, manejo del historial y bucle de conversación). Sobre esta base se construyeron
después versiones más avanzadas que añaden *tool use* para gestionar Google Calendar.

## ✨ Características

- Conversación por terminal en lenguaje natural.
- Memoria de corto plazo: recuerda los últimos mensajes para dar continuidad al diálogo.
- Configuración sencilla mediante variables de entorno.

## 🧰 Tecnologías

- **Python 3.13**
- **Groq** — inferencia del modelo `openai/gpt-oss-120b`
- `python-dotenv` para el manejo de variables de entorno

> ℹ️ Si en tu `agente1.py` usas un modelo distinto, actualiza el nombre en esta sección.

## 📁 Estructura del proyecto

```
.
├── agente1.py         # Bucle principal del chatbot
├── simple_memory.py   # Memoria de conversación de corto plazo
├── requirements.txt
└── .env               # (NO se sube) Clave de la API de Groq
```

## ✅ Requisitos previos

1. **Python 3.13** instalado.
2. Una **clave de API de Groq**, obtenida en [console.groq.com](https://console.groq.com).

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/BryanGEP/agente-conversacional-groq.git
cd agente-conversacional-groq

# 2. Crear y activar el entorno virtual
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate
# Linux / macOS:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## 🔧 Configuración

Crea un archivo `.env` en la raíz del proyecto con tu clave de Groq:

```
Pk_GROQ=tu-clave-de-groq-aqui
```

## ▶️ Uso

```bash
python agente1.py
```

Escribe tus mensajes en la terminal y el agente responderá manteniendo el contexto de la
conversación. Escribe `salir` para terminar.

## 🔒 Seguridad

El archivo `.env` contiene tu clave privada de la API y **nunca debe subirse al
repositorio** (está excluido en `.gitignore`). Si una clave se filtra públicamente,
revócala de inmediato y genera una nueva.

## 👤 Autor

**Bryan Gael Esquivel Pérez** — [@BryanGEP](https://github.com/BryanGEP)
