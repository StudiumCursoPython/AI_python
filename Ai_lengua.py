import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Descargar los datos necesarios de nltk
nltk.download('punkt')
nltk.download('stopwords')

# Función para procesar el texto
def process_text(text):
    # Tokenización: dividir el texto en palabras
    words = word_tokenize(text)

    # Filtrar las palabras vacías (stopwords)
    filtered_words = [word for word in words if word not in stopwords.words('spanish')]

    # Contar la frecuencia de cada palabra
    word_counts = Counter(filtered_words)

    return word_counts

# Texto de ejemplo
example_text = "Este es un ejemplo de texto para procesar con la biblioteca NLTK en Python."

# Procesar el texto
processed_text = process_text(example_text)

print("Frecuencia de palabras:", processed_text)
