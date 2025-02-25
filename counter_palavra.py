# Substituir o dict por Counter;

from collections import Counter
from extract_text import extract

def contar_palavras_counter(texto):
    palavras = texto  
    contagem_palavras = Counter(palavras)  

    return contagem_palavras

# print(contar_palavras_counter(extract("texto.txt")))