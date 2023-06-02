import requests
from bs4 import BeautifulSoup
import json
import re

sites={"Sistema digestivo": "https://pt.wikipedia.org/wiki/Categoria:Sistema_digestivo", 
       "Sistema urinário":"https://pt.wikipedia.org/wiki/Categoria:Sistema_urin%C3%A1rio", 
       "Sistema reprodutor":"https://pt.wikipedia.org/wiki/Categoria:Sistema_reprodutor", 
       "Sistema sensorial": "https://pt.wikipedia.org/wiki/Categoria:Sistema_sensorial",
       "Sistema endócrino": "https://pt.wikipedia.org/wiki/Categoria:Sistema_end%C3%B3crino",
       "Sistema nervoso" : "https://pt.wikipedia.org/wiki/Categoria:Sistema_nervoso",
       "Sistema tegumentar": "https://pt.wikipedia.org/wiki/Categoria:Sistema_tegumentar",
       "Sistema muscular": "https://pt.wikipedia.org/wiki/Categoria:Sistema_muscular",
       "Sistema circulatório": "https://pt.wikipedia.org/wiki/Categoria:Sistema_circulat%C3%B3rio",
       "Sistema respiratório": "https://pt.wikipedia.org/wiki/Categoria:Sistema_respirat%C3%B3rio",
       "Sistema esquelético": "https://pt.wikipedia.org/wiki/Categoria:Sistema_esquel%C3%A9tico"
       }

url_principal = "https://pt.wikipedia.org/"

def extractInfo(url):
    page_html = requests.get(url).text
    page_soup=BeautifulSoup(page_html, "html.parser")
    page_div = page_soup.find("div", class_="mw-parser-output")
    res = page_div.p.text
    return str(res)

lista = []
dicionario = {}
dicio_desc = {}

for categoria, site in sites.items():
    url=site
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html.parser")

    subsection = soup.body.find_all("div", id="mw-pages")
    print(categoria)
  
    
    for divs in subsection:
        divs = divs.find_all("div", class_="mw-category-group")
        for div in divs:
            termos = div.find_all("li")
            for termo in termos:
                
                #print (termo.a.text)
                chave = termo.text.strip().lower()
                if chave == "urinotórax" or chave == "predefinição:sistema nervoso":
                    break
                valor = categoria.strip().lower()
                dicionario[chave] = valor
                page_url = url_principal + termo.a["href"]
                page_info = extractInfo(page_url)
                dicio_desc[chave] = page_info


file = open("descricoes.json","w", encoding="utf-8")
json.dump(dicio_desc,file, ensure_ascii=False, indent = 4)
file.close()


file = open("novos.json","w", encoding="utf-8")
json.dump(dicionario,file, ensure_ascii=False, indent = 4)
file.close()


with open('novos.json', 'r', encoding="UTF-8") as f:
    novos = json.load(f)


with open('trabalho1.json', 'r', encoding="UTF-8") as f:
    trabalho1 = json.load(f)


for key in trabalho1:
    for key2 in novos:
        if key2 == key:
            trabalho1[key]['categoria'] = novos[key]


out = open ("final_original.json", "w", encoding="utf-8")
json.dump(trabalho1, out, ensure_ascii=False, indent=4)
out.close()

