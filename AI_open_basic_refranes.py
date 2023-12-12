#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

import openai

def complete_phrase_with_gpt3(prompt, api_key):
    openai.api_key = "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"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes elegir el modelo específico de GPT-3 aquí
        prompt=prompt,
        max_tokens=50  # Limita la cantidad de tokens (palabras) generados
    )

    return response.choices[0].text.strip()

# Tu clave API de OpenAI (debes reemplazar esto con tu propia clave)
api_key = "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"

# El comienzo del refrán o frase que quieres completar

prompt = input("Dime el comienzo del refran: ")

# Obtener la frase completada por GPT-3
completed_phrase = complete_phrase_with_gpt3(prompt, api_key)
print("Frase completada:", completed_phrase)
