import re
import json

ficheiro = open("dicionario_medico.xml", encoding="utf-8")
text = ficheiro.read()

def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip() #para tirar os espaços em branco antes da descrição

text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) #*? para ele parar no primeiro > e não retirar info importante
#text = re.findall(r"(<b>(.*)</b>([^<].*\.))", text) ----- so apanha descrições de uma linha 
lista = re.findall(r"<b>(.*)</b>([^<]*)", text) #o \. não é necessario pq pode nao ter ponto final

lista = [[designacao, limpa(descricao)] for designacao, descricao in lista]

#dicionario = dict(lista) #converter em dicionário pq assim depois dá para ter tuplos


#out = open ("dicionario_medico_aula.json", "w", encoding="utf-8")
#json.dump(lista, out, ensure_ascii=False, indent=4)
#json.dump(dicionario, out, ensure_ascii=False, indent=4)
#out.close()

#dicionario = {}
print(lista)

