import json
import re

#with open("dicionario_medico_aula.json", encoding="utf-8") as file:
with open("dicionario_medico_aula_teste.json", encoding="utf-8") as file:
    dicionario = json.load(file)

#with open("LIVRO-Doenças-do-Aparelho-Digestivos.html", "r+", encoding="utf-8") as file1:
with open("LIVRO-Doenças-do-Aparelho-Digestivos_teste.html", "r+", encoding="utf-8") as file1:
    texto = file1.read()
    linhas = texto.splitlines()

t = dicionario.keys()
texto =""
for l in linhas:
    palavras = re.sub(r"<.+?>", " ", l) 
    for p in re.findall(r"\b.+?\b", palavras): 
        p = p.lower()
        if p in t:
            l = re.sub(p, f"<a href title='{dicionario.get(p)}'>{p}</a>", l)
    texto += l+"\n"
with open("LIVRO-Doenças-do-Aparelho-Digestivos_teste.html", "w",  encoding="utf-8") as file1:
    file1.write(texto)


#foram usados ficheiros de teste de json e html mais pequenos que os originais para ser possível testar, utilizando os originais dava este erro:
#Traceback (most recent call last):
  #File "c:\Users\Asus\Desktop\UM\4º ano\2º semestre\PLN2\PLN\aula4\file2.py", line 42, in <module>
    #l = re.sub(w, r"<a href title=" + dicionario.get(w) + r">" + w + "</a>", l)
  #File "C:\Users\Asus\AppData\Local\Programs\Python\Python39\lib\re.py", line 210, in sub
    #return _compile(pattern, flags).sub(repl, string, count)
#MemoryError
