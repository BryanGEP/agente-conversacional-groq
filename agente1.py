from dotenv import load_dotenv 
from groq import Groq
import os

from simple_memory import SimpleMemory

load_dotenv()

api_key=os.environ.get("Pk_GROQ")
client=Groq(api_key=api_key)
memory=SimpleMemory(max_messages=10)


print("Mi primer agente de IA") 

while True:

    user_input = input("Tu: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ('exit', 'salir'):
        print("Hasta luego")
        break

    #Recuperar memoria
    messages=memory.messages()

    messages.append(
        {"role": "user", "content": user_input}
    )

    #Llamar al modelo
    resp= client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages= messages
    )

    msg = resp.choices[0].message
    assitant_text = msg.content or ""
    print(f"Asistente: {assitant_text}")

    #Agregar los mensajes del usuario y del LLM
    memory.add("user", user_input)
    memory.add("assistant", assitant_text)