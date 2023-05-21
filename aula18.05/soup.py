from bs4 import BeautifulSoup
import requests
import json

url = "https://www.atlasdasaude.pt/doen%C3%A7asAaZ"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

'''
titles = soup.find_all("h3")
for title in titles:
    print(title.text)
'''

divs = soup.find_all("div", class_="views-row")
for div in divs:
    lista = []
    title = div.div.h3.a.text
    #print(div, end="\n\n")
    desc = div.find("div", class_="field-content").text
    lista.append({title.strip():desc.strip()})

file = open ("doenças.json", "w")
json.dump(lista, file, ensure_ascii=False, indent=4)
file.close
