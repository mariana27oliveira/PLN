import json

file=open("dicionario_medico_aula.json", encoding="utf-8")
lista = json.load(file)
print(lista)

#json nao tem tuples então ficamos com uma lista de listas