from bs4 import BeautifulSoup #fazer o parse da pagina html e fazer extrações
import requests #para obtermos a pagina html
import json

url = "https://www.atlasdasaude.pt/doen%C3%A7asAaZ"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

'''
titles = soup.find_all("h3")
for title in titles:
    print(title.text)
'''

divs = soup.find_all("div", class_="views-row") #divs dos elementos que queremos extrair

lista = []
for div in divs:
    title = div.div.h3.a.text
    #print(div, end="\n\n")
    desc = div.find("div", class_="field-content").text
    lista.append({title.strip():desc.strip()})

file = open ("doenças.json", "w")
json.dump(lista, file, ensure_ascii=False, indent=4)
file.close


#nos queremos automaticamente extrair as doenças que começam com todas as letras. agora so temos as que começam com A