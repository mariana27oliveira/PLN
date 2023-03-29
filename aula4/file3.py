#outra forma de fazer o tpc
import json
import re

dicio_f = open("dicionario_medico_aula_teste.json", encoding="utf-8")

dicio = json.load(dicio_f)

livro_f = open("livro_teste.txt", encoding="utf-8")

result_f = open ("result.html", "w", encoding="utf-8")

text = livro_f.read()

#.strip(".!,;?") tira toda essa pontuação .strip() tira espaços

blacklist = ["e","de","são"]

nova_lista = [re.escape(designacao) for designacao in dicio.keys() if designacao not in blacklist]

#ou
#blacklist{"e","de","são"}
#nova_lista = dicio.keys() - blacklist

expressao = r"\b("+"|".join(nova_lista)+r")\b"

body="<body>"

def anotaTermo(termo):
    termo = termo[1]
    return "<a data-toggle='tooltip' href='' title='" + dicio[termo] + "'>"+termo+" </a>"
    

text = re.sub(expressao, anotaTermo, text)
#para por mais bonito
text = re.sub(r"\f", "<hr>", text)
text = re.sub(r"\n", "<br>", text)


body+= text
body += "</body>"

result_f.write(body)

result_f.close()

livro_f.close()
dicio_f.close()

