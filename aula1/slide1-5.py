# Função que recebe um texto como argumento e o ”limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc

import string
import unicodedata

def limpa_t():
    t =input("Insere o texto a limpar: ")
    for punctuation in string.punctuation:
        t = t.replace(punctuation, f" {punctuation} ")
    t = t.lower()
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode('utf-8')
    t = " ".join(t.split())
    print (t)

limpa_t()