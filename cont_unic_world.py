from extract_text import  extract
import re


def palavras_unicas(arquivo):

    # text = extract(arquivo)
    # palavras = re.findall(r'\b\w+\b', text.lower())
    # palavras_unic =  set(palavras)
    palavras_unic = {}

    quantidade = 0
    for c in range(0,len(extract(arquivo))):
        palavra = arquivo[c]

        if palavra not in palavras_unic:
            palavras_unic[palavra] = quantidade



    return len(palavras_unic)

print(palavras_unicas("texto.txt"))




