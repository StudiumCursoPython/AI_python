#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

import openai

def completar_frase_gpt3(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        # Puedes elegir el modelo específico de GPT-3 aquí
        engine="text-davinci-003",  
        prompt=prompt,
        # Número máxinmo de palabras generadas
        max_tokens=50  
    )

    return response.choices[0].text.strip()

# Clave API de OpenAI
api_key = "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"

# El comienzo del refrán o frase que quieres completar

prompt = input("Dime el comienzo del refran: ")

# Obtener la frase completada por GPT-3
completed_phrase = completar_frase_gpt3(prompt, api_key)
print("Frase completada:", completed_phrase)
