# Utilizar o texto anexo para produzir um dataset tokenizado por espaços em branco;

import re

def extract(endereco):
    
    with open(endereco,'r',encoding = "utf-8") as arquivo:
        text = arquivo.read()

    text = text.lower()
    texto_limpo = re.sub(r'[^a-zA-Záàâãäéèêíïóôõöúç0-9\s-]', '', text)
    
    return texto_limpo.split()

# print(extract("texto.txt"))