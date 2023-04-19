import re
import json

ficheiro = open("anatomia_geral.xml", encoding="utf-8")
text = ficheiro.read()

result_f=open("result3.txt", "w", encoding='UTF-8')

def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip() #para tirar os espaços em branco antes da descrição

text = re.sub (r"</?page.*>", "", text)
text = re.sub (r"</?text.*?>", "", text) 
text = re.sub (r"<fontspec.*/>", "", text)
text = re.sub (r"[0-9]+", "", text)
text = re.sub (r"<image.*/>", "", text)
text = re.sub (r"\s[A-Z](<|,|\n)", "", text)
text = re.sub (r"<i><b>(.*)</b></i>", "", text)
text = re.sub (r"<i>", "<b>", text)
text = re.sub (r"</i>", "</b>", text)
text = re.sub (r"(\n)+", "", text)
text = re.sub (r"</b>(\s)+<b>", "</b><b>", text)
text = re.sub (r"</b><b>", "\n<b>", text)
text = re.sub (r"<b>", "@<b>", text)



lista = re.findall(r"<b>\s(.*?)\.</b>(.*?)\s+@", text) 
lista = [[designacao.lower(), limpa(descricao)] for designacao, descricao in lista]

dicionario = dict(lista) #converter em dicionário pq assim depois dá para ter tuplos


result_f.write(text)

out = open ("definicoes2.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()



print(lista)