""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from collections import Counter
from nltk import bigrams
import random
import nltk

# Función para construir un modelo de bigramas
def build_bigram_model(text):
    tokens = nltk.word_tokenize(text.lower())  # Tokenizar y convertir a minúsculas
    bigrams_list = list(bigrams(tokens))  # Crear bigramas
    bigram_model = {}
    for bigram in bigrams_list:
        if bigram[0] in bigram_model:
            bigram_model[bigram[0]].append(bigram[1])
        else:
            bigram_model[bigram[0]] = [bigram[1]]
    return bigram_model

# Texto de ejemplo para entrenar el modelo
text = """
En casa del herrero, cuchillo de palo.
Más vale pájaro en mano que ciento volando.
No hay mal que por bien no venga.
El que mucho abarca poco aprieta.
"""

# Construir el modelo
model = build_bigram_model(text)

# Función para completar un refrán
def complete_proverb(start_word, model, length=5):
    current_word = start_word.lower()
    sentence = [current_word]
    for _ in range(length):
        next_words = model.get(current_word)
        if not next_words:
            break
        next_word = random.choice(next_words)
        sentence.append(next_word)
        current_word = next_word
    return ' '.join(sentence)

# Palabra inicial del refrán
initial_word = "Más"

# Intentar completar el refrán
completed_proverb = complete_proverb(initial_word, model)
print("Refrán completado:", completed_proverb)