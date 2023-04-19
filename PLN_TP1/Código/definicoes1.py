import re
import json

ficheiro = open("Dicionario_de_termos_medicos_e_de_enfermagem.xml", encoding="utf-8")
text = ficheiro.read()

result_f=open("result2.txt", "w", encoding='UTF-8')


def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip() #para tirar os espaços em branco antes da descrição

text = re.sub (r"</?page.*>", "", text)
text = re.sub (r"<text top=\"[0-9]+\" left=\"[0-9]+\" width=\"[0-9]+\" height=\"11\" font=\"[0-9]+\">.*</text>", "", text)
text = re.sub (r"<text top=\"[0-9]+\" left=\"[0-9]+\" width=\"[0-9]+\" height=\"111\" font=\"[0-9]+\"><i>.*</i></text>", "", text)
text = re.sub (r"<text top=\"[0-9]+\" left=\"[0-9]+\" width=\"[0-9]+\" height=\"185\" font=\"[0-9]+\"><i>.*</i></text>", "", text)
text = re.sub (r"</?text.*?>", "", text) #*? para ele parar no primeiro > e não retirar info importante
text = re.sub (r"<i>", "", text)
text = re.sub (r"</i>", "", text)
text = re.sub (r"Sou Enfermagem - Cadastre-se grátis", "", text)
text = re.sub (r"\s-\s", "", text)
text = re.sub (r"-\s", "", text)
text = re.sub (r"<a href=\"https://souenfermagem.com.br\">em: https://souenfermagem.com.br</a>", "", text)
text = re.sub (r"<fontspec.*/>", "", text)
text = re.sub (r"\n\s", "\n", text)
text = re.sub (r"\n", "", text)
text = re.sub (r"○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○", "", text)
text = re.sub (r"-</b><b>", "", text)
text = re.sub (r"</b><b>", "", text)

lista = re.findall(r"<b>(.*?)</b>([^<]*)", text) #o \. não é necessario pq pode nao ter ponto final
lista = [[designacao.lower(), limpa(descricao)] for designacao, descricao in lista]

dicionario = dict(lista)

result_f.write(text)

out = open ("definicoes1.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()
