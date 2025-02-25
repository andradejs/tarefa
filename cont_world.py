# Contar o total de palavras e mostrar o resultado no console (Anotar este resultado);

from extract_text import extract

def contarPalavras(arquivo):

    texto = extract(arquivo)
    return len(texto)

