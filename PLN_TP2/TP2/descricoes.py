import json
import re

with open('descricoes.json', 'r', encoding="UTF-8") as f:
    dicio_desc = json.load(f)


with open('final.json', 'r', encoding="UTF-8") as f:
    final = json.load(f)


for key, value in dicio_desc.items():
    for key2, value2 in final.items():
        if key == key2:
            if 'definição' not in value2:
                value2['definição'] = value


file = open("final.json","w", encoding="utf-8")
json.dump(final,file, ensure_ascii=False, indent = 4)
file.close()


with open('final.json', 'r', encoding="UTF-8") as f:
    final = json.load(f)

for key, value in final.items():
    value["definição"]=re.sub(r'\[\d\]', '', value["definição"])

file = open("final.json","w", encoding="utf-8")
json.dump(final,file, ensure_ascii=False, indent = 4)
file.close()