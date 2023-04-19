import re
import json

ficheirotxt = open("Glossario_de_termos_Medicos_Tecnicos_Populares.xml", encoding="utf-8")
text = ficheirotxt.read()

text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) 
text = re.sub(r"</?fontspec.*?>", "", text) 
text = re.sub (r"<i>", "",text)
text = re.sub (r"</i>", "",text)


text = re.sub(r"<b>[A-Z]</b>", "", text)


lista1 = re.findall(r"<b>(.*)</b>", text) 


text2 = re.sub(r"<b>(.*)</b>", "", text)
text2= re.sub(r"\n+", "", text2)
text2 = re.sub(r"\s,", "", text2)



text2 = re.sub(r"\(pop\)", "@@", text2)
text2 = re.sub(r"@@  @@", "@@" , text2)


result=open("pop2.txt", "w", encoding='UTF-8')
result.write(text2)
result.close()


lista2 = re.findall(r"@(?:\s|,|X)(.*?)@", text2)
lista3= re.findall(r"(^.*?)\s@", text2)
lista4= lista3 + lista2

del lista1[239]
del lista1[245]
del lista1[381]
del lista1[395]
del lista1[561]
del lista1[2550]

lista_de_listas = [[x, y] for x, y in zip(lista1, lista4)]

dicionario={}
dicionario = dict(lista_de_listas)

out = open ("pop.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()

