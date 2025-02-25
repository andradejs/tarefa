# Criar um dict de str para list, onde a chave é a primeira palavra de cada tupla única e o valor é uma lista das palavras que a seguem no texto;
# Mostrar na tela a lista de palavras que seguem a palavra 'para' (Anotar este resultado);


from bigramas import bigramas
from bigramas_unicos import counterBigramas

def next_word():

    word_dict = {}

    bigramas_list = bigramas()

    for word1, word2 in bigramas_list:

        if word1 not in word_dict:

            word_dict[word1] = []

        word_dict[word1].append(word2)

    


    return word_dict

    
# words = next_word()
# print(words)
# print(words['para'])