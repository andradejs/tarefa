# Criar bigramas, usando tuplas, e contar as tuplas únicas, mostrando no console (Anotar este resultado);

from collections import Counter
from extract_text import extract


def counterBigramas():
    
    bigramas = {}

    texto = extract("texto.txt")


    for c in range(0, len(texto)-1):

        bigrama = (texto[c] ,texto[c+1])

        if bigrama not in bigramas:
            bigramas[bigrama] = 1
        else:
            bigramas[bigrama] += 1

    return bigramas

# print(counterBigramas())