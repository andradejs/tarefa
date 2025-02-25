# Usar dict para produzir uma lista de palavras únicas, onde cada palavra é a chave do dicionário, e mostrar a quantidade de palavras únicas no console (Anotar este resultado);

from extract_text import  extract
import re


def palavras_unicas(arquivo):

    # text = extract(arquivo)
    # palavras = re.findall(r'\b\w+\b', text.lower())
    # palavras_unic =  set(palavras)
    palavras_unic = {}

    palavras = extract(arquivo)
    for c in range(0,len(palavras)):
        palavra = palavras[c]

        if palavra not in palavras_unic:
            palavras_unic[palavra] = 1
        else:
            palavras_unic[palavra] += 1

    return palavras_unic

# resultado = palavras_unicas("texto.txt")
# print(resultado)
# print(len(resultado))



