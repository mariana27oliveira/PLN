# Função que recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro

from collections import Counter

def palavrasfreq():
    nome = input("Nome do ficheiro/path do ficheiro: ")
    f = open(nome, 'r')
    p = f.read().split()
    c = Counter(p)
    for p, cont in c.most_common(10):
        print(f"{p}: {cont}")

palavrasfreq()