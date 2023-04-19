import re
import json

ficheiro = open("RU5HW615037.xml", encoding="utf-8")
text = ficheiro.read()

ficheiro.close()


#text = re.sub(r"</?page.*>", "", text)
#text = re.sub(r"</?text.*?>", "", text) #*? para ele parar no primeiro > e não retirar info importante
#text = re.sub(r"\n<i>.*</i>\n", " ", text)
#text = re.sub(r"\f", "", text)
#text = re.sub(r"(\n\n(.*)\n\n((.*)\n\n)*)", "", text)
#lista = re.findall(r"<b>(.*?)\nU\n(.*?)\nE\n(.*?)\n<b>", text, re.S) #o \. não é necessario pq pode nao ter ponto final

text = re.sub(r"</?page.*>", "", text) #nao precisa de ? pq para sede qualquer forma nos \n
text = re.sub(r"</?fontspec.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) #*? para ele parar no primeiro > e não retirar info importante
text = re.sub(r"\n<i>.*</i>\n", "", text)
text = re.sub(r"<b>(.*?)</b>", "", text)
#text = re.sub(r"\n+", " ", text)
#text = re.sub(r"\s+", " ", text)
#text = re.sub(r"- ", "", text)
#text = text.strip()

lista = re.findall(r"(.*) - (.*)", text) #o \. não é necessario pq pode nao ter ponto final
nova_lista = [[(pt.strip()).lower(), en] for en, pt in lista]
#lista = [[pt, limpa(traducao)] for pt, traducao in lista]

dicionario = dict(nova_lista) #converter em dicionário pq assim depois dá para ter tuplos
#result.write(text)


file_out = open("doc_2_colgate.json", "w", encoding="utf-8")
json.dump(dicionario, file_out, ensure_ascii=False, indent=4)
file_out.close()
