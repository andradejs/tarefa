from extract_text import extract

def bigramas():

    bigramas = []

    texto = extract("texto.txt")

    for c in range(0, len(texto)-1):

        bigrama = (texto[c] ,texto[c+1])

        bigramas.append(bigrama)

    return bigramas