import re
import json

ficheiro = open("dicionario_termos_medicos_pt_es_en.xml", encoding="utf-8")
text = ficheiro.read()

ficheiro.close()


def limpa(text):
    text = re.sub(r"</?b>","", text)
    return text

text = re.sub(r"</?page.*>", "", text) 
text = re.sub(r"</?fontspec.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) 
text = re.sub(r"\n<i>.*</i>\n", " ", text)
text = re.sub(r"<b>português – inglês – espanhol</b>", " ", text)
text = re.sub(r"<b>português</b>\n<b>–</b>\n<b>inglês</b>\n<b>–</b>\n<b>espanhol</b>\n", "", text)
text = re.sub(r"(<b>(.*?)</b>\n)?<b>[0-9]+</b>(\n<b>(.*?)</b>)?", "", text)
text = re.sub(r"<b>[A-Z]</b>\n", "", text)
text = re.sub(r"\n+", " ", text)
text = re.sub(r"\s+", " ", text)
text = re.sub(r"- ", "", text)

lista = re.findall(r"b>(.*?)</b>\sU\s(.*?)\sE\s(.*?) <", text) #o \. não é necessario pq pode nao ter ponto final
nova_lista = [[limpa(designacao), ingles, espanhol] for designacao, ingles, espanhol in lista]

   
principal = {}

for i in nova_lista:
    principal[i[0]] = {
        "en": i[1],
        "es": i[2],
    }

file_out = open("principal.json", "w", encoding="utf-8")
json.dump(principal, file_out, ensure_ascii=False, indent=4)
file_out.close()
