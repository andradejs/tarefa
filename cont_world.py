  from extract_text import extract

def contarPalavras(arquivo):

    texto = extract(arquivo)
    return len(texto)

