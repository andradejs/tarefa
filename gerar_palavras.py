# Usar random.choice( list ) para 'gerar' a próxima palavra.

from random import choice
from next_word import next_word

def gerarPalavras(quantidade,palavra_inicial):
    words_dict = next_word()

    frase = palavra_inicial
    
    palavra_atual = palavra_inicial
    for c in range(1,quantidade):
        palavra_atual = choice(words_dict[palavra_atual])
        frase += ' ' + palavra_atual


    return frase

print(gerarPalavras(20,'para'))

#para usar o gerador de lero lero rsrs, basta colocar a quantidade de palavras e a palavra inicial