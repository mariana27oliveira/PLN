import re
import json

ficheirotxt = open("CIH_Bilingual_Medical_Glossary_English-Spanish.xml", encoding="utf-8")
text = ficheirotxt.read()


def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

text = re.sub(r"</?pdf2xml.*?>", "", text)
text = re.sub(r"<!DOCTYPE.*?>", "", text)
text = re.sub(r"<\?xml.*?>", "", text)
text = re.sub(r"</?fontspec.*?>", "", text) 
text = re.sub(r"</?page.*>", "", text)
text = re.sub(r">\d+\s</text>", "", text)
text = re.sub(r"<text top=\"1066\" left=\"802\" width=\"11\" height=\"16\" font=\"1\"", "", text)
text = re.sub(r"<text top=\"1066\" left=\"795\" width=\"19\" height=\"16\" font=\"1\"", "", text)
text = re.sub(r"</?text.*?>", "", text)
text = re.sub(r"<b>(.*)</b>", "", text)
text = re.sub(r"Copyright © 2004 by the Center for Immigrant Health", "", text)
text = re.sub(r"<i>Language Initiatives </i>", "", text)
text = re.sub(r"<i>Center for Immigrant Health \(New York University School of Medicine\) </i>", "", text)
text = re.sub(r"<i>\s</i>", "", text)
text = re.sub(r"<i></i>", "", text)
text = re.sub (r"<i>", "",text)
text = re.sub (r".</i>", "",text)
text = re.sub (r"</i>", "",text)
text = re.sub(r"^\s*$\n?", "", text, flags=re.MULTILINE)

result_f=open("en_es.txt", "w", encoding='UTF-8')
result_f.write(text)
result_f.close()

with open('en_es.txt', 'r', encoding='UTF-8') as f:
    linhas = f.readlines()

#ingles:
linhas_impares = []

#Espanhol:
linhas_pares = []


for i, linha in enumerate(linhas):
    if i % 2 == 0:
        linhas_pares.append(limpa(linha.lower()))
    else:
        linhas_impares.append(limpa(linha.lower()))


lista_de_listas = [[x, y] for x, y in zip(linhas_pares, linhas_impares)]


dicionario={}
dicionario = dict(lista_de_listas)

out = open ("dicio_en_es.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()
