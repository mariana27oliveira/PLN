#3. Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa

ficheiro = input ("Nome do ficheiro/path do ficheiro:")

def ficheiro_inverso(ficheiro):
    f = list(open(ficheiro))
    print (f[::-1])

ficheiro_inverso(ficheiro)

