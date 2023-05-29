# Função que recebe um texto como argumento e o ”limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc

import string
import unicodedata

def limpa_t():
    t =input("Insere o texto a limpar: ")
    for punctuation in string.punctuation:
        t = t.replace(punctuation, f" {punctuation} ")
        print(t)
    t = t.lower()
    print(t)
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode('utf-8')
    print(t)
    t = " ".join(t.split())
    print (t)

limpa_t()