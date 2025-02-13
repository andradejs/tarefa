import re

def extract(endereco):
    
    with open(endereco,'r',encoding = "utf-8") as arquivo:
        text = arquivo.read()
    
    texto_limpo = re.sub(r'[^a-zA-Záàâãäéèêíïóôõöúç0-9\s-]', '', text)
    
    return texto_limpo.split()
