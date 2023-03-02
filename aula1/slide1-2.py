#2. Função que recebe array de números e imprime números pares

x=input("Lista:")
def pares(x):
    y=x.split(" ")
    print("Os números pares são:")
    for i in y:
        if int(i) % 2 == 0:
            print (i)
pares(x)

