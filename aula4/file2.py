'''
#VERSÃO USANDO LISTA DE LISTAS NO JSON
import json
import re

file=open("dicionario_medico_aula.json", encoding="utf-8")
lista = json.load(file)

#json nao tem tuples então ficamos com uma lista de listas


file1=open("LIVRO-Doenças-do-Aparelho-Digestivos.html", "r+", encoding="utf-8")
texto = file1.read()
for [termo, definição] in lista:
    if termo in texto:
        texto = re.sub(termo, f'<a href="#{termo}">{definição}</a>', texto)

print("\nTexto modificado:\n", texto)
file1.write(texto)
file1.flush() 
file1.close()
'''

#VERSÃO USANDO DICIONÁRIO
import json
import re

with open("dicionario_medico_aula.json", encoding="utf-8") as file:
    dicionario = json.load(file)

with open("LIVRO-Doenças-do-Aparelho-Digestivos.html", "r+", encoding="utf-8") as file1:
    texto = file1.read()
    linhas = texto.splitlines()

t = dicionario.keys()
texto =""
for l in linhas:
    words = re.sub(r"<.+?>", " ", l) 
    for w in re.findall(r"\b.+?\b", words): 
        w = w.lower()
        if w in t:
            l = re.sub(w, r"<a href title=" + dicionario.get(w) + r">" + w + "</a>", l)
    texto += l+"\n"

file1.write(texto)


#dá este erro:
#Traceback (most recent call last):
  #File "c:\Users\Asus\Desktop\UM\4º ano\2º semestre\PLN2\PLN\aula4\file2.py", line 42, in <module>
    #l = re.sub(w, r"<a href title=" + dicionario.get(w) + r">" + w + "</a>", l)
  #File "C:\Users\Asus\AppData\Local\Programs\Python\Python39\lib\re.py", line 210, in sub
    #return _compile(pattern, flags).sub(repl, string, count)
#MemoryError
