#nos queremos automaticamente extrair as doenças que começam com todas as letras.

import requests
from bs4 import BeautifulSoup
import json

def extractDiseaseParser (url):
    page_html = requests.get(url).text
    page_soup=BeautifulSoup(page_html, "html.parser")
    print(page_soup)

    page_div = page_soup.find("div", class_="field-name-body")
    #estamos a remover os divs que apareciam no print na parte da page
    res = page_div.div.div
    res.name = "page" #altera o nome do elemento
    res.attrs = {} #altera os atributos para nada, neste caso
    return str(res)

def getDiseaseInfo(url):
    desc = div.find("div", class_="field-content").text
    title = div.div.h3.a.text
    return title, desc




url = "https://www.atlasdasaude.pt/doencasAaZ/"
url2 = "https://www.atlasdasaude.pt" #para conseguirmos obter o url certo, se nao a parte do doencasAaZ ia ser repetido

html=requests.get(url).text

soup=BeautifulSoup(html, "html.parser")

divs = soup.find_all("div", class_="views-summary views-summary-unformatted")

urls = []
for div in divs:
    #url = div.a["href"] -- para conseguir extrair o atributo href e nao a letra em si (div.a.text dava a letra)

    urls.append(url2 + div.a["href"]) #em vez de url pomos url2

#print("".join(urls)) -- torna a lista numa string e da print de tudo junto
#print("\n\n".join(urls)) -- separa os elementos da lista por \n\n

lista = [] 
for u in urls: #:1 so para vermos se fica bem, para noa bombardearmos o site. chama-se slice (0:1 é a mesma coisa)
    #print(u)
    html_=requests.get(u).text
    soup_ = BeautifulSoup(html_, "html.parser")
    divs = soup_.find_all("div", class_="views-row")

    for div in divs:
        page_url = url2 + div.div.h3.a["href"]
        page_info = extractDiseaseParser(page_url)
        title, desc = getDiseaseInfo(div)

        lista.append({title:{"desc":desc, "page":page_info}})

#está a ficar grande, vamos fazer funções
print(lista)
file = open ("doenças.json", "w", encoding="utf-8")
json.dump(lista, file, ensure_ascii=False, indent=4)
file.close

#para alem das descrições queremos tambem o conteudo da pagina correspondente



#TPC > Website Medscape (https://reference.medscape.com/) e extrair informação que quisermos e por num dicionario, ou seja ir percorrendo as hiperligações até chegar aqui (https://emedicine.medscape.com/article/137911-overview)
